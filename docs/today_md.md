<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#Residual-Learning-for-Image-Point-Descriptors>Residual Learning for Image Point Descriptors</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Recursive-Distillation-for-Open-Set-Distributed-Robot-Localization>Recursive Distillation for Open-Set Distributed Robot Localization</a></li>
        <li><a href=#Residual-Learning-for-Image-Point-Descriptors>Residual Learning for Image Point Descriptors</a></li>
        <li><a href=#CaLDiff:-Camera-Localization-in-NeRF-via-Pose-Diffusion>CaLDiff: Camera Localization in NeRF via Pose Diffusion</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#Residual-Learning-for-Image-Point-Descriptors>Residual Learning for Image Point Descriptors</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#BEV-CV:-Birds-Eye-View-Transform-for-Cross-View-Geo-Localisation>BEV-CV: Birds-Eye-View Transform for Cross-View Geo-Localisation</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#LangSplat:-3D-Language-Gaussian-Splatting>LangSplat: 3D Language Gaussian Splatting</a></li>
        <li><a href=#2D-Guided-3D-Gaussian-Segmentation>2D-Guided 3D Gaussian Segmentation</a></li>
        <li><a href=#Pano-NeRF:-Synthesizing-High-Dynamic-Range-Novel-Views-with-Geometry-from-Sparse-Low-Dynamic-Range-Panoramic-Images>Pano-NeRF: Synthesizing High Dynamic Range Novel Views with Geometry from Sparse Low Dynamic Range Panoramic Images</a></li>
        <li><a href=#Human101:-Training-100+FPS-Human-Gaussians-in-100s-from-1-View>Human101: Training 100+FPS Human Gaussians in 100s from 1 View</a></li>
        <li><a href=#Efficient-Deformable-Tissue-Reconstruction-via-Orthogonal-Neural-Plane>Efficient Deformable Tissue Reconstruction via Orthogonal Neural Plane</a></li>
        <li><a href=#CaLDiff:-Camera-Localization-in-NeRF-via-Pose-Diffusion>CaLDiff: Camera Localization in NeRF via Pose Diffusion</a></li>
      </ul>
    </li>
  </ol>
</details>

## SFM  

### [Residual Learning for Image Point Descriptors](http://arxiv.org/abs/2312.15471)  
Rashik Shrestha, Ajad Chhatkuli, Menelaos Kanakis, Luc Van Gool  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Local image feature descriptors have had a tremendous impact on the development and application of computer vision methods. It is therefore unsurprising that significant efforts are being made for learning-based image point descriptors. However, the advantage of learned methods over handcrafted methods in real applications is subtle and more nuanced than expected. Moreover, handcrafted descriptors such as SIFT and SURF still perform better point localization in Structure-from-Motion (SfM) compared to many learned counterparts. In this paper, we propose a very simple and effective approach to learning local image descriptors by using a hand-crafted detector and descriptor. Specifically, we choose to learn only the descriptors, supported by handcrafted descriptors while discarding the point localization head. We optimize the final descriptor by leveraging the knowledge already present in the handcrafted descriptor. Such an approach of optimization allows us to discard learning knowledge already present in non-differentiable functions such as the hand-crafted descriptors and only learn the residual knowledge in the main network branch. This offers 50X convergence speed compared to the standard baseline architecture of SuperPoint while at inference the combined descriptor provides superior performance over the learned and hand-crafted descriptors. This is done with minor increase in the computations over the baseline learned descriptor. Our approach has potential applications in ensemble learning and learning with non-differentiable functions. We perform experiments in matching, camera localization and Structure-from-Motion in order to showcase the advantages of our approach.  
  </ol>  
</details>  
  
  



## Visual Localization  

### [Recursive Distillation for Open-Set Distributed Robot Localization](http://arxiv.org/abs/2312.15897)  
Kenta Tsukahara, Kanji Tanaka  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    A typical assumption in state-of-the-art self-localization models is that an annotated training dataset is available for the target workspace. However, this is not necessarily true when a robot travels around the general open world. This work introduces a novel training scheme for open-world distributed robot systems. In our scheme, a robot (``student") can ask the other robots it meets at unfamiliar places (``teachers") for guidance. Specifically, a pseudo-training dataset is reconstructed from the teacher model and then used for continual learning of the student model under domain, class, and vocabulary incremental setup. Unlike typical knowledge transfer schemes, our scheme introduces only minimal assumptions on the teacher model, so that it can handle various types of open-set teachers, including those uncooperative, untrainable (e.g., image retrieval engines), or black-box teachers (i.e., data privacy). In this paper, we investigate a ranking function as an instance of such generic models, using a challenging data-free recursive distillation scenario, where a student once trained can recursively join the next-generation open teacher set.  
  </ol>  
