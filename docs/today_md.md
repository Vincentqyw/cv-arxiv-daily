<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#Keypoint-based-Stereophotoclinometry-for-Characterizing-and-Navigating-Small-Bodies:-A-Factor-Graph-Approach>Keypoint-based Stereophotoclinometry for Characterizing and Navigating Small Bodies: A Factor Graph Approach</a></li>
        <li><a href=#Gaussian-Splatting-SLAM>Gaussian Splatting SLAM</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Collapse-Oriented-Adversarial-Training-with-Triplet-Decoupling-for-Robust-Image-Retrieval>Collapse-Oriented Adversarial Training with Triplet Decoupling for Robust Image Retrieval</a></li>
        <li><a href=#Attacking-the-Loop:-Adversarial-Attacks-on-Graph-based-Loop-Closure-Detection>Attacking the Loop: Adversarial Attacks on Graph-based Loop Closure Detection</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#Keypoint-based-Stereophotoclinometry-for-Characterizing-and-Navigating-Small-Bodies:-A-Factor-Graph-Approach>Keypoint-based Stereophotoclinometry for Characterizing and Navigating Small Bodies: A Factor Graph Approach</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#COLMAP-Free-3D-Gaussian-Splatting>COLMAP-Free 3D Gaussian Splatting</a></li>
        <li><a href=#Unifying-Correspondence,-Pose-and-NeRF-for-Pose-Free-Novel-View-Synthesis-from-Stereo-Pairs>Unifying Correspondence, Pose and NeRF for Pose-Free Novel View Synthesis from Stereo Pairs</a></li>
        <li><a href=#WaterHE-NeRF:-Water-ray-Tracing-Neural-Radiance-Fields-for-Underwater-Scene-Reconstruction>WaterHE-NeRF: Water-ray Tracing Neural Radiance Fields for Underwater Scene Reconstruction</a></li>
        <li><a href=#TeTriRF:-Temporal-Tri-Plane-Radiance-Fields-for-Efficient-Free-Viewpoint-Video>TeTriRF: Temporal Tri-Plane Radiance Fields for Efficient Free-Viewpoint Video</a></li>
      </ul>
    </li>
  </ol>
</details>

## SFM  

### [Keypoint-based Stereophotoclinometry for Characterizing and Navigating Small Bodies: A Factor Graph Approach](http://arxiv.org/abs/2312.06865)  
Travis Driver, Andrew Vaughan, Yang Cheng, Adnan Ansar, John Christian, Panagiotis Tsiotras  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper proposes the incorporation of techniques from stereophotoclinometry (SPC) into a keypoint-based structure-from-motion (SfM) system to estimate the surface normal and albedo at detected landmarks to improve autonomous surface and shape characterization of small celestial bodies from in-situ imagery. In contrast to the current state-of-the-practice method for small body shape reconstruction, i.e., SPC, which relies on human-in-the-loop verification and high-fidelity a priori information to achieve accurate results, we forego the expensive maplet estimation step and instead leverage dense keypoint measurements and correspondences from an autonomous keypoint detection and matching method based on deep learning to provide the necessary photogrammetric constraints. Moreover, we develop a factor graph-based approach allowing for simultaneous optimization of the spacecraft's pose, landmark positions, Sun-relative direction, and surface normals and albedos via fusion of Sun sensor measurements and image keypoint measurements. The proposed framework is validated on real imagery of the Cornelia crater on Asteroid 4 Vesta, along with pose estimation and mapping comparison against an SPC reconstruction, where we demonstrate precise alignment to the SPC solution without relying on any a priori camera pose and topography information or humans-in-the-loop  
  </ol>  
</details>  
  
### [Gaussian Splatting SLAM](http://arxiv.org/abs/2312.06741)  
Hidenobu Matsuki, Riku Murai, Paul H. J. Kelly, Andrew J. Davison  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We present the first application of 3D Gaussian Splatting to incremental 3D reconstruction using a single moving monocular or RGB-D camera. Our Simultaneous Localisation and Mapping (SLAM) method, which runs live at 3fps, utilises Gaussians as the only 3D representation, unifying the required representation for accurate, efficient tracking, mapping, and high-quality rendering. Several innovations are required to continuously reconstruct 3D scenes with high fidelity from a live camera. First, to move beyond the original 3DGS algorithm, which requires accurate poses from an offline Structure from Motion (SfM) system, we formulate camera tracking for 3DGS using direct optimisation against the 3D Gaussians, and show that this enables fast and robust tracking with a wide basin of convergence. Second, by utilising the explicit nature of the Gaussians, we introduce geometric verification and regularisation to handle the ambiguities occurring in incremental 3D dense reconstruction. Finally, we introduce a full SLAM system which not only achieves state-of-the-art results in novel view synthesis and trajectory estimation, but also reconstruction of tiny and even transparent objects.  
  </ol>  
