<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#BEV-CLIP:-Multi-modal-BEV-Retrieval-Methodology-for-Complex-Scene-in-Autonomous-Driving>BEV-CLIP: Multi-modal BEV Retrieval Methodology for Complex Scene in Autonomous Driving</a></li>
        <li><a href=#Multi-Granularity-Representation-Learning-for-Sketch-based-Dynamic-Face-Image-Retrieval>Multi-Granularity Representation Learning for Sketch-based Dynamic Face Image Retrieval</a></li>
        <li><a href=#Bayesian-Recursive-Information-Optical-Imaging:-A-Ghost-Imaging-Scheme-Based-on-Bayesian-Filtering>Bayesian Recursive Information Optical Imaging: A Ghost Imaging Scheme Based on Bayesian Filtering</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#6D-Diff:-A-Keypoint-Diffusion-Framework-for-6D-Object-Pose-Estimation>6D-Diff: A Keypoint Diffusion Framework for 6D Object Pose Estimation</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#Street-Gaussians-for-Modeling-Dynamic-Urban-Scenes>Street Gaussians for Modeling Dynamic Urban Scenes</a></li>
        <li><a href=#Noise-NeRF:-Hide-Information-in-Neural-Radiance-Fields-using-Trainable-Noise>Noise-NeRF: Hide Information in Neural Radiance Fields using Trainable Noise</a></li>
        <li><a href=#3D-Visibility-aware-Generalizable-Neural-Radiance-Fields-for-Interacting-Hands>3D Visibility-aware Generalizable Neural Radiance Fields for Interacting Hands</a></li>
        <li><a href=#Sharp-NeRF:-Grid-based-Fast-Deblurring-Neural-Radiance-Fields-Using-Sharpness-Prior>Sharp-NeRF: Grid-based Fast Deblurring Neural Radiance Fields Using Sharpness Prior</a></li>
        <li><a href=#GD^2-NeRF:-Generative-Detail-Compensation-via-GAN-and-Diffusion-for-One-shot-Generalizable-Neural-Radiance-Fields>GD^2-NeRF: Generative Detail Compensation via GAN and Diffusion for One-shot Generalizable Neural Radiance Fields</a></li>
        <li><a href=#Inpaint4DNeRF:-Promptable-Spatio-Temporal-NeRF-Inpainting-with-Generative-Diffusion-Models>Inpaint4DNeRF: Promptable Spatio-Temporal NeRF Inpainting with Generative Diffusion Models</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [BEV-CLIP: Multi-modal BEV Retrieval Methodology for Complex Scene in Autonomous Driving](http://arxiv.org/abs/2401.01065)  
Dafeng Wei, Tian Gao, Zhengyu Jia, Changwei Cai, Chengkai Hou, Peng Jia, Fu Liu, Kun Zhan, Jingchen Fan, Yixing Zhao, Yang Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The demand for the retrieval of complex scene data in autonomous driving is increasing, especially as passenger vehicles have been equipped with the ability to navigate urban settings, with the imperative to address long-tail scenarios. Meanwhile, under the pre-existing two dimensional image retrieval method, some problems may arise with scene retrieval, such as lack of global feature representation and subpar text retrieval ability. To address these issues, we have proposed \textbf{BEV-CLIP}, the first multimodal Bird's-Eye View(BEV) retrieval methodology that utilizes descriptive text as an input to retrieve corresponding scenes. This methodology applies the semantic feature extraction abilities of a large language model (LLM) to facilitate zero-shot retrieval of extensive text descriptions, and incorporates semi-structured information from a knowledge graph to improve the semantic richness and variety of the language embedding. Our experiments result in 87.66% accuracy on NuScenes dataset in text-to-BEV feature retrieval. The demonstrated cases in our paper support that our retrieval method is also indicated to be effective in identifying certain long-tail corner scenes.  
  </ol>  
</details>  
**comments**: Under review of CVPR 2024  
  