</details>  
**comments**: 5 pages, 4 figures, technical report  
  
### [Residual Learning for Image Point Descriptors](http://arxiv.org/abs/2312.15471)  
Rashik Shrestha, Ajad Chhatkuli, Menelaos Kanakis, Luc Van Gool  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Local image feature descriptors have had a tremendous impact on the development and application of computer vision methods. It is therefore unsurprising that significant efforts are being made for learning-based image point descriptors. However, the advantage of learned methods over handcrafted methods in real applications is subtle and more nuanced than expected. Moreover, handcrafted descriptors such as SIFT and SURF still perform better point localization in Structure-from-Motion (SfM) compared to many learned counterparts. In this paper, we propose a very simple and effective approach to learning local image descriptors by using a hand-crafted detector and descriptor. Specifically, we choose to learn only the descriptors, supported by handcrafted descriptors while discarding the point localization head. We optimize the final descriptor by leveraging the knowledge already present in the handcrafted descriptor. Such an approach of optimization allows us to discard learning knowledge already present in non-differentiable functions such as the hand-crafted descriptors and only learn the residual knowledge in the main network branch. This offers 50X convergence speed compared to the standard baseline architecture of SuperPoint while at inference the combined descriptor provides superior performance over the learned and hand-crafted descriptors. This is done with minor increase in the computations over the baseline learned descriptor. Our approach has potential applications in ensemble learning and learning with non-differentiable functions. We perform experiments in matching, camera localization and Structure-from-Motion in order to showcase the advantages of our approach.  
  </ol>  
</details>  
  
### [CaLDiff: Camera Localization in NeRF via Pose Diffusion](http://arxiv.org/abs/2312.15242)  
Rashik Shrestha, Bishad Koju, Abhigyan Bhusal, Danda Pani Paudel, François Rameau  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    With the widespread use of NeRF-based implicit 3D representation, the need for camera localization in the same representation becomes manifestly apparent. Doing so not only simplifies the localization process -- by avoiding an outside-the-NeRF-based localization -- but also has the potential to offer the benefit of enhanced localization. This paper studies the problem of localizing cameras in NeRF using a diffusion model for camera pose adjustment. More specifically, given a pre-trained NeRF model, we train a diffusion model that iteratively updates randomly initialized camera poses, conditioned upon the image to be localized. At test time, a new camera is localized in two steps: first, coarse localization using the proposed pose diffusion process, followed by local refinement steps of a pose inversion process in NeRF. In fact, the proposed camera localization by pose diffusion (CaLDiff) method also integrates the pose inversion steps within the diffusion process. Such integration offers significantly better localization, thanks to our downstream refinement-aware diffusion process. Our exhaustive experiments on challenging real-world data validate our method by providing significantly better results than the compared methods and the established baselines. Our source code will be made publicly available.  
  </ol>  
</details>  
  
  



## Keypoint Detection  

### [Residual Learning for Image Point Descriptors](http://arxiv.org/abs/2312.15471)  
Rashik Shrestha, Ajad Chhatkuli, Menelaos Kanakis, Luc Van Gool  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Local image feature descriptors have had a tremendous impact on the development and application of computer vision methods. It is therefore unsurprising that significant efforts are being made for learning-based image point descriptors. However, the advantage of learned methods over handcrafted methods in real applications is subtle and more nuanced than expected. Moreover, handcrafted descriptors such as SIFT and SURF still perform better point localization in Structure-from-Motion (SfM) compared to many learned counterparts. In this paper, we propose a very simple and effective approach to learning local image descriptors by using a hand-crafted detector and descriptor. Specifically, we choose to learn only the descriptors, supported by handcrafted descriptors while discarding the point localization head. We optimize the final descriptor by leveraging the knowledge already present in the handcrafted descriptor. Such an approach of optimization allows us to discard learning knowledge already present in non-differentiable functions such as the hand-crafted descriptors and only learn the residual knowledge in the main network branch. This offers 50X convergence speed compared to the standard baseline architecture of SuperPoint while at inference the combined descriptor provides superior performance over the learned and hand-crafted descriptors. This is done with minor increase in the computations over the baseline learned descriptor. Our approach has potential applications in ensemble learning and learning with non-differentiable functions. We perform experiments in matching, camera localization and Structure-from-Motion in order to showcase the advantages of our approach.  
  </ol>  
</details>  
  
  



## Image Matching  