</details>  
**comments**: First two authors contributed equally to this work. Project Page:
  https://rmurai.co.uk/projects/GaussianSplattingSLAM/ Video:
  https://www.youtube.com/watch?v=x604ghp9R_Q&ab_channel=DysonRoboticsLaboratoryatImperialCollege  
  
  



## Visual Localization  

### [Collapse-Oriented Adversarial Training with Triplet Decoupling for Robust Image Retrieval](http://arxiv.org/abs/2312.07364)  
Qiwei Tian, Chenhao Lin, Qian Li, Zhengyu Zhao, Chao Shen  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Adversarial training has achieved substantial performance in defending image retrieval systems against adversarial examples. However, existing studies still suffer from two major limitations: model collapse and weak adversary. This paper addresses these two limitations by proposing collapse-oriented (COLO) adversarial training with triplet decoupling (TRIDE). Specifically, COLO prevents model collapse by temporally orienting the perturbation update direction with a new collapse metric, while TRIDE yields a strong adversary by spatially decoupling the update targets of perturbation into the anchor and the two candidates of a triplet. Experimental results demonstrate that our COLO-TRIDE outperforms the current state of the art by 7% on average over 10 robustness metrics and across 3 popular datasets. In addition, we identify the fairness limitations of commonly used robustness metrics in image retrieval and propose a new metric for more meaningful robustness evaluation. Codes will be made publicly available on GitHub.  
  </ol>  
</details>  
  
### [Attacking the Loop: Adversarial Attacks on Graph-based Loop Closure Detection](http://arxiv.org/abs/2312.06991)  
Jonathan J. Y. Kim, Martin Urschler, Patricia J. Riddle, Jorg S. Wicker  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    With the advancement in robotics, it is becoming increasingly common for large factories and warehouses to incorporate visual SLAM (vSLAM) enabled automated robots that operate closely next to humans. This makes any adversarial attacks on vSLAM components potentially detrimental to humans working alongside them. Loop Closure Detection (LCD) is a crucial component in vSLAM that minimizes the accumulation of drift in mapping, since even a small drift can accumulate into a significant drift over time. A prior work by Kim et al., SymbioLCD2, unified visual features and semantic objects into a single graph structure for finding loop closure candidates. While this provided a performance improvement over visual feature-based LCD, it also created a single point of vulnerability for potential graph-based adversarial attacks. Unlike previously reported visual-patch based attacks, small graph perturbations are far more challenging to detect, making them a more significant threat. In this paper, we present Adversarial-LCD, a novel black-box evasion attack framework that employs an eigencentrality-based perturbation method and an SVM-RBF surrogate model with a Weisfeiler-Lehman feature extractor for attacking graph-based LCD. Our evaluation shows that the attack performance of Adversarial-LCD with the SVM-RBF surrogate model was superior to that of other machine learning surrogate algorithms, including SVM-linear, SVM-polynomial, and Bayesian classifier, demonstrating the effectiveness of our attack framework. Furthermore, we show that our eigencentrality-based perturbation method outperforms other algorithms, such as Random-walk and Shortest-path, highlighting the efficiency of Adversarial-LCD's perturbation selection method.  
  </ol>  
</details>  
**comments**: Accepted at VISIGRAPP 2024, 8 pages  
  
  



## Keypoint Detection  

### [Keypoint-based Stereophotoclinometry for Characterizing and Navigating Small Bodies: A Factor Graph Approach](http://arxiv.org/abs/2312.06865)  
Travis Driver, Andrew Vaughan, Yang Cheng, Adnan Ansar, John Christian, Panagiotis Tsiotras  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper proposes the incorporation of techniques from stereophotoclinometry (SPC) into a keypoint-based structure-from-motion (SfM) system to estimate the surface normal and albedo at detected landmarks to improve autonomous surface and shape characterization of small celestial bodies from in-situ imagery. In contrast to the current state-of-the-practice method for small body shape reconstruction, i.e., SPC, which relies on human-in-the-loop verification and high-fidelity a priori information to achieve accurate results, we forego the expensive maplet estimation step and instead leverage dense keypoint measurements and correspondences from an autonomous keypoint detection and matching method based on deep learning to provide the necessary photogrammetric constraints. Moreover, we develop a factor graph-based approach allowing for simultaneous optimization of the spacecraft's pose, landmark positions, Sun-relative direction, and surface normals and albedos via fusion of Sun sensor measurements and image keypoint measurements. The proposed framework is validated on real imagery of the Cornelia crater on Asteroid 4 Vesta, along with pose estimation and mapping comparison against an SPC reconstruction, where we demonstrate precise alignment to the SPC solution without relying on any a priori camera pose and topography information or humans-in-the-loop  
  </ol>  
</details>  
  
  



## NeRF  

