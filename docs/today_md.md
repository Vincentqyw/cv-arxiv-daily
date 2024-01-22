<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#slam>SLAM</a></li>
      <ul>
        <li><a href=#Motion-Consistency-Loss-for-Monocular-Visual-Odometry-with-Attention-Based-Deep-Learning>Motion Consistency Loss for Monocular Visual Odometry with Attention-Based Deep Learning</a></li>
      </ul>
    </li>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#SCENES:-Subpixel-Correspondence-Estimation-With-Epipolar-Supervision>SCENES: Subpixel Correspondence Estimation With Epipolar Supervision</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#CBVS:-A-Large-Scale-Chinese-Image-Text-Benchmark-for-Real-World-Short-Video-Search-Scenarios>CBVS: A Large-Scale Chinese Image-Text Benchmark for Real-World Short Video Search Scenarios</a></li>
        <li><a href=#PhotoScout:-Synthesis-Powered-Multi-Modal-Image-Search>PhotoScout: Synthesis-Powered Multi-Modal Image Search</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#SCENES:-Subpixel-Correspondence-Estimation-With-Epipolar-Supervision>SCENES: Subpixel Correspondence Estimation With Epipolar Supervision</a></li>
      </ul>
    </li>
  </ol>
</details>

## SLAM  

### [Motion Consistency Loss for Monocular Visual Odometry with Attention-Based Deep Learning](http://arxiv.org/abs/2401.10857)  
André O. Françani, Marcos R. O. A. Maximo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Deep learning algorithms have driven expressive progress in many complex tasks. The loss function is a core component of deep learning techniques, guiding the learning process of neural networks. This paper contributes by introducing a consistency loss for visual odometry with deep learning-based approaches. The motion consistency loss explores repeated motions that appear in consecutive overlapped video clips. Experimental results show that our approach increased the performance of a model on the KITTI odometry benchmark.  
  </ol>  
</details>  
  
  



## SFM  

### [SCENES: Subpixel Correspondence Estimation With Epipolar Supervision](http://arxiv.org/abs/2401.10886)  
Dominik A. Kloepfer, João F. Henriques, Dylan Campbell  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Extracting point correspondences from two or more views of a scene is a fundamental computer vision problem with particular importance for relative camera pose estimation and structure-from-motion. Existing local feature matching approaches, trained with correspondence supervision on large-scale datasets, obtain highly-accurate matches on the test sets. However, they do not generalise well to new datasets with different characteristics to those they were trained on, unlike classic feature extractors. Instead, they require finetuning, which assumes that ground-truth correspondences or ground-truth camera poses and 3D structure are available. We relax this assumption by removing the requirement of 3D structure, e.g., depth maps or point clouds, and only require camera pose information, which can be obtained from odometry. We do so by replacing correspondence losses with epipolar losses, which encourage putative matches to lie on the associated epipolar line. While weaker than correspondence supervision, we observe that this cue is sufficient for finetuning existing models on new data. We then further relax the assumption of known camera poses by using pose estimates in a novel bootstrapping approach. We evaluate on highly challenging datasets, including an indoor drone dataset and an outdoor smartphone camera dataset, and obtain state-of-the-art results without strong supervision.  
  </ol>  
</details>  
  
  



## Visual Localization  

### [CBVS: A Large-Scale Chinese Image-Text Benchmark for Real-World Short Video Search Scenarios](http://arxiv.org/abs/2401.10475)  
Xiangshuo Qiao, Xianxin Li, Xiaozhe Qu, Jie Zhang, Yang Liu, Yu Luo, Cihang Jin, Jin Ma  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Vision-Language Models pre-trained on large-scale image-text datasets have shown superior performance in downstream tasks such as image retrieval. Most of the images for pre-training are presented in the form of open domain common-sense visual elements. Differently, video covers in short video search scenarios are presented as user-originated contents that provide important visual summaries of videos. In addition, a portion of the video covers come with manually designed cover texts that provide semantic complements. In order to fill in the gaps in short video cover data, we establish the first large-scale cover-text benchmark for Chinese short video search scenarios. Specifically, we release two large-scale datasets CBVS-5M/10M to provide short video covers, and the manual fine-labeling dataset CBVS-20K to provide real user queries, which serves as an image-text benchmark test in the Chinese short video search field. To integrate the semantics of cover text in the case of modality missing, we propose UniCLIP where cover texts play a guiding role during training, however are not relied upon by inference. Extensive evaluation on CBVS-20K demonstrates the excellent performance of our proposal. UniCLIP has been deployed to Tencent's online video search systems with hundreds of millions of visits and achieved significant gains. The complete dataset, code and checkpoints will be available upon release.  
  </ol>  
</details>  
  
### [PhotoScout: Synthesis-Powered Multi-Modal Image Search](http://arxiv.org/abs/2401.10464)  
Celeste Barnaby, Qiaochu Chen, Chenglong Wang, Isil Dillig  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Due to the availability of increasingly large amounts of visual data, there is a growing need for tools that can help users find relevant images. While existing tools can perform image retrieval based on similarity or metadata, they fall short in scenarios that necessitate semantic reasoning about the content of the image. This paper explores a new multi-modal image search approach that allows users to conveniently specify and perform semantic image search tasks. With our tool, PhotoScout, the user interactively provides natural language descriptions, positive and negative examples, and object tags to specify their search tasks. Under the hood, PhotoScout is powered by a program synthesis engine that generates visual queries in a domain-specific language and executes the synthesized program to retrieve the desired images. In a study with 25 participants, we observed that PhotoScout allows users to perform image retrieval tasks more accurately and with less manual effort.  
  </ol>  
</details>  
  
  



## Image Matching  

### [SCENES: Subpixel Correspondence Estimation With Epipolar Supervision](http://arxiv.org/abs/2401.10886)  
Dominik A. Kloepfer, João F. Henriques, Dylan Campbell  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Extracting point correspondences from two or more views of a scene is a fundamental computer vision problem with particular importance for relative camera pose estimation and structure-from-motion. Existing local feature matching approaches, trained with correspondence supervision on large-scale datasets, obtain highly-accurate matches on the test sets. However, they do not generalise well to new datasets with different characteristics to those they were trained on, unlike classic feature extractors. Instead, they require finetuning, which assumes that ground-truth correspondences or ground-truth camera poses and 3D structure are available. We relax this assumption by removing the requirement of 3D structure, e.g., depth maps or point clouds, and only require camera pose information, which can be obtained from odometry. We do so by replacing correspondence losses with epipolar losses, which encourage putative matches to lie on the associated epipolar line. While weaker than correspondence supervision, we observe that this cue is sufficient for finetuning existing models on new data. We then further relax the assumption of known camera poses by using pose estimates in a novel bootstrapping approach. We evaluate on highly challenging datasets, including an indoor drone dataset and an outdoor smartphone camera dataset, and obtain state-of-the-art results without strong supervision.  
  </ol>  
</details>  
  
  



