<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#Structure-from-Duplicates:-Neural-Inverse-Graphics-from-a-Pile-of-Objects>Structure from Duplicates: Neural Inverse Graphics from a Pile of Objects</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Modality-Aware-Representation-Learning-for-Zero-shot-Sketch-based-Image-Retrieval>Modality-Aware Representation Learning for Zero-shot Sketch-based Image Retrieval</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#InseRF:-Text-Driven-Generative-Object-Insertion-in-Neural-3D-Scenes>InseRF: Text-Driven Generative Object Insertion in Neural 3D Scenes</a></li>
        <li><a href=#CTNeRF:-Cross-Time-Transformer-for-Dynamic-Neural-Radiance-Field-from-Monocular-Video>CTNeRF: Cross-Time Transformer for Dynamic Neural Radiance Field from Monocular Video</a></li>
      </ul>
    </li>
  </ol>
</details>

## SFM  

### [Structure from Duplicates: Neural Inverse Graphics from a Pile of Objects](http://arxiv.org/abs/2401.05236)  
[[code](https://github.com/tianhang-cheng/sfd)]  
Tianhang Cheng, Wei-Chiu Ma, Kaiyu Guan, Antonio Torralba, Shenlong Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Our world is full of identical objects (\emphe.g., cans of coke, cars of same model). These duplicates, when seen together, provide additional and strong cues for us to effectively reason about 3D. Inspired by this observation, we introduce Structure from Duplicates (SfD), a novel inverse graphics framework that reconstructs geometry, material, and illumination from a single image containing multiple identical objects. SfD begins by identifying multiple instances of an object within an image, and then jointly estimates the 6DoF pose for all instances.An inverse graphics pipeline is subsequently employed to jointly reason about the shape, material of the object, and the environment light, while adhering to the shared geometry and material constraint across instances. Our primary contributions involve utilizing object duplicates as a robust prior for single-image inverse graphics and proposing an in-plane rotation-robust Structure from Motion (SfM) formulation for joint 6-DoF object pose estimation. By leveraging multi-view cues from a single image, SfD generates more realistic and detailed 3D reconstructions, significantly outperforming existing single image reconstruction models and multi-view reconstruction approaches with a similar or greater number of observations.  
  </ol>  
</details>  
**comments**: Code: https://github.com/Tianhang-Cheng/SfD  
  
  



## Visual Localization  

### [Modality-Aware Representation Learning for Zero-shot Sketch-based Image Retrieval](http://arxiv.org/abs/2401.04860)  
Eunyi Lyou, Doyeon Lee, Jooeun Kim, Joonseok Lee  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Zero-shot learning offers an efficient solution for a machine learning model to treat unseen categories, avoiding exhaustive data collection. Zero-shot Sketch-based Image Retrieval (ZS-SBIR) simulates real-world scenarios where it is hard and costly to collect paired sketch-photo samples. We propose a novel framework that indirectly aligns sketches and photos by contrasting them through texts, removing the necessity of access to sketch-photo pairs. With an explicit modality encoding learned from data, our approach disentangles modality-agnostic semantics from modality-specific information, bridging the modality gap and enabling effective cross-modal content retrieval within a joint latent space. From comprehensive experiments, we verify the efficacy of the proposed model on ZS-SBIR, and it can be also applied to generalized and fine-grained settings.  
  </ol>  
</details>  
**comments**: Accepted at WACV 2024  
  
  



## NeRF  

### [InseRF: Text-Driven Generative Object Insertion in Neural 3D Scenes](http://arxiv.org/abs/2401.05335)  
Mohamad Shahbazi, Liesbeth Claessens, Michael Niemeyer, Edo Collins, Alessio Tonioni, Luc Van Gool, Federico Tombari  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We introduce InseRF, a novel method for generative object insertion in the NeRF reconstructions of 3D scenes. Based on a user-provided textual description and a 2D bounding box in a reference viewpoint, InseRF generates new objects in 3D scenes. Recently, methods for 3D scene editing have been profoundly transformed, owing to the use of strong priors of text-to-image diffusion models in 3D generative modeling. Existing methods are mostly effective in editing 3D scenes via style and appearance changes or removing existing objects. Generating new objects, however, remains a challenge for such methods, which we address in this study. Specifically, we propose grounding the 3D object insertion to a 2D object insertion in a reference view of the scene. The 2D edit is then lifted to 3D using a single-view object reconstruction method. The reconstructed object is then inserted into the scene, guided by the priors of monocular depth estimation methods. We evaluate our method on various 3D scenes and provide an in-depth analysis of the proposed components. Our experiments with generative insertion of objects in several 3D scenes indicate the effectiveness of our method compared to the existing methods. InseRF is capable of controllable and 3D-consistent object insertion without requiring explicit 3D information as input. Please visit our project page at https://mohamad-shahbazi.github.io/inserf.  
  </ol>  
</details>  
  
### [CTNeRF: Cross-Time Transformer for Dynamic Neural Radiance Field from Monocular Video](http://arxiv.org/abs/2401.04861)  
Xingyu Miao, Yang Bai, Haoran Duan, Yawen Huang, Fan Wan, Yang Long, Yefeng Zheng  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The goal of our work is to generate high-quality novel views from monocular videos of complex and dynamic scenes. Prior methods, such as DynamicNeRF, have shown impressive performance by leveraging time-varying dynamic radiation fields. However, these methods have limitations when it comes to accurately modeling the motion of complex objects, which can lead to inaccurate and blurry renderings of details. To address this limitation, we propose a novel approach that builds upon a recent generalization NeRF, which aggregates nearby views onto new viewpoints. However, such methods are typically only effective for static scenes. To overcome this challenge, we introduce a module that operates in both the time and frequency domains to aggregate the features of object motion. This allows us to learn the relationship between frames and generate higher-quality images. Our experiments demonstrate significant improvements over state-of-the-art methods on dynamic scene datasets. Specifically, our approach outperforms existing methods in terms of both the accuracy and visual quality of the synthesized views.  
  </ol>  
</details>  
  
  



