<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#Local-Feature-Matching-Using-Deep-Learning:-A-Survey>Local Feature Matching Using Deep Learning: A Survey</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Improved-Scene-Landmark-Detection-for-Camera-Localization>Improved Scene Landmark Detection for Camera Localization</a></li>
        <li><a href=#Local-Feature-Matching-Using-Deep-Learning:-A-Survey>Local Feature Matching Using Deep Learning: A Survey</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#Improved-Scene-Landmark-Detection-for-Camera-Localization>Improved Scene Landmark Detection for Camera Localization</a></li>
        <li><a href=#Local-Feature-Matching-Using-Deep-Learning:-A-Survey>Local Feature Matching Using Deep Learning: A Survey</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#CARFF:-Conditional-Auto-encoded-Radiance-Field-for-3D-Scene-Forecasting>CARFF: Conditional Auto-encoded Radiance Field for 3D Scene Forecasting</a></li>
        <li><a href=#Semantic-Anything-in-3D-Gaussians>Semantic Anything in 3D Gaussians</a></li>
      </ul>
    </li>
  </ol>
</details>

## SFM  

### [Local Feature Matching Using Deep Learning: A Survey](http://arxiv.org/abs/2401.17592)  
Shibiao Xu, Shunpeng Chen, Rongtao Xu, Changwei Wang, Peng Lu, Li Guo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Local feature matching enjoys wide-ranging applications in the realm of computer vision, encompassing domains such as image retrieval, 3D reconstruction, and object recognition. However, challenges persist in improving the accuracy and robustness of matching due to factors like viewpoint and lighting variations. In recent years, the introduction of deep learning models has sparked widespread exploration into local feature matching techniques. The objective of this endeavor is to furnish a comprehensive overview of local feature matching methods. These methods are categorized into two key segments based on the presence of detectors. The Detector-based category encompasses models inclusive of Detect-then-Describe, Joint Detection and Description, Describe-then-Detect, as well as Graph Based techniques. In contrast, the Detector-free category comprises CNN Based, Transformer Based, and Patch Based methods. Our study extends beyond methodological analysis, incorporating evaluations of prevalent datasets and metrics to facilitate a quantitative comparison of state-of-the-art techniques. The paper also explores the practical application of local feature matching in diverse domains such as Structure from Motion, Remote Sensing Image Registration, and Medical Image Registration, underscoring its versatility and significance across various fields. Ultimately, we endeavor to outline the current challenges faced in this domain and furnish future research directions, thereby serving as a reference for researchers involved in local feature matching and its interconnected domains.  
  </ol>  
</details>  
  
  



## Visual Localization  