### [BEV-CV: Birds-Eye-View Transform for Cross-View Geo-Localisation](http://arxiv.org/abs/2312.15363)  
Tavis Shore, Simon Hadfield, Oscar Mendez  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Cross-view image matching for geo-localisation is a challenging problem due to the significant visual difference between aerial and ground-level viewpoints. The method provides localisation capabilities from geo-referenced images, eliminating the need for external devices or costly equipment. This enhances the capacity of agents to autonomously determine their position, navigate, and operate effectively in environments where GPS signals are unavailable. Current research employs a variety of techniques to reduce the domain gap such as applying polar transforms to aerial images or synthesising between perspectives. However, these approaches generally rely on having a 360{\deg} field of view, limiting real-world feasibility. We propose BEV-CV, an approach which introduces two key novelties. Firstly we bring ground-level images into a semantic Birds-Eye-View before matching embeddings, allowing for direct comparison with aerial segmentation representations. Secondly, we introduce the use of a Normalised Temperature-scaled Cross Entropy Loss to the sub-field, achieving faster convergence than with the standard triplet loss. BEV-CV achieves state-of-the-art recall accuracies, improving feature extraction Top-1 rates by more than 300%, and Top-1% rates by approximately 150% for 70{\deg} crops, and for orientation-aware application we achieve a 35% Top-1 accuracy increase with 70{\deg} crops.  
  </ol>  
</details>  
**comments**: 8 pages, 6 figures  
  
  



## NeRF  

### [LangSplat: 3D Language Gaussian Splatting](http://arxiv.org/abs/2312.16084)  
Minghan Qin, Wanhua Li, Jiawei Zhou, Haoqian Wang, Hanspeter Pfister  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Human lives in a 3D world and commonly uses natural language to interact with a 3D scene. Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently. This paper introduces LangSplat, which constructs a 3D language field that enables precise and efficient open-vocabulary querying within 3D spaces. Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled from CLIP, to represent the language field. By employing a tile-based splatting technique for rendering language features, we circumvent the costly rendering process inherent in NeRF. Instead of directly learning CLIP embeddings, LangSplat first trains a scene-wise language autoencoder and then learns language features on the scene-specific latent space, thereby alleviating substantial memory demands imposed by explicit modeling. Existing methods struggle with imprecise and vague 3D language fields, which fail to discern clear boundaries between objects. We delve into this issue and propose to learn hierarchical semantics using SAM, thereby eliminating the need for extensively querying the language field across various scales and the regularization of DINO features. Extensive experiments on open-vocabulary 3D object localization and semantic segmentation demonstrate that LangSplat significantly outperforms the previous state-of-the-art method LERF by a large margin. Notably, LangSplat is extremely efficient, achieving a {\speed} $\times$ speedup compared to LERF at the resolution of 1440 $\times$ 1080. We strongly recommend readers to check out our video results at https://langsplat.github.io  
  </ol>  
</details>  
**comments**: Project Page: https://langsplat.github.io  
  
### [2D-Guided 3D Gaussian Segmentation](http://arxiv.org/abs/2312.16047)  
Kun Lan, Haoran Li, Haolin Shi, Wenjun Wu, Yong Liao, Lin Wang, Pengyuan Zhou  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Recently, 3D Gaussian, as an explicit 3D representation method, has demonstrated strong competitiveness over NeRF (Neural Radiance Fields) in terms of expressing complex scenes and training duration. These advantages signal a wide range of applications for 3D Gaussians in 3D understanding and editing. Meanwhile, the segmentation of 3D Gaussians is still in its infancy. The existing segmentation methods are not only cumbersome but also incapable of segmenting multiple objects simultaneously in a short amount of time. In response, this paper introduces a 3D Gaussian segmentation method implemented with 2D segmentation as supervision. This approach uses input 2D segmentation maps to guide the learning of the added 3D Gaussian semantic information, while nearest neighbor clustering and statistical filtering refine the segmentation results. Experiments show that our concise method can achieve comparable performances on mIOU and mAcc for multi-object segmentation as previous single-object segmentation methods.  
  </ol>  
</details>  
  
### [Pano-NeRF: Synthesizing High Dynamic Range Novel Views with Geometry from Sparse Low Dynamic Range Panoramic Images](http://arxiv.org/abs/2312.15942)  
Zhan Lu, Qian Zheng, Boxin Shi, Xudong Jiang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Panoramic imaging research on geometry recovery and High Dynamic Range (HDR) reconstruction becomes a trend with the development of Extended Reality (XR). Neural Radiance Fields (NeRF) provide a promising scene representation for both tasks without requiring extensive prior data. However, in the case of inputting sparse Low Dynamic Range (LDR) panoramic images, NeRF often degrades with under-constrained geometry and is unable to reconstruct HDR radiance from LDR inputs. We observe that the radiance from each pixel in panoramic images can be modeled as both a signal to convey scene lighting information and a light source to illuminate other pixels. Hence, we propose the irradiance fields from sparse LDR panoramic images, which increases the observation counts for faithful geometry recovery and leverages the irradiance-radiance attenuation for HDR reconstruction. Extensive experiments demonstrate that the irradiance fields outperform state-of-the-art methods on both geometry recovery and HDR reconstruction and validate their effectiveness. Furthermore, we show a promising byproduct of spatially-varying lighting estimation. The code is available at https://github.com/Lu-Zhan/Pano-NeRF.  
  </ol>  
