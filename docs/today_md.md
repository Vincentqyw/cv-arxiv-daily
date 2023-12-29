<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#slam>SLAM</a></li>
      <ul>
        <li><a href=#SR-LIVO:-LiDAR-Inertial-Visual-Odometry-and-Mapping-with-Sweep-Reconstruction>SR-LIVO: LiDAR-Inertial-Visual Odometry and Mapping with Sweep Reconstruction</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#LIP-Loc:-LiDAR-Image-Pretraining-for-Cross-Modal-Localization>LIP-Loc: LiDAR Image Pretraining for Cross-Modal Localization</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#Bezier-based-Regression-Feature-Descriptor-for-Deformable-Linear-Objects>Bezier-based Regression Feature Descriptor for Deformable Linear Objects</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#City-on-Web:-Real-time-Neural-Rendering-of-Large-scale-Scenes-on-the-Web>City-on-Web: Real-time Neural Rendering of Large-scale Scenes on the Web</a></li>
        <li><a href=#DL3DV-10K:-A-Large-Scale-Scene-Dataset-for-Deep-Learning-based-3D-Vision>DL3DV-10K: A Large-Scale Scene Dataset for Deep Learning-based 3D Vision</a></li>
        <li><a href=#SUNDIAL:-3D-Satellite-Understanding-through-Direct,-Ambient,-and-Complex-Lighting-Decomposition>SUNDIAL: 3D Satellite Understanding through Direct, Ambient, and Complex Lighting Decomposition</a></li>
        <li><a href=#INFAMOUS-NeRF:-ImproviNg-FAce-MOdeling-Using-Semantically-Aligned-Hypernetworks-with-Neural-Radiance-Fields>INFAMOUS-NeRF: ImproviNg FAce MOdeling Using Semantically-Aligned Hypernetworks with Neural Radiance Fields</a></li>
      </ul>
    </li>
  </ol>
</details>

## SLAM  

### [SR-LIVO: LiDAR-Inertial-Visual Odometry and Mapping with Sweep Reconstruction](http://arxiv.org/abs/2312.16800)  
Zikang Yuan, Jie Deng, Ruiye Ming, Fengtian Lang, Xin Yang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Existing LiDAR-inertial-visual odometry and mapping (LIV-SLAM) systems mainly utilize the LiDAR-inertial odometry (LIO) module for structure reconstruction and the visual-inertial odometry (VIO) module for color rendering. However, the accuracy of VIO is often compromised by photometric changes, weak textures and motion blur, unlike the more robust LIO. This paper introduces SR-LIVO, an advanced and novel LIV-SLAM system employing sweep reconstruction to align reconstructed sweeps with image timestamps. This allows the LIO module to accurately determine states at all imaging moments, enhancing pose accuracy and processing efficiency. Experimental results on two public datasets demonstrate that: 1) our SRLIVO outperforms existing state-of-the-art LIV-SLAM systems in both pose accuracy and time efficiency; 2) our LIO-based pose estimation prove more accurate than VIO-based ones in several mainstream LIV-SLAM systems (including ours). We have released our source code to contribute to the community development in this field.  
  </ol>  
</details>  
**comments**: 7 pages, 6 figures, submitted to IEEE RA-L  
  
  



## Visual Localization  

