<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#BonnBeetClouds3D:-A-Dataset-Towards-Point-Cloud-based-Organ-level-Phenotyping-of-Sugar-Beet-Plants-under-Field-Conditions>BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#Harnessing-Diffusion-Models-for-Visual-Perception-with-Meta-Prompts>Harnessing Diffusion Models for Visual Perception with Meta Prompts</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#PoseGen:-Learning-to-Generate-3D-Human-Pose-Dataset-with-NeRF>PoseGen: Learning to Generate 3D Human Pose Dataset with NeRF</a></li>
        <li><a href=#Density-Uncertainty-Quantification-with-NeRF-Ensembles:-Impact-of-Data-and-Scene-Constraints>Density Uncertainty Quantification with NeRF-Ensembles: Impact of Data and Scene Constraints</a></li>
        <li><a href=#PlatoNeRF:-3D-Reconstruction-in-Plato's-Cave-via-Single-View-Two-Bounce-Lidar>PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar</a></li>
      </ul>
    </li>
  </ol>
</details>

## Keypoint Detection  

### [BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions](http://arxiv.org/abs/2312.14706)  
Elias Marks, Jonas Bömer, Federico Magistri, Anurag Sah, Jens Behley, Cyrill Stachniss  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Agricultural production is facing severe challenges in the next decades induced by climate change and the need for sustainability, reducing its impact on the environment. Advancements in field management through non-chemical weeding by robots in combination with monitoring of crops by autonomous unmanned aerial vehicles (UAVs) and breeding of novel and more resilient crop varieties are helpful to address these challenges. The analysis of plant traits, called phenotyping, is an essential activity in plant breeding, it however involves a great amount of manual labor. With this paper, we address the problem of automatic fine-grained organ-level geometric analysis needed for precision phenotyping. As the availability of real-world data in this domain is relatively scarce, we propose a novel dataset that was acquired using UAVs capturing high-resolution images of a real breeding trial containing 48 plant varieties and therefore covering great morphological and appearance diversity. This enables the development of approaches for autonomous phenotyping that generalize well to different varieties. Based on overlapping high-resolution images from multiple viewing angles, we compute photogrammetric dense point clouds and provide detailed and accurate point-wise labels for plants, leaves, and salient points as the tip and the base. Additionally, we include measurements of phenotypic traits performed by experts from the German Federal Plant Variety Office on the real plants, allowing the evaluation of new approaches not only on segmentation and keypoint detection but also directly on the downstream tasks. The provided labeled point clouds enable fine-grained plant analysis and support further progress in the development of automatic phenotyping approaches, but also enable further research in surface reconstruction, point cloud completion, and semantic interpretation of point clouds.  
  </ol>  
</details>  
  
  



## Image Matching  