</details>  
  
### [Human101: Training 100+FPS Human Gaussians in 100s from 1 View](http://arxiv.org/abs/2312.15258)  
[[code](https://github.com/longxiang-ai/human101)]  
Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Reconstructing the human body from single-view videos plays a pivotal role in the virtual reality domain. One prevalent application scenario necessitates the rapid reconstruction of high-fidelity 3D digital humans while simultaneously ensuring real-time rendering and interaction. Existing methods often struggle to fulfill both requirements. In this paper, we introduce Human101, a novel framework adept at producing high-fidelity dynamic 3D human reconstructions from 1-view videos by training 3D Gaussians in 100 seconds and rendering in 100+ FPS. Our method leverages the strengths of 3D Gaussian Splatting, which provides an explicit and efficient representation of 3D humans. Standing apart from prior NeRF-based pipelines, Human101 ingeniously applies a Human-centric Forward Gaussian Animation method to deform the parameters of 3D Gaussians, thereby enhancing rendering speed (i.e., rendering 1024-resolution images at an impressive 60+ FPS and rendering 512-resolution images at 100+ FPS). Experimental results indicate that our approach substantially eclipses current methods, clocking up to a 10 times surge in frames per second and delivering comparable or superior rendering quality. Code and demos will be released at https://github.com/longxiang-ai/Human101.  
  </ol>  
</details>  
**comments**: Website: https://github.com/longxiang-ai/Human101  
  
### [Efficient Deformable Tissue Reconstruction via Orthogonal Neural Plane](http://arxiv.org/abs/2312.15253)  
[[code](https://github.com/loping151/forplane)]  
Chen Yang, Kailing Wang, Yuehao Wang, Qi Dou, Xiaokang Yang, Wei Shen  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Intraoperative imaging techniques for reconstructing deformable tissues in vivo are pivotal for advanced surgical systems. Existing methods either compromise on rendering quality or are excessively computationally intensive, often demanding dozens of hours to perform, which significantly hinders their practical application. In this paper, we introduce Fast Orthogonal Plane (Forplane), a novel, efficient framework based on neural radiance fields (NeRF) for the reconstruction of deformable tissues. We conceptualize surgical procedures as 4D volumes, and break them down into static and dynamic fields comprised of orthogonal neural planes. This factorization iscretizes the four-dimensional space, leading to a decreased memory usage and faster optimization. A spatiotemporal importance sampling scheme is introduced to improve performance in regions with tool occlusion as well as large motions and accelerate training. An efficient ray marching method is applied to skip sampling among empty regions, significantly improving inference speed. Forplane accommodates both binocular and monocular endoscopy videos, demonstrating its extensive applicability and flexibility. Our experiments, carried out on two in vivo datasets, the EndoNeRF and Hamlyn datasets, demonstrate the effectiveness of our framework. In all cases, Forplane substantially accelerates both the optimization process (by over 100 times) and the inference process (by over 15 times) while maintaining or even improving the quality across a variety of non-rigid deformations. This significant performance improvement promises to be a valuable asset for future intraoperative surgical applications. The code of our project is now available at https://github.com/Loping151/ForPlane.  
  </ol>  
</details>  
  
### [CaLDiff: Camera Localization in NeRF via Pose Diffusion](http://arxiv.org/abs/2312.15242)  
Rashik Shrestha, Bishad Koju, Abhigyan Bhusal, Danda Pani Paudel, François Rameau  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    With the widespread use of NeRF-based implicit 3D representation, the need for camera localization in the same representation becomes manifestly apparent. Doing so not only simplifies the localization process -- by avoiding an outside-the-NeRF-based localization -- but also has the potential to offer the benefit of enhanced localization. This paper studies the problem of localizing cameras in NeRF using a diffusion model for camera pose adjustment. More specifically, given a pre-trained NeRF model, we train a diffusion model that iteratively updates randomly initialized camera poses, conditioned upon the image to be localized. At test time, a new camera is localized in two steps: first, coarse localization using the proposed pose diffusion process, followed by local refinement steps of a pose inversion process in NeRF. In fact, the proposed camera localization by pose diffusion (CaLDiff) method also integrates the pose inversion steps within the diffusion process. Such integration offers significantly better localization, thanks to our downstream refinement-aware diffusion process. Our exhaustive experiments on challenging real-world data validate our method by providing significantly better results than the compared methods and the established baselines. Our source code will be made publicly available.  
  </ol>  
</details>  
  
  



