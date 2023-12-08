'''
Send an multipart email with HTML and plain text alternatives. The message
should be constructed as a plain-text file of the following format:

    From: Your Name <your@email.com>
    To: Recipient One <recipient@to.com>
    Subject: Your subject line
    ---
    Markdown content here
The script accepts content from stdin and, by default, prints the raw
generated email content to stdout.
Preview your message on OS X by invoking the script with `-p` or
`--preview`, and it will open in your default mail client.
To send the message, invoke with `-s` or `--send`. You must have a
JSON file in your home directory named `.markdown-to-email.json`
with the following keys:
    {
        "username": "smtp-username",
        "smtp": "smtp.gmail.com:587",
        "password": "your-password"
    }
Enjoy!
'''


import os
import re
import sys
import json
import argparse
import smtplib
import subprocess
import yaml
import logging
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from daily_arxiv import sort_papers
try:
    import pygments
    import markdown
except ImportError:
    print('This script requires pygements and markdown to be installed.')
    print('Please:')
    print('   pip install pygments markdown')
    sys.exit(0)


class SendEmail(object):
    def __init__(self, config_file) -> None:
        self.config = self.readconfig(config_file)
        self.css = subprocess.check_output(
            ['pygmentize', '-S', 'default', '-f', 'html'])
        self.markdown_content = ''
        self.html_content = ''

    def readconfig(self, config_file="config.yaml") -> dict:
        with open(config_file, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        config['emails']['username'] = os.environ["USERNAME"]
        config['emails']['smtp'] = os.environ["SMTP"]
        config['emails']['password'] = os.environ["PASSWORD"]
        return config['emails']

    def transform_md(self, raw_md):
        """_summary_

        Parameters
        ----------
        raw_md : _type_ string(content or path) #TODO: path
            _description_ raw paper markdown content

        Returns
        -------
        markdown_content, html_content : _type_ string, string
            _description_ md string and html string
        """
        self.markdown_content = raw_md.strip()
        self.html_content = markdown.markdown(
            self.markdown_content, ['extra', 'codehilite'])
        self.html_content = '<style type="text/css">' + \
            self.css+'</style>' + self.html_content

        return self.markdown_content, self.html_content

    def send(self, headers):
        """_summary_

        Parameters
        ----------
        headers : _type_ config['emails']['headers']
            _description_
        """
        message = MIMEMultipart('alternative')
        message['To'] = headers['To']
        message['From'] = headers['From']
        message['Subject'] = headers['Subject']

        # attach the message parts
        message.attach(MIMEText(self.markdown_content, 'plain'))
        message.attach(MIMEText(self.html_content, 'html'))

        if headers['send']:
            to = message['To'].split(', ')

            server = smtplib.SMTP(self.config['smtp'])
            server.starttls()
            server.login(self.config['username'], self.config['password'])
            server.sendmail(message['From'], to, message.as_string())
            server.quit()
        elif headers['preview']:
            open('/tmp/preview.eml', 'w').write(message.as_string())
            os.system('open -a Mail /tmp/preview.eml')
        else:
            print(message.as_string())

    def json2md(self, data,
                md_filename,
                task='',
                to_web=False,
                use_title=True,
                use_tc=True,
                use_b2t=True):

        def pretty_math(s:str) -> str:
            ret = ''
            match = re.search(r"\$.*\$", s)
            if match == None:
                return s
            math_start,math_end = match.span()
            space_trail = space_leading = ''
            if s[:math_start][-1] != ' ' and '*' != s[:math_start][-1]: space_trail = ' '
            if s[math_end:][0] != ' ' and '*' != s[math_end:][0]: space_leading = ' '
            ret += s[:math_start]
            ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
            ret += s[math_end:]
            return ret

        DateNow = datetime.date.today()
        DateNow = str(DateNow)
        DateNow = DateNow.replace('-','.')

        # clean README.md if daily already exist else create it
        with open(md_filename,"w+") as f:
            pass

        # write data into README.md
        with open(md_filename,"a+") as f:

            if (use_title == True) and (to_web == True):
                f.write("---\n" + "layout: default\n" + "---\n\n")

            # if show_badge == True:
            #     f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            #     f.write(f"[![Forks][forks-shield]][forks-url]\n")
            #     f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            #     f.write(f"[![Issues][issues-shield]][issues-url]\n\n")

            if use_title == True:
                #f.write(("<p align="center"><h1 align="center"><br><ins>CV-ARXIV-DAILY"
                #         "</ins><br>Automatically Update CV Papers Daily</h1></p>\n"))
                f.write("## Updated on " + DateNow + "\n")
            else:
                f.write("> Updated on " + DateNow + "\n")

            #Add: table of contents
            if use_tc == True:
                f.write("<details>\n")
                f.write("  <summary>Table of Contents</summary>\n")
                f.write("  <ol>\n")
                for keyword in data.keys():
                    day_content = data[keyword]
                    if not day_content:
                        continue
                    kw = keyword.replace(' ','-')
                    f.write(f"    <li><a href=#{kw.lower()}>{keyword}</a></li>\n")
                f.write("  </ol>\n")
                f.write("</details>\n\n")

            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                # the head of each part
                f.write(f"## {keyword}\n\n")

                if use_title == True :
                    if to_web == False:
                        f.write("|Publish Date|Title|Authors|PDF|Code|\n" + "|---|---|---|---|---|\n")
                    else:
                        f.write("| Publish Date | Title | Authors | PDF | Code |\n")
                        f.write("|:---------|:-----------------------|:---------|:------|:------|\n")

                # sort papers by date
                day_content = sort_papers(day_content)

                for _,v in day_content.items():
                    if v is not None:
                        f.write(pretty_math(v)) # make latex pretty

                f.write(f"\n")

                #Add: back to top
                if use_b2t:
                    top_info = f"#Updated on {DateNow}"
                    top_info = top_info.replace(' ','-').replace('.','')
                    f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")

            # if show_badge == True:
            #     # we don't like long string, break it!
            #     f.write((f"[contributors-shield]: https://img.shields.io/github/"
            #             f"contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge\n"))
            #     f.write((f"[contributors-url]: https://github.com/Vincentqyw/"
            #             f"cv-arxiv-daily/graphs/contributors\n"))
            #     f.write((f"[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/"
            #             f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            #     f.write((f"[forks-url]: https://github.com/Vincentqyw/"
            #             f"cv-arxiv-daily/network/members\n"))
            #     f.write((f"[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/"
            #             f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            #     f.write((f"[stars-url]: https://github.com/Vincentqyw/"
            #             f"cv-arxiv-daily/stargazers\n"))
            #     f.write((f"[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/"
            #             f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            #     f.write((f"[issues-url]: https://github.com/Vincentqyw/"
            #             f"cv-arxiv-daily/issues\n\n"))

        logging.info(f"{task} finished")