### [LIP-Loc: LiDAR Image Pretraining for Cross-Modal Localization](http://arxiv.org/abs/2312.16648)  
Sai Shubodh Puligilla, Mohammad Omama, Husain Zaidi, Udit Singh Parihar, Madhava Krishna  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Global visual localization in LiDAR-maps, crucial for autonomous driving applications, remains largely unexplored due to the challenging issue of bridging the cross-modal heterogeneity gap. Popular multi-modal learning approach Contrastive Language-Image Pre-Training (CLIP) has popularized contrastive symmetric loss using batch construction technique by applying it to multi-modal domains of text and image. We apply this approach to the domains of 2D image and 3D LiDAR points on the task of cross-modal localization. Our method is explained as follows: A batch of N (image, LiDAR) pairs is constructed so as to predict what is the right match between N X N possible pairings across the batch by jointly training an image encoder and LiDAR encoder to learn a multi-modal embedding space. In this way, the cosine similarity between N positive pairings is maximized, whereas that between the remaining negative pairings is minimized. Finally, over the obtained similarity scores, a symmetric cross-entropy loss is optimized. To the best of our knowledge, this is the first work to apply batched loss approach to a cross-modal setting of image & LiDAR data and also to show Zero-shot transfer in a visual localization setting. We conduct extensive analyses on standard autonomous driving datasets such as KITTI and KITTI-360 datasets. Our method outperforms state-of-the-art recall@1 accuracy on the KITTI-360 dataset by 22.4%, using only perspective images, in contrast to the state-of-the-art approach, which utilizes the more informative fisheye images. Additionally, this superior performance is achieved without resorting to complex architectures. Moreover, we demonstrate the zero-shot capabilities of our model and we beat SOTA by 8% without even training on it. Furthermore, we establish the first benchmark for cross-modal localization on the KITTI dataset.  
  </ol>  
</details>  
**comments**: To be presented at WACV-W 2024. Project page:
  https://shubodhs.ai/liploc  
  
  



## Keypoint Detection  

### [Bezier-based Regression Feature Descriptor for Deformable Linear Objects](http://arxiv.org/abs/2312.16502)  
Fangqing Chen  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    In this paper, a feature extraction approach for the deformable linear object is presented, which uses a Bezier curve to represent the original geometric shape. The proposed extraction strategy is combined with a parameterization technique, the goal is to compute the regression features from the visual-feedback RGB image, and finally obtain the efficient shape feature in the low-dimensional latent space. Existing works of literature often fail to capture the complex characteristics in a unified framework. They also struggle in scenarios where only local shape descriptors are used to guide the robot to complete the manipulation. To address these challenges, we propose a feature extraction technique using a parameterization approach to generate the regression features, which leverages the power of the Bezier curve and linear regression. The proposed extraction method effectively captures topological features and node characteristics, making it well-suited for the deformation object manipulation task. Large mount of simulations are conducted to evaluate the presented method. Our results demonstrate that the proposed method outperforms existing methods in terms of prediction accuracy, robustness, and computational efficiency. Furthermore, our approach enables the extraction of meaningful insights from the predicted links, thereby contributing to a better understanding of the shape of the deformable linear objects. Overall, this work represents a significant step forward in the use of Bezier curve for shape representation.  
  </ol>  
</details>  
  
  



## NeRF  

### [City-on-Web: Real-time Neural Rendering of Large-scale Scenes on the Web](http://arxiv.org/abs/2312.16457)  
Kaiwen Song, Juyong Zhang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    NeRF has significantly advanced 3D scene reconstruction, capturing intricate details across various environments. Existing methods have successfully leveraged radiance field baking to facilitate real-time rendering of small scenes. However, when applied to large-scale scenes, these techniques encounter significant challenges, struggling to provide a seamless real-time experience due to limited resources in computation, memory, and bandwidth. In this paper, we propose City-on-Web, which represents the whole scene by partitioning it into manageable blocks, each with its own Level-of-Detail, ensuring high fidelity, efficient memory management and fast rendering. Meanwhile, we carefully design the training and inference process such that the final rendering result on web is consistent with training. Thanks to our novel representation and carefully designed training/inference process, we are the first to achieve real-time rendering of large-scale scenes in resource-constrained environments. Extensive experimental results demonstrate that our method facilitates real-time rendering of large-scale scenes on a web platform, achieving 32FPS at 1080P resolution with an RTX 3060 GPU, while simultaneously achieving a quality that closely rivals that of state-of-the-art methods. Project page: https://ustc3dv.github.io/City-on-Web/  
  </ol>  
</details>  
**comments**: Project page: https://ustc3dv.github.io/City-on-Web/  
  