### [Improved Scene Landmark Detection for Camera Localization](http://arxiv.org/abs/2401.18083)  
[[code](https://github.com/microsoft/scenelandmarklocalization)]  
Tien Do, Sudipta N. Sinha  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Camera localization methods based on retrieval, local feature matching, and 3D structure-based pose estimation are accurate but require high storage, are slow, and are not privacy-preserving. A method based on scene landmark detection (SLD) was recently proposed to address these limitations. It involves training a convolutional neural network (CNN) to detect a few predetermined, salient, scene-specific 3D points or landmarks and computing camera pose from the associated 2D-3D correspondences. Although SLD outperformed existing learning-based approaches, it was notably less accurate than 3D structure-based methods. In this paper, we show that the accuracy gap was due to insufficient model capacity and noisy labels during training. To mitigate the capacity issue, we propose to split the landmarks into subgroups and train a separate network for each subgroup. To generate better training labels, we propose using dense reconstructions to estimate visibility of scene landmarks. Finally, we present a compact architecture to improve memory efficiency. Accuracy wise, our approach is on par with state of the art structure based methods on the INDOOR-6 dataset but runs significantly faster and uses less storage. Code and models can be found at https://github.com/microsoft/SceneLandmarkLocalization.  
  </ol>  
</details>  
**comments**: To be presented at 3DV 2024  
  
### [Local Feature Matching Using Deep Learning: A Survey](http://arxiv.org/abs/2401.17592)  
Shibiao Xu, Shunpeng Chen, Rongtao Xu, Changwei Wang, Peng Lu, Li Guo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Local feature matching enjoys wide-ranging applications in the realm of computer vision, encompassing domains such as image retrieval, 3D reconstruction, and object recognition. However, challenges persist in improving the accuracy and robustness of matching due to factors like viewpoint and lighting variations. In recent years, the introduction of deep learning models has sparked widespread exploration into local feature matching techniques. The objective of this endeavor is to furnish a comprehensive overview of local feature matching methods. These methods are categorized into two key segments based on the presence of detectors. The Detector-based category encompasses models inclusive of Detect-then-Describe, Joint Detection and Description, Describe-then-Detect, as well as Graph Based techniques. In contrast, the Detector-free category comprises CNN Based, Transformer Based, and Patch Based methods. Our study extends beyond methodological analysis, incorporating evaluations of prevalent datasets and metrics to facilitate a quantitative comparison of state-of-the-art techniques. The paper also explores the practical application of local feature matching in diverse domains such as Structure from Motion, Remote Sensing Image Registration, and Medical Image Registration, underscoring its versatility and significance across various fields. Ultimately, we endeavor to outline the current challenges faced in this domain and furnish future research directions, thereby serving as a reference for researchers involved in local feature matching and its interconnected domains.  
  </ol>  
</details>  
  
  



## Image Matching  

### [Improved Scene Landmark Detection for Camera Localization](http://arxiv.org/abs/2401.18083)  
[[code](https://github.com/microsoft/scenelandmarklocalization)]  
Tien Do, Sudipta N. Sinha  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Camera localization methods based on retrieval, local feature matching, and 3D structure-based pose estimation are accurate but require high storage, are slow, and are not privacy-preserving. A method based on scene landmark detection (SLD) was recently proposed to address these limitations. It involves training a convolutional neural network (CNN) to detect a few predetermined, salient, scene-specific 3D points or landmarks and computing camera pose from the associated 2D-3D correspondences. Although SLD outperformed existing learning-based approaches, it was notably less accurate than 3D structure-based methods. In this paper, we show that the accuracy gap was due to insufficient model capacity and noisy labels during training. To mitigate the capacity issue, we propose to split the landmarks into subgroups and train a separate network for each subgroup. To generate better training labels, we propose using dense reconstructions to estimate visibility of scene landmarks. Finally, we present a compact architecture to improve memory efficiency. Accuracy wise, our approach is on par with state of the art structure based methods on the INDOOR-6 dataset but runs significantly faster and uses less storage. Code and models can be found at https://github.com/microsoft/SceneLandmarkLocalization.  
  </ol>  
</details>  
**comments**: To be presented at 3DV 2024  
  
### [Local Feature Matching Using Deep Learning: A Survey](http://arxiv.org/abs/2401.17592)  
Shibiao Xu, Shunpeng Chen, Rongtao Xu, Changwei Wang, Peng Lu, Li Guo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Local feature matching enjoys wide-ranging applications in the realm of computer vision, encompassing domains such as image retrieval, 3D reconstruction, and object recognition. However, challenges persist in improving the accuracy and robustness of matching due to factors like viewpoint and lighting variations. In recent years, the introduction of deep learning models has sparked widespread exploration into local feature matching techniques. The objective of this endeavor is to furnish a comprehensive overview of local feature matching methods. These methods are categorized into two key segments based on the presence of detectors. The Detector-based category encompasses models inclusive of Detect-then-Describe, Joint Detection and Description, Describe-then-Detect, as well as Graph Based techniques. In contrast, the Detector-free category comprises CNN Based, Transformer Based, and Patch Based methods. Our study extends beyond methodological analysis, incorporating evaluations of prevalent datasets and metrics to facilitate a quantitative comparison of state-of-the-art techniques. The paper also explores the practical application of local feature matching in diverse domains such as Structure from Motion, Remote Sensing Image Registration, and Medical Image Registration, underscoring its versatility and significance across various fields. Ultimately, we endeavor to outline the current challenges faced in this domain and furnish future research directions, thereby serving as a reference for researchers involved in local feature matching and its interconnected domains.  
  </ol>  
</details>  
  
  



## NeRF  

### [CARFF: Conditional Auto-encoded Radiance Field for 3D Scene Forecasting](http://arxiv.org/abs/2401.18075)  
Jiezhi Yang, Khushi Desai, Charles Packer, Harshil Bhatia, Nicholas Rhinehart, Rowan McAllister, Joseph Gonzalez  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We propose CARFF: Conditional Auto-encoded Radiance Field for 3D Scene Forecasting, a method for predicting future 3D scenes given past observations, such as 2D ego-centric images. Our method maps an image to a distribution over plausible 3D latent scene configurations using a probabilistic encoder, and predicts the evolution of the hypothesized scenes through time. Our latent scene representation conditions a global Neural Radiance Field (NeRF) to represent a 3D scene model, which enables explainable predictions and straightforward downstream applications. This approach extends beyond previous neural rendering work by considering complex scenarios of uncertainty in environmental states and dynamics. We employ a two-stage training of Pose-Conditional-VAE and NeRF to learn 3D representations. Additionally, we auto-regressively predict latent scene representations as a partially observable Markov decision process, utilizing a mixture density network. We demonstrate the utility of our method in realistic scenarios using the CARLA driving simulator, where CARFF can be used to enable efficient trajectory and contingency planning in complex multi-agent autonomous driving scenarios involving visual occlusions.  
  </ol>  
</details>  
  
### [Semantic Anything in 3D Gaussians](http://arxiv.org/abs/2401.17857)  
Xu Hu, Yuxi Wang, Lue Fan, Junsong Fan, Junran Peng, Zhen Lei, Qing Li, Zhaoxiang Zhang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    3D Gaussian Splatting has emerged as an alternative 3D representation of Neural Radiance Fields (NeRFs), benefiting from its high-quality rendering results and real-time rendering speed. Considering the 3D Gaussian representation remains unparsed, it is necessary first to execute object segmentation within this domain. Subsequently, scene editing and collision detection can be performed, proving vital to a multitude of applications, such as virtual reality (VR), augmented reality (AR), game/movie production, etc. In this paper, we propose a novel approach to achieve object segmentation in 3D Gaussian via an interactive procedure without any training process and learned parameters. We refer to the proposed method as SA-GS, for Segment Anything in 3D Gaussians. Given a set of clicked points in a single input view, SA-GS can generalize SAM to achieve 3D consistent segmentation via the proposed multi-view mask generation and view-wise label assignment methods. We also propose a cross-view label-voting approach to assign labels from different views. In addition, in order to address the boundary roughness issue of segmented objects resulting from the non-negligible spatial sizes of 3D Gaussian located at the boundary, SA-GS incorporates the simple but effective Gaussian Decomposition scheme. Extensive experiments demonstrate that SA-GS achieves high-quality 3D segmentation results, which can also be easily applied for scene editing and collision detection tasks. Codes will be released soon.  
  </ol>  
</details>  
  
  