### [Harnessing Diffusion Models for Visual Perception with Meta Prompts](http://arxiv.org/abs/2312.14733)  
[[code](https://github.com/fudan-zvg/meta-prompts)]  
Qiang Wan, Zilong Huang, Bingyi Kang, Jiashi Feng, Li Zhang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The issue of generative pretraining for vision models has persisted as a long-standing conundrum. At present, the text-to-image (T2I) diffusion model demonstrates remarkable proficiency in generating high-definition images matching textual inputs, a feat made possible through its pre-training on large-scale image-text pairs. This leads to a natural inquiry: can diffusion models be utilized to tackle visual perception tasks? In this paper, we propose a simple yet effective scheme to harness a diffusion model for visual perception tasks. Our key insight is to introduce learnable embeddings (meta prompts) to the pre-trained diffusion models to extract proper features for perception. The effect of meta prompts are two-fold. First, as a direct replacement of the text embeddings in the T2I models, it can activate task-relevant features during feature extraction. Second, it will be used to re-arrange the extracted features to ensures that the model focuses on the most pertinent features for the task on hand. Additionally, we design a recurrent refinement training strategy that fully leverages the property of diffusion models, thereby yielding stronger visual features. Extensive experiments across various benchmarks validate the effectiveness of our approach. Our approach achieves new performance records in depth estimation tasks on NYU depth V2 and KITTI, and in semantic segmentation task on CityScapes. Concurrently, the proposed method attains results comparable to the current state-of-the-art in semantic segmentation on ADE20K and pose estimation on COCO datasets, further exemplifying its robustness and versatility.  
  </ol>  
</details>  
  
  



## NeRF  

### [PoseGen: Learning to Generate 3D Human Pose Dataset with NeRF](http://arxiv.org/abs/2312.14915)  
Mohsen Gholami, Rabab Ward, Z. Jane Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper proposes an end-to-end framework for generating 3D human pose datasets using Neural Radiance Fields (NeRF). Public datasets generally have limited diversity in terms of human poses and camera viewpoints, largely due to the resource-intensive nature of collecting 3D human pose data. As a result, pose estimators trained on public datasets significantly underperform when applied to unseen out-of-distribution samples. Previous works proposed augmenting public datasets by generating 2D-3D pose pairs or rendering a large amount of random data. Such approaches either overlook image rendering or result in suboptimal datasets for pre-trained models. Here we propose PoseGen, which learns to generate a dataset (human 3D poses and images) with a feedback loss from a given pre-trained pose estimator. In contrast to prior art, our generated data is optimized to improve the robustness of the pre-trained model. The objective of PoseGen is to learn a distribution of data that maximizes the prediction error of a given pre-trained model. As the learned data distribution contains OOD samples of the pre-trained model, sampling data from such a distribution for further fine-tuning a pre-trained model improves the generalizability of the model. This is the first work that proposes NeRFs for 3D human data generation. NeRFs are data-driven and do not require 3D scans of humans. Therefore, using NeRF for data generation is a new direction for convenient user-specific data generation. Our extensive experiments show that the proposed PoseGen improves two baseline models (SPIN and HybrIK) on four datasets with an average 6% relative improvement.  
  </ol>  
</details>  
  
### [Density Uncertainty Quantification with NeRF-Ensembles: Impact of Data and Scene Constraints](http://arxiv.org/abs/2312.14664)  
Miriam Jäger, Steven Landgraf, Boris Jutzi  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    In the fields of computer graphics, computer vision and photogrammetry, Neural Radiance Fields (NeRFs) are a major topic driving current research and development. However, the quality of NeRF-generated 3D scene reconstructions and subsequent surface reconstructions, heavily relies on the network output, particularly the density. Regarding this critical aspect, we propose to utilize NeRF-Ensembles that provide a density uncertainty estimate alongside the mean density. We demonstrate that data constraints such as low-quality images and poses lead to a degradation of the training process, increased density uncertainty and decreased predicted density. Even with high-quality input data, the density uncertainty varies based on scene constraints such as acquisition constellations, occlusions and material properties. NeRF-Ensembles not only provide a tool for quantifying the uncertainty but exhibit two promising advantages: Enhanced robustness and artifact removal. Through the utilization of NeRF-Ensembles instead of single NeRFs, small outliers are removed, yielding a smoother output with improved completeness of structures. Furthermore, applying percentile-based thresholds on density uncertainty outliers proves to be effective for the removal of large (foggy) artifacts in post-processing. We conduct our methodology on 3 different datasets: (i) synthetic benchmark dataset, (ii) real benchmark dataset, (iii) real data under realistic recording conditions and sensors.  
  </ol>  
</details>  
**comments**: 21 pages, 12 figures, 5 tables  
  
### [PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar](http://arxiv.org/abs/2312.14239)  
Tzofi Klinghoffer, Xiaoyu Xiang, Siddharth Somasundaram, Yuchen Fan, Christian Richardt, Ramesh Raskar, Rakesh Ranjan  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    3D reconstruction from a single-view is challenging because of the ambiguity from monocular cues and lack of information about occluded regions. Neural radiance fields (NeRF), while popular for view synthesis and 3D reconstruction, are typically reliant on multi-view images. Existing methods for single-view 3D reconstruction with NeRF rely on either data priors to hallucinate views of occluded regions, which may not be physically accurate, or shadows observed by RGB cameras, which are difficult to detect in ambient light and low albedo backgrounds. We propose using time-of-flight data captured by a single-photon avalanche diode to overcome these limitations. Our method models two-bounce optical paths with NeRF, using lidar transient data for supervision. By leveraging the advantages of both NeRF and two-bounce light measured by lidar, we demonstrate that we can reconstruct visible and occluded geometry without data priors or reliance on controlled ambient lighting or scene albedo. In addition, we demonstrate improved generalization under practical constraints on sensor spatial- and temporal-resolution. We believe our method is a promising direction as single-photon lidars become ubiquitous on consumer devices, such as phones, tablets, and headsets.  
  </ol>  
</details>  
**comments**: Project Page: https://platonerf.github.io/  
  
  



