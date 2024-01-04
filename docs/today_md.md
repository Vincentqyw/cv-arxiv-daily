<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#slam>SLAM</a></li>
      <ul>
        <li><a href=#LEAP-VO:-Long-term-Effective-Any-Point-Tracking-for-Visual-Odometry>LEAP-VO: Long-term Effective Any Point Tracking for Visual Odometry</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#DDN-SLAM:-Real-time-Dense-Dynamic-Neural-Implicit-SLAM-with-Joint-Semantic-Encoding>DDN-SLAM: Real-time Dense Dynamic Neural Implicit SLAM with Joint Semantic Encoding</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#Local-Adaptive-Clustering-Based-Image-Matching-for-Automatic-Visual-Identification>Local Adaptive Clustering Based Image Matching for Automatic Visual Identification</a></li>
        <li><a href=#A-Transformer-Based-Adaptive-Semantic-Aggregation-Method-for-UAV-Visual-Geo-Localization>A Transformer-Based Adaptive Semantic Aggregation Method for UAV Visual Geo-Localization</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#SIGNeRF:-Scene-Integrated-Generation-for-Neural-Radiance-Fields>SIGNeRF: Scene Integrated Generation for Neural Radiance Fields</a></li>
      </ul>
    </li>
  </ol>
</details>

## SLAM  

### [LEAP-VO: Long-term Effective Any Point Tracking for Visual Odometry](http://arxiv.org/abs/2401.01887)  
Weirong Chen, Le Chen, Rui Wang, Marc Pollefeys  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Visual odometry estimates the motion of a moving camera based on visual input. Existing methods, mostly focusing on two-view point tracking, often ignore the rich temporal context in the image sequence, thereby overlooking the global motion patterns and providing no assessment of the full trajectory reliability. These shortcomings hinder performance in scenarios with occlusion, dynamic objects, and low-texture areas. To address these challenges, we present the Long-term Effective Any Point Tracking (LEAP) module. LEAP innovatively combines visual, inter-track, and temporal cues with mindfully selected anchors for dynamic track estimation. Moreover, LEAP's temporal probabilistic formulation integrates distribution updates into a learnable iterative refinement module to reason about point-wise uncertainty. Based on these traits, we develop LEAP-VO, a robust visual odometry system adept at handling occlusions and dynamic scenes. Our mindful integration showcases a novel practice by employing long-term point tracking as the front-end. Extensive experiments demonstrate that the proposed pipeline significantly outperforms existing baselines across various visual odometry benchmarks.  
  </ol>  
</details>  
**comments**: 15 pages, 11 figures  
  
  



## Visual Localization  

### [DDN-SLAM: Real-time Dense Dynamic Neural Implicit SLAM with Joint Semantic Encoding](http://arxiv.org/abs/2401.01545)  
Mingrui Li, Jiaming He, Guangan Jiang, Hongyu Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We propose DDN-SLAM, a real-time dense neural implicit semantic SLAM system designed for dynamic scenes. While existing neural implicit SLAM systems perform well in static scenes, they often encounter challenges in real-world environments with dynamic interferences, leading to ineffective tracking and mapping. DDN-SLAM utilizes the priors provided by the deep semantic system, combined with conditional probability fields, for segmentation.By constructing depth-guided static masks and employing joint multi-resolution hashing encoding, we ensure fast hole filling and high-quality mapping while mitigating the effects of dynamic information interference. To enhance tracking robustness, we utilize sparse feature points validated with optical flow and keyframes, enabling loop closure detection and global bundle optimization. Furthermore, DDN-SLAM supports monocular, stereo, and RGB-D inputs, operating robustly at a frequency of 20-30Hz. Extensive experiments on 6 virtual/real datasets demonstrate that our method outperforms state-of-the-art approaches in both dynamic and static scenes.  
  </ol>  
</details>  
**comments**: 11pages, 4figures  
  
  



## Image Matching  

### [Local Adaptive Clustering Based Image Matching for Automatic Visual Identification](http://arxiv.org/abs/2401.01720)  
Zhizhen Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Monitoring cameras are extensively utilized in industrial production to monitor equipment running. With advancements in computer vision, device recognition using image features is viable. This paper presents a vision-assisted identification system that implements real-time automatic equipment labeling through image matching in surveillance videos. The system deploys the ORB algorithm to extract image features and the GMS algorithm to remove incorrect matching points. According to the principles of clustering and template locality, a method known as Local Adaptive Clustering (LAC) has been established to enhance label positioning. This method segments matching templates using the cluster center, which improves the efficiency and stability of labels. The experimental results demonstrate that LAC effectively curtails the label drift.  
  </ol>  
</details>  
  
### [A Transformer-Based Adaptive Semantic Aggregation Method for UAV Visual Geo-Localization](http://arxiv.org/abs/2401.01574)  
Shishen Li, Cuiwei Liu, Huaijun Qiu, Zhaokui Li  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper addresses the task of Unmanned Aerial Vehicles (UAV) visual geo-localization, which aims to match images of the same geographic target taken by different platforms, i.e., UAVs and satellites. In general, the key to achieving accurate UAV-satellite image matching lies in extracting visual features that are robust against viewpoint changes, scale variations, and rotations. Current works have shown that part matching is crucial for UAV visual geo-localization since part-level representations can capture image details and help to understand the semantic information of scenes. However, the importance of preserving semantic characteristics in part-level representations is not well discussed. In this paper, we introduce a transformer-based adaptive semantic aggregation method that regards parts as the most representative semantics in an image. Correlations of image patches to different parts are learned in terms of the transformer's feature map. Then our method decomposes part-level features into an adaptive sum of all patch features. By doing this, the learned parts are encouraged to focus on patches with typical semantics. Extensive experiments on the University-1652 dataset have shown the superiority of our method over the current works.  
  </ol>  
</details>  
**comments**: 12 pages  
  
  



## NeRF  

### [SIGNeRF: Scene Integrated Generation for Neural Radiance Fields](http://arxiv.org/abs/2401.01647)  
Jan-Niklas Dihlmann, Andreas Engelhardt, Hendrik Lensch  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Advances in image diffusion models have recently led to notable improvements in the generation of high-quality images. In combination with Neural Radiance Fields (NeRFs), they enabled new opportunities in 3D generation. However, most generative 3D approaches are object-centric and applying them to editing existing photorealistic scenes is not trivial. We propose SIGNeRF, a novel approach for fast and controllable NeRF scene editing and scene-integrated object generation. A new generative update strategy ensures 3D consistency across the edited images, without requiring iterative optimization. We find that depth-conditioned diffusion models inherently possess the capability to generate 3D consistent views by requesting a grid of images instead of single views. Based on these insights, we introduce a multi-view reference sheet of modified images. Our method updates an image collection consistently based on the reference sheet and refines the original NeRF with the newly generated image set in one go. By exploiting the depth conditioning mechanism of the image diffusion model, we gain fine control over the spatial location of the edit and enforce shape guidance by a selected region or an external mesh.  
  </ol>  
</details>  
**comments**: Project Page: https://signerf.jdihlmann.com  
  
  