### [DL3DV-10K: A Large-Scale Scene Dataset for Deep Learning-based 3D Vision](http://arxiv.org/abs/2312.16256)  
Lu Ling, Yichen Sheng, Zhi Tu, Wentian Zhao, Cheng Xin, Kun Wan, Lantao Yu, Qianyu Guo, Zixun Yu, Yawen Lu, Xuanmao Li, Xingpeng Sun, Rohan Ashok, Aniruddha Mukherjee, Hao Kang, Xiangrui Kong, Gang Hua, Tianti Zhang, Bedrich Benes, Aniket Bera  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We have witnessed significant progress in deep learning-based 3D vision, ranging from neural radiance field (NeRF) based 3D representation learning to applications in novel view synthesis (NVS). However, existing scene-level datasets for deep learning-based 3D vision, limited to either synthetic environments or a narrow selection of real-world scenes, are quite insufficient. This insufficiency not only hinders a comprehensive benchmark of existing methods but also caps what could be explored in deep learning-based 3D analysis. To address this critical gap, we present DL3DV-10K, a large-scale scene dataset, featuring 51.2 million frames from 10,510 videos captured from 65 types of point-of-interest (POI) locations, covering both bounded and unbounded scenes, with different levels of reflection, transparency, and lighting. We conducted a comprehensive benchmark of recent NVS methods on DL3DV-10K, which revealed valuable insights for future research in NVS. In addition, we have obtained encouraging results in a pilot study to learn generalizable NeRF from DL3DV-10K, which manifests the necessity of a large-scale scene-level dataset to forge a path toward a foundation model for learning 3D representation. Our DL3DV-10K dataset, benchmark results, and models will be publicly accessible at https://dl3dv-10k.github.io/DL3DV-10K/.  
  </ol>  
</details>  
  
### [SUNDIAL: 3D Satellite Understanding through Direct, Ambient, and Complex Lighting Decomposition](http://arxiv.org/abs/2312.16215)  
Nikhil Behari, Akshat Dave, Kushagra Tiwary, William Yang, Ramesh Raskar  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    3D modeling from satellite imagery is essential in areas of environmental science, urban planning, agriculture, and disaster response. However, traditional 3D modeling techniques face unique challenges in the remote sensing context, including limited multi-view baselines over extensive regions, varying direct, ambient, and complex illumination conditions, and time-varying scene changes across captures. In this work, we introduce SUNDIAL, a comprehensive approach to 3D reconstruction of satellite imagery using neural radiance fields. We jointly learn satellite scene geometry, illumination components, and sun direction in this single-model approach, and propose a secondary shadow ray casting technique to 1) improve scene geometry using oblique sun angles to render shadows, 2) enable physically-based disentanglement of scene albedo and illumination, and 3) determine the components of illumination from direct, ambient (sky), and complex sources. To achieve this, we incorporate lighting cues and geometric priors from remote sensing literature in a neural rendering approach, modeling physical properties of satellite scenes such as shadows, scattered sky illumination, and complex illumination and shading of vegetation and water. We evaluate the performance of SUNDIAL against existing NeRF-based techniques for satellite scene modeling and demonstrate improved scene and lighting disentanglement, novel view and lighting rendering, and geometry and sun direction estimation on challenging scenes with small baselines, sparse inputs, and variable illumination.  
  </ol>  
</details>  
**comments**: 8 pages, 6 figures  
  
### [INFAMOUS-NeRF: ImproviNg FAce MOdeling Using Semantically-Aligned Hypernetworks with Neural Radiance Fields](http://arxiv.org/abs/2312.16197)  
Andrew Hou, Feng Liu, Zhiyuan Ren, Michel Sarkis, Ning Bi, Yiying Tong, Xiaoming Liu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We propose INFAMOUS-NeRF, an implicit morphable face model that introduces hypernetworks to NeRF to improve the representation power in the presence of many training subjects. At the same time, INFAMOUS-NeRF resolves the classic hypernetwork tradeoff of representation power and editability by learning semantically-aligned latent spaces despite the subject-specific models, all without requiring a large pretrained model. INFAMOUS-NeRF further introduces a novel constraint to improve NeRF rendering along the face boundary. Our constraint can leverage photometric surface rendering and multi-view supervision to guide surface color prediction and improve rendering near the surface. Finally, we introduce a novel, loss-guided adaptive sampling method for more effective NeRF training by reducing the sampling redundancy. We show quantitatively and qualitatively that our method achieves higher representation power than prior face modeling methods in both controlled and in-the-wild settings. Code and models will be released upon publication.  
  </ol>  
</details>  
  
  



