<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#BrainSLAM:-SLAM-on-Neural-Population-Activity-Data>BrainSLAM: SLAM on Neural Population Activity Data</a></li>
        <li><a href=#Night-Rider:-Nocturnal-Vision-aided-Localization-in-Streetlight-Maps-Using-Invariant-Extended-Kalman-Filtering>Night-Rider: Nocturnal Vision-aided Localization in Streetlight Maps Using Invariant Extended Kalman Filtering</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#ViCA-NeRF:-View-Consistency-Aware-3D-Editing-of-Neural-Radiance-Fields>ViCA-NeRF: View-Consistency-Aware 3D Editing of Neural Radiance Fields</a></li>
        <li><a href=#Emo-Avatar:-Efficient-Monocular-Video-Style-Avatar-through-Texture-Rendering>Emo-Avatar: Efficient Monocular Video Style Avatar through Texture Rendering</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [BrainSLAM: SLAM on Neural Population Activity Data](http://arxiv.org/abs/2402.00588)  
Kipp Freud, Nathan Lepora, Matt W. Jones, Cian O'Donnell  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Simultaneous localisation and mapping (SLAM) algorithms are commonly used in robotic systems for learning maps of novel environments. Brains also appear to learn maps, but the mechanisms are not known and it is unclear how to infer these maps from neural activity data. We present BrainSLAM; a method for performing SLAM using only population activity (local field potential, LFP) data simultaneously recorded from three brain regions in rats: hippocampus, prefrontal cortex, and parietal cortex. This system uses a convolutional neural network (CNN) to decode velocity and familiarity information from wavelet scalograms of neural local field potential data recorded from rats as they navigate a 2D maze. The CNN's output drives a RatSLAM-inspired architecture, powering an attractor network which performs path integration plus a separate system which performs `loop closure' (detecting previously visited locations and correcting map aliasing errors). Together, these three components can construct faithful representations of the environment while simultaneously tracking the animal's location. This is the first demonstration of inference of a spatial map from brain recordings. Our findings expand SLAM to a new modality, enabling a new method of mapping environments and facilitating a better understanding of the role of cognitive maps in navigation and decision making.  
  </ol>  
</details>  
**comments**: Accepted to the 23rd International Conference on Autonomous Agents
  and Multiagent Systems. 2024  
  
### [Night-Rider: Nocturnal Vision-aided Localization in Streetlight Maps Using Invariant Extended Kalman Filtering](http://arxiv.org/abs/2402.00330)  
Tianxiao Gao, Mingle Zhao, Chengzhong Xu, Hui Kong  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Vision-aided localization for low-cost mobile robots in diverse environments has attracted widespread attention recently. Although many current systems are applicable in daytime environments, nocturnal visual localization is still an open problem owing to the lack of stable visual information. An insight from most nocturnal scenes is that the static and bright streetlights are reliable visual information for localization. Hence we propose a nocturnal vision-aided localization system in streetlight maps with a novel data association and matching scheme using object detection methods. We leverage the Invariant Extended Kalman Filter (InEKF) to fuse IMU, odometer, and camera measurements for consistent state estimation at night. Furthermore, a tracking recovery module is also designed for tracking failures. Experiments on multiple real nighttime scenes validate that the system can achieve remarkably accurate and robust localization in nocturnal environments.  
  </ol>  
</details>  
  
  



## NeRF  

### [ViCA-NeRF: View-Consistency-Aware 3D Editing of Neural Radiance Fields](http://arxiv.org/abs/2402.00864)  
[[code](https://github.com/dongjiahua/vica-nerf)]  
Jiahua Dong, Yu-Xiong Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    We introduce ViCA-NeRF, the first view-consistency-aware method for 3D editing with text instructions. In addition to the implicit neural radiance field (NeRF) modeling, our key insight is to exploit two sources of regularization that explicitly propagate the editing information across different views, thus ensuring multi-view consistency. For geometric regularization, we leverage the depth information derived from NeRF to establish image correspondences between different views. For learned regularization, we align the latent codes in the 2D diffusion model between edited and unedited images, enabling us to edit key views and propagate the update throughout the entire scene. Incorporating these two strategies, our ViCA-NeRF operates in two stages. In the initial stage, we blend edits from different views to create a preliminary 3D edit. This is followed by a second stage of NeRF training, dedicated to further refining the scene's appearance. Experimental results demonstrate that ViCA-NeRF provides more flexible, efficient (3 times faster) editing with higher levels of consistency and details, compared with the state of the art. Our code is publicly available.  
  </ol>  
</details>  
**comments**: Neurips2023; project page: https://github.com/Dongjiahua/VICA-NeRF  
  
### [Emo-Avatar: Efficient Monocular Video Style Avatar through Texture Rendering](http://arxiv.org/abs/2402.00827)  
Pinxin Liu, Luchuan Song, Daoan Zhang, Hang Hua, Yunlong Tang, Huaijin Tu, Jiebo Luo, Chenliang Xu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Artistic video portrait generation is a significant and sought-after task in the fields of computer graphics and vision. While various methods have been developed that integrate NeRFs or StyleGANs with instructional editing models for creating and editing drivable portraits, these approaches face several challenges. They often rely heavily on large datasets, require extensive customization processes, and frequently result in reduced image quality. To address the above problems, we propose the Efficient Monotonic Video Style Avatar (Emo-Avatar) through deferred neural rendering that enhances StyleGAN's capacity for producing dynamic, drivable portrait videos. We proposed a two-stage deferred neural rendering pipeline. In the first stage, we utilize few-shot PTI initialization to initialize the StyleGAN generator through several extreme poses sampled from the video to capture the consistent representation of aligned faces from the target portrait. In the second stage, we propose a Laplacian pyramid for high-frequency texture sampling from UV maps deformed by dynamic flow of expression for motion-aware texture prior integration to provide torso features to enhance StyleGAN's ability to generate complete and upper body for portrait video rendering. Emo-Avatar reduces style customization time from hours to merely 5 minutes compared with existing methods. In addition, Emo-Avatar requires only a single reference image for editing and employs region-aware contrastive learning with semantic invariant CLIP guidance, ensuring consistent high-resolution output and identity preservation. Through both quantitative and qualitative assessments, Emo-Avatar demonstrates superior performance over existing methods in terms of training efficiency, rendering quality and editability in self- and cross-reenactment.  
  </ol>  
</details>  
  
  