### [COLMAP-Free 3D Gaussian Splatting](http://arxiv.org/abs/2312.07504)  
Yang Fu, Sifei Liu, Amey Kulkarni, Jan Kautz, Alexei A. Efros, Xiaolong Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    While neural rendering has led to impressive advances in scene reconstruction and novel view synthesis, it relies heavily on accurately pre-computed camera poses. To relax this constraint, multiple efforts have been made to train Neural Radiance Fields (NeRFs) without pre-processed camera poses. However, the implicit representations of NeRFs provide extra challenges to optimize the 3D structure and camera poses at the same time. On the other hand, the recently proposed 3D Gaussian Splatting provides new opportunities given its explicit point cloud representations. This paper leverages both the explicit geometric representation and the continuity of the input video stream to perform novel view synthesis without any SfM preprocessing. We process the input frames in a sequential manner and progressively grow the 3D Gaussians set by taking one input frame at a time, without the need to pre-compute the camera poses. Our method significantly improves over previous approaches in view synthesis and camera pose estimation under large motion changes. Our project page is https://oasisyang.github.io/colmap-free-3dgs  
  </ol>  
</details>  
**comments**: Project Page: https://oasisyang.github.io/colmap-free-3dgs  
  
### [Unifying Correspondence, Pose and NeRF for Pose-Free Novel View Synthesis from Stereo Pairs](http://arxiv.org/abs/2312.07246)  
Sunghwan Hong, Jaewoo Jung, Heeseong Shin, Jiaolong Yang, Seungryong Kim, Chong Luo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This work delves into the task of pose-free novel view synthesis from stereo pairs, a challenging and pioneering task in 3D vision. Our innovative framework, unlike any before, seamlessly integrates 2D correspondence matching, camera pose estimation, and NeRF rendering, fostering a synergistic enhancement of these tasks. We achieve this through designing an architecture that utilizes a shared representation, which serves as a foundation for enhanced 3D geometry understanding. Capitalizing on the inherent interplay between the tasks, our unified framework is trained end-to-end with the proposed training strategy to improve overall model accuracy. Through extensive evaluations across diverse indoor and outdoor scenes from two real-world datasets, we demonstrate that our approach achieves substantial improvement over previous methodologies, especially in scenarios characterized by extreme viewpoint changes and the absence of accurate camera poses.  
  </ol>  
</details>  
**comments**: Project page: https://ku-cvlab.github.io/CoPoNeRF/  
  
### [WaterHE-NeRF: Water-ray Tracing Neural Radiance Fields for Underwater Scene Reconstruction](http://arxiv.org/abs/2312.06946)  
Jingchun Zhou, Tianyu Liang, Zongxin He, Dehuan Zhang, Weishi Zhang, Xianping Fu, Chongyi Li  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Field (NeRF) technology demonstrates immense potential in novel viewpoint synthesis tasks, due to its physics-based volumetric rendering process, which is particularly promising in underwater scenes. Addressing the limitations of existing underwater NeRF methods in handling light attenuation caused by the water medium and the lack of real Ground Truth (GT) supervision, this study proposes WaterHE-NeRF. We develop a new water-ray tracing field by Retinex theory that precisely encodes color, density, and illuminance attenuation in three-dimensional space. WaterHE-NeRF, through its illuminance attenuation mechanism, generates both degraded and clear multi-view images and optimizes image restoration by combining reconstruction loss with Wasserstein distance. Additionally, the use of histogram equalization (HE) as pseudo-GT enhances the network's accuracy in preserving original details and color distribution. Extensive experiments on real underwater datasets and synthetic datasets validate the effectiveness of WaterHE-NeRF. Our code will be made publicly available.  
  </ol>  
</details>  
  
### [TeTriRF: Temporal Tri-Plane Radiance Fields for Efficient Free-Viewpoint Video](http://arxiv.org/abs/2312.06713)  
Minye Wu, Zehao Wang, Georgios Kouros, Tinne Tuytelaars  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Fields (NeRF) revolutionize the realm of visual media by providing photorealistic Free-Viewpoint Video (FVV) experiences, offering viewers unparalleled immersion and interactivity. However, the technology's significant storage requirements and the computational complexity involved in generation and rendering currently limit its broader application. To close this gap, this paper presents Temporal Tri-Plane Radiance Fields (TeTriRF), a novel technology that significantly reduces the storage size for Free-Viewpoint Video (FVV) while maintaining low-cost generation and rendering. TeTriRF introduces a hybrid representation with tri-planes and voxel grids to support scaling up to long-duration sequences and scenes with complex motions or rapid changes. We propose a group training scheme tailored to achieving high training efficiency and yielding temporally consistent, low-entropy scene representations. Leveraging these properties of the representations, we introduce a compression pipeline with off-the-shelf video codecs, achieving an order of magnitude less storage size compared to the state-of-the-art. Our experiments demonstrate that TeTriRF can achieve competitive quality with a higher compression rate.  
  </ol>  
</details>  
**comments**: 13 pages, 11 figures  
  
  



