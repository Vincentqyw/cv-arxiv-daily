<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Enhancing-Image-Retrieval-:-A-Comprehensive-Study-on-Photo-Search-using-the-CLIP-Mode>Enhancing Image Retrieval : A Comprehensive Study on Photo Search using the CLIP Mode</a></li>
        <li><a href=#PlaceFormer:-Transformer-based-Visual-Place-Recognition-using-Multi-Scale-Patch-Selection-and-Fusion>PlaceFormer: Transformer-based Visual Place Recognition using Multi-Scale Patch Selection and Fusion</a></li>
        <li><a href=#SemanticSLAM:-Learning-based-Semantic-Map-Construction-and-Robust-Camera-Localization>SemanticSLAM: Learning based Semantic Map Construction and Robust Camera Localization</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#Linear-Relative-Pose-Estimation-Founded-on-Pose-only-Imaging-Geometry>Linear Relative Pose Estimation Founded on Pose-only Imaging Geometry</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#EndoGaussians:-Single-View-Dynamic-Gaussian-Splatting-for-Deformable-Endoscopic-Tissues-Reconstruction>EndoGaussians: Single View Dynamic Gaussian Splatting for Deformable Endoscopic Tissues Reconstruction</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [Enhancing Image Retrieval : A Comprehensive Study on Photo Search using the CLIP Mode](http://arxiv.org/abs/2401.13613)  
Naresh Kumar Lahajal, Harini S  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Photo search, the task of retrieving images based on textual queries, has witnessed significant advancements with the introduction of CLIP (Contrastive Language-Image Pretraining) model. CLIP leverages a vision-language pre training approach, wherein it learns a shared representation space for images and text, enabling cross-modal understanding. This model demonstrates the capability to understand the semantic relationships between diverse image and text pairs, allowing for efficient and accurate retrieval of images based on natural language queries. By training on a large-scale dataset containing images and their associated textual descriptions, CLIP achieves remarkable generalization, providing a powerful tool for tasks such as zero-shot learning and few-shot classification. This abstract summarizes the foundational principles of CLIP and highlights its potential impact on advancing the field of photo search, fostering a seamless integration of natural language understanding and computer vision for improved information retrieval in multimedia applications  
  </ol>  
</details>  
  
### [PlaceFormer: Transformer-based Visual Place Recognition using Multi-Scale Patch Selection and Fusion](http://arxiv.org/abs/2401.13082)  
Shyam Sundar Kannan, Byung-Cheol Min  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Visual place recognition is a challenging task in the field of computer vision, and autonomous robotics and vehicles, which aims to identify a location or a place from visual inputs. Contemporary methods in visual place recognition employ convolutional neural networks and utilize every region within the image for the place recognition task. However, the presence of dynamic and distracting elements in the image may impact the effectiveness of the place recognition process. Therefore, it is meaningful to focus on task-relevant regions of the image for improved recognition. In this paper, we present PlaceFormer, a novel transformer-based approach for visual place recognition. PlaceFormer employs patch tokens from the transformer to create global image descriptors, which are then used for image retrieval. To re-rank the retrieved images, PlaceFormer merges the patch tokens from the transformer to form multi-scale patches. Utilizing the transformer's self-attention mechanism, it selects patches that correspond to task-relevant areas in an image. These selected patches undergo geometric verification, generating similarity scores across different patch sizes. Subsequently, spatial scores from each patch size are fused to produce a final similarity score. This score is then used to re-rank the images initially retrieved using global image descriptors. Extensive experiments on benchmark datasets demonstrate that PlaceFormer outperforms several state-of-the-art methods in terms of accuracy and computational efficiency, requiring less time and memory.  
  </ol>  
</details>  
  
### [SemanticSLAM: Learning based Semantic Map Construction and Robust Camera Localization](http://arxiv.org/abs/2401.13076)  
[[code](https://github.com/leomingyangli/semanticslam)]  
Mingyang Li, Yue Ma, Qinru Qiu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Current techniques in Visual Simultaneous Localization and Mapping (VSLAM) estimate camera displacement by comparing image features of consecutive scenes. These algorithms depend on scene continuity, hence requires frequent camera inputs. However, processing images frequently can lead to significant memory usage and computation overhead. In this study, we introduce SemanticSLAM, an end-to-end visual-inertial odometry system that utilizes semantic features extracted from an RGB-D sensor. This approach enables the creation of a semantic map of the environment and ensures reliable camera localization. SemanticSLAM is scene-agnostic, which means it doesn't require retraining for different environments. It operates effectively in indoor settings, even with infrequent camera input, without prior knowledge. The strength of SemanticSLAM lies in its ability to gradually refine the semantic map and improve pose estimation. This is achieved by a convolutional long-short-term-memory (ConvLSTM) network, trained to correct errors during map construction. Compared to existing VSLAM algorithms, SemanticSLAM improves pose estimation by 17%. The resulting semantic map provides interpretable information about the environment and can be easily applied to various downstream tasks, such as path planning, obstacle avoidance, and robot navigation. The code will be publicly available at https://github.com/Leomingyangli/SemanticSLAM  
  </ol>  
</details>  
**comments**: 2023 IEEE Symposium Series on Computational Intelligence (SSCI) 6
  pages  
  
  



## Image Matching  

### [Linear Relative Pose Estimation Founded on Pose-only Imaging Geometry](http://arxiv.org/abs/2401.13357)  
Qi Cai, Xinrui Li, Yuanxin Wu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    How to efficiently and accurately handle image matching outliers is a critical issue in two-view relative estimation. The prevailing RANSAC method necessitates that the minimal point pairs be inliers. This paper introduces a linear relative pose estimation algorithm for n $( n \geq 6$) point pairs, which is founded on the recent pose-only imaging geometry to filter out outliers by proper reweighting. The proposed algorithm is able to handle planar degenerate scenes, and enhance robustness and accuracy in the presence of a substantial ratio of outliers. Specifically, we embed the linear global translation (LiGT) constraint into the strategies of iteratively reweighted least-squares (IRLS) and RANSAC so as to realize robust outlier removal. Simulations and real tests of the Strecha dataset show that the proposed algorithm achieves relative rotation accuracy improvement of 2 $\sim$ 10 times in face of as large as 80% outliers.  
  </ol>  
</details>  
  
  



## NeRF  

### [EndoGaussians: Single View Dynamic Gaussian Splatting for Deformable Endoscopic Tissues Reconstruction](http://arxiv.org/abs/2401.13352)  
Yangsen Chen, Hao Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The accurate 3D reconstruction of deformable soft body tissues from endoscopic videos is a pivotal challenge in medical applications such as VR surgery and medical image analysis. Existing methods often struggle with accuracy and the ambiguity of hallucinated tissue parts, limiting their practical utility. In this work, we introduce EndoGaussians, a novel approach that employs Gaussian Splatting for dynamic endoscopic 3D reconstruction. This method marks the first use of Gaussian Splatting in this context, overcoming the limitations of previous NeRF-based techniques. Our method sets new state-of-the-art standards, as demonstrated by quantitative assessments on various endoscope datasets. These advancements make our method a promising tool for medical professionals, offering more reliable and efficient 3D reconstructions for practical applications in the medical field.  
  </ol>  
</details>  
  
  