### [Multi-Granularity Representation Learning for Sketch-based Dynamic Face Image Retrieval](http://arxiv.org/abs/2401.00371)  
[[code](https://github.com/ddw2aigroup2cqupt/mgrl)]  
Liang Wang, Dawei Dai, Shiyu Fu, Guoyin Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    In specific scenarios, face sketch can be used to identify a person. However, drawing a face sketch often requires exceptional skill and is time-consuming, limiting its widespread applications in actual scenarios. The new framework of sketch less face image retrieval (SLFIR)[1] attempts to overcome the barriers by providing a means for humans and machines to interact during the drawing process. Considering SLFIR problem, there is a large gap between a partial sketch with few strokes and any whole face photo, resulting in poor performance at the early stages. In this study, we propose a multigranularity (MG) representation learning (MGRL) method to address the SLFIR problem, in which we learn the representation of different granularity regions for a partial sketch, and then, by combining all MG regions of the sketches and images, the final distance was determined. In the experiments, our method outperformed state-of-the-art baselines in terms of early retrieval on two accessible datasets. Codes are available at https://github.com/ddw2AIGROUP2CQUPT/MGRL.  
  </ol>  
</details>  
**comments**: 5 pages,5 figures  
  
### [Bayesian Recursive Information Optical Imaging: A Ghost Imaging Scheme Based on Bayesian Filtering](http://arxiv.org/abs/2401.00032)  
Long-Kun Du, Chenyu Hu, Shuang Liu, Chenjin Deng, Chaoran Wang, Zunwang Bo, Mingliang Chen, Wei-Tao Liu, Shensheng Han  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Computational imaging~(CI) has been attracting a lot of interest in recent years for its superiority over traditional imaging in various applications. In CI systems, information is generally acquired in an encoded form and subsequently decoded via processing algorithms, which is quite in line with the information transmission mode of modern communication, and leads to emerging studies from the viewpoint of information optical imaging. Currently, one of the most important issues to be theoretically studied for CI is to quantitatively evaluate the fundamental ability of information acquisition, which is essential for both objective performance assessment and efficient design of imaging system. In this paper, by incorporating the Bayesian filtering paradigm, we propose a framework for CI that enables quantitative evaluation and design of the imaging system, and demonstate it based on ghost imaging. In specific, this framework can provide a quantitative evaluation on the acquired information through Fisher information and Cram\'er-Rao Lower Bound (CRLB), and the intrinsic performance of the imaging system can be accessed in real-time. With simulation and experiments, the framework is validated and compared with existing linear unbiased algorithms. In particular, the image retrieval can reach the CRLB. Furthermore, information-driven adaptive design for optimizing the information acquisition procedure is also achieved. By quantitative describing and efficient designing, the proposed framework is expected to promote the practical applications of CI techniques.  
  </ol>  
</details>  
  
  



## Keypoint Detection  

### [6D-Diff: A Keypoint Diffusion Framework for 6D Object Pose Estimation](http://arxiv.org/abs/2401.00029)  
Li Xu, Haoxuan Qu, Yujun Cai, Jun Liu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Estimating the 6D object pose from a single RGB image often involves noise and indeterminacy due to challenges such as occlusions and cluttered backgrounds. Meanwhile, diffusion models have shown appealing performance in generating high-quality images from random noise with high indeterminacy through step-by-step denoising. Inspired by their denoising capability, we propose a novel diffusion-based framework (6D-Diff) to handle the noise and indeterminacy in object pose estimation for better performance. In our framework, to establish accurate 2D-3D correspondence, we formulate 2D keypoints detection as a reverse diffusion (denoising) process. To facilitate such a denoising process, we design a Mixture-of-Cauchy-based forward diffusion process and condition the reverse process on the object features. Extensive experiments on the LM-O and YCB-V datasets demonstrate the effectiveness of our framework.  
  </ol>  
</details>  
**comments**: Fix typo  
  
  



## NeRF  

### [Street Gaussians for Modeling Dynamic Urban Scenes](http://arxiv.org/abs/2401.01339)  
Yunzhi Yan, Haotong Lin, Chenxu Zhou, Weijie Wang, Haiyang Sun, Kun Zhan, Xianpeng Lang, Xiaowei Zhou, Sida Peng  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper aims to tackle the problem of modeling dynamic urban street scenes from monocular videos. Recent methods extend NeRF by incorporating tracked vehicle poses to animate vehicles, enabling photo-realistic view synthesis of dynamic urban street scenes. However, significant limitations are their slow training and rendering speed, coupled with the critical need for high precision in tracked vehicle poses. We introduce Street Gaussians, a new explicit scene representation that tackles all these limitations. Specifically, the dynamic urban street is represented as a set of point clouds equipped with semantic logits and 3D Gaussians, each associated with either a foreground vehicle or the background. To model the dynamics of foreground object vehicles, each object point cloud is optimized with optimizable tracked poses, along with a dynamic spherical harmonics model for the dynamic appearance. The explicit representation allows easy composition of object vehicles and background, which in turn allows for scene editing operations and rendering at 133 FPS (1066 $\times$ 1600 resolution) within half an hour of training. The proposed method is evaluated on multiple challenging benchmarks, including KITTI and Waymo Open datasets. Experiments show that the proposed method consistently outperforms state-of-the-art methods across all datasets. Furthermore, the proposed representation delivers performance on par with that achieved using precise ground-truth poses, despite relying only on poses from an off-the-shelf tracker. The code is available at https://zju3dv.github.io/street_gaussians/.  
  </ol>  
</details>  
**comments**: Project page: https://zju3dv.github.io/street_gaussians/  
  
### [Noise-NeRF: Hide Information in Neural Radiance Fields using Trainable Noise](http://arxiv.org/abs/2401.01216)  
Qinglong Huang, Yong Liao, Yanbin Hao, Pengyuan Zhou  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural radiance fields (NeRF) have been proposed as an innovative 3D representation method. While attracting lots of attention, NeRF faces critical issues such as information confidentiality and security. Steganography is a technique used to embed information in another object as a means of protecting information security. Currently, there are few related studies on NeRF steganography, facing challenges in low steganography quality, model weight damage, and a limited amount of steganographic information. This paper proposes a novel NeRF steganography method based on trainable noise: Noise-NeRF. Furthermore, we propose the Adaptive Pixel Selection strategy and Pixel Perturbation strategy to improve the steganography quality and efficiency. The extensive experiments on open-source datasets show that Noise-NeRF provides state-of-the-art performances in both steganography quality and rendering quality, as well as effectiveness in super-resolution image steganography.  
  </ol>  
</details>  
  
### [3D Visibility-aware Generalizable Neural Radiance Fields for Interacting Hands](http://arxiv.org/abs/2401.00979)  
Xuan Huang, Hanhui Li, Zejun Yang, Zhisheng Wang, Xiaodan Liang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural radiance fields (NeRFs) are promising 3D representations for scenes, objects, and humans. However, most existing methods require multi-view inputs and per-scene training, which limits their real-life applications. Moreover, current methods focus on single-subject cases, leaving scenes of interacting hands that involve severe inter-hand occlusions and challenging view variations remain unsolved. To tackle these issues, this paper proposes a generalizable visibility-aware NeRF (VA-NeRF) framework for interacting hands. Specifically, given an image of interacting hands as input, our VA-NeRF first obtains a mesh-based representation of hands and extracts their corresponding geometric and textural features. Subsequently, a feature fusion module that exploits the visibility of query points and mesh vertices is introduced to adaptively merge features of both hands, enabling the recovery of features in unseen areas. Additionally, our VA-NeRF is optimized together with a novel discriminator within an adversarial learning paradigm. In contrast to conventional discriminators that predict a single real/fake label for the synthesized image, the proposed discriminator generates a pixel-wise visibility map, providing fine-grained supervision for unseen areas and encouraging the VA-NeRF to improve the visual quality of synthesized images. Experiments on the Interhand2.6M dataset demonstrate that our proposed VA-NeRF outperforms conventional NeRFs significantly. Project Page: \url{https://github.com/XuanHuang0/VANeRF}.  
  </ol>  
</details>  
**comments**: Accepted by AAAI-24  
  
### [Sharp-NeRF: Grid-based Fast Deblurring Neural Radiance Fields Using Sharpness Prior](http://arxiv.org/abs/2401.00825)  
[[code](https://github.com/benhenryl/sharpnerf)]  
Byeonghyeon Lee, Howoong Lee, Usman Ali, Eunbyung Park  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Fields (NeRF) have shown remarkable performance in neural rendering-based novel view synthesis. However, NeRF suffers from severe visual quality degradation when the input images have been captured under imperfect conditions, such as poor illumination, defocus blurring, and lens aberrations. Especially, defocus blur is quite common in the images when they are normally captured using cameras. Although few recent studies have proposed to render sharp images of considerably high-quality, yet they still face many key challenges. In particular, those methods have employed a Multi-Layer Perceptron (MLP) based NeRF, which requires tremendous computational time. To overcome these shortcomings, this paper proposes a novel technique Sharp-NeRF -- a grid-based NeRF that renders clean and sharp images from the input blurry images within half an hour of training. To do so, we used several grid-based kernels to accurately model the sharpness/blurriness of the scene. The sharpness level of the pixels is computed to learn the spatially varying blur kernels. We have conducted experiments on the benchmarks consisting of blurry images and have evaluated full-reference and non-reference metrics. The qualitative and quantitative results have revealed that our approach renders the sharp novel views with vivid colors and fine details, and it has considerably faster training time than the previous works. Our project page is available at https://benhenryl.github.io/SharpNeRF/  
  </ol>  
</details>  
**comments**: Accepted to WACV 2024  
  
### [GD^2-NeRF: Generative Detail Compensation via GAN and Diffusion for One-shot Generalizable Neural Radiance Fields](http://arxiv.org/abs/2401.00616)  
Xiao Pan, Zongxin Yang, Shuai Bai, Yi Yang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    In this paper, we focus on the One-shot Novel View Synthesis (O-NVS) task which targets synthesizing photo-realistic novel views given only one reference image per scene. Previous One-shot Generalizable Neural Radiance Fields (OG-NeRF) methods solve this task in an inference-time finetuning-free manner, yet suffer the blurry issue due to the encoder-only architecture that highly relies on the limited reference image. On the other hand, recent diffusion-based image-to-3d methods show vivid plausible results via distilling pre-trained 2D diffusion models into a 3D representation, yet require tedious per-scene optimization. Targeting these issues, we propose the GD $^2$-NeRF, a Generative Detail compensation framework via GAN and Diffusion that is both inference-time finetuning-free and with vivid plausible details. In detail, following a coarse-to-fine strategy, GD$^2$-NeRF is mainly composed of a One-stage Parallel Pipeline (OPP) and a 3D-consistent Detail Enhancer (Diff3DE). At the coarse stage, OPP first efficiently inserts the GAN model into the existing OG-NeRF pipeline for primarily relieving the blurry issue with in-distribution priors captured from the training dataset, achieving a good balance between sharpness (LPIPS, FID) and fidelity (PSNR, SSIM). Then, at the fine stage, Diff3DE further leverages the pre-trained image diffusion models to complement rich out-distribution details while maintaining decent 3D consistency. Extensive experiments on both the synthetic and real-world datasets show that GD$^2$ -NeRF noticeably improves the details while without per-scene finetuning.  
  </ol>  
</details>  
**comments**: Reading with Macbook Preview is recommended for best quality;
  Submitted to Journal  
  
### [Inpaint4DNeRF: Promptable Spatio-Temporal NeRF Inpainting with Generative Diffusion Models](http://arxiv.org/abs/2401.00208)  
Han Jiang, Haosen Sun, Ruoxuan Li, Chi-Keung Tang, Yu-Wing Tai  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Current Neural Radiance Fields (NeRF) can generate photorealistic novel views. For editing 3D scenes represented by NeRF, with the advent of generative models, this paper proposes Inpaint4DNeRF to capitalize on state-of-the-art stable diffusion models (e.g., ControlNet) for direct generation of the underlying completed background content, regardless of static or dynamic. The key advantages of this generative approach for NeRF inpainting are twofold. First, after rough mask propagation, to complete or fill in previously occluded content, we can individually generate a small subset of completed images with plausible content, called seed images, from which simple 3D geometry proxies can be derived. Second and the remaining problem is thus 3D multiview consistency among all completed images, now guided by the seed images and their 3D proxies. Without other bells and whistles, our generative Inpaint4DNeRF baseline framework is general which can be readily extended to 4D dynamic NeRFs, where temporal consistency can be naturally handled in a similar way as our multiview consistency.  
  </ol>  
</details>  
  
  



