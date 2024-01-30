<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Cross-Modal-Coordination-Across-a-Diverse-Set-of-Input-Modalities>Cross-Modal Coordination Across a Diverse Set of Input Modalities</a></li>
        <li><a href=#Regressing-Transformers-for-Data-efficient-Visual-Place-Recognition>Regressing Transformers for Data-efficient Visual Place Recognition</a></li>
        <li><a href=#Transformer-based-Clipped-Contrastive-Quantization-Learning-for-Unsupervised-Image-Retrieval>Transformer-based Clipped Contrastive Quantization Learning for Unsupervised Image Retrieval</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#Reconstructing-Close-Human-Interactions-from-Multiple-Views>Reconstructing Close Human Interactions from Multiple Views</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#Endo-4DGS:-Distilling-Depth-Ranking-for-Endoscopic-Monocular-Scene-Reconstruction-with-4D-Gaussian-Splatting>Endo-4DGS: Distilling Depth Ranking for Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting</a></li>
        <li><a href=#Divide-and-Conquer:-Rethinking-the-Training-Paradigm-of-Neural-Radiance-Fields>Divide and Conquer: Rethinking the Training Paradigm of Neural Radiance Fields</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [Cross-Modal Coordination Across a Diverse Set of Input Modalities](http://arxiv.org/abs/2401.16347)  
Jorge Sánchez, Rodrigo Laguna  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Cross-modal retrieval is the task of retrieving samples of a given modality by using queries of a different one. Due to the wide range of practical applications, the problem has been mainly focused on the vision and language case, e.g. text to image retrieval, where models like CLIP have proven effective in solving such tasks. The dominant approach to learning such coordinated representations consists of projecting them onto a common space where matching views stay close and those from non-matching pairs are pushed away from each other. Although this cross-modal coordination has been applied also to other pairwise combinations, extending it to an arbitrary number of diverse modalities is a problem that has not been fully explored in the literature. In this paper, we propose two different approaches to the problem. The first is based on an extension of the CLIP contrastive objective to an arbitrary number of input modalities, while the second departs from the contrastive formulation and tackles the coordination problem by regressing the cross-modal similarities towards a target that reflects two simple and intuitive constraints of the cross-modal retrieval task. We run experiments on two different datasets, over different combinations of input modalities and show that the approach is not only simple and effective but also allows for tackling the retrieval problem in novel ways. Besides capturing a more diverse set of pair-wise interactions, we show that we can use the learned representations to improve retrieval performance by combining the embeddings from two or more such modalities.  
  </ol>  
</details>  
  
### [Regressing Transformers for Data-efficient Visual Place Recognition](http://arxiv.org/abs/2401.16304)  
María Leyva-Vallina, Nicola Strisciuglio, Nicolai Petkov  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Visual place recognition is a critical task in computer vision, especially for localization and navigation systems. Existing methods often rely on contrastive learning: image descriptors are trained to have small distance for similar images and larger distance for dissimilar ones in a latent space. However, this approach struggles to ensure accurate distance-based image similarity representation, particularly when training with binary pairwise labels, and complex re-ranking strategies are required. This work introduces a fresh perspective by framing place recognition as a regression problem, using camera field-of-view overlap as similarity ground truth for learning. By optimizing image descriptors to align directly with graded similarity labels, this approach enhances ranking capabilities without expensive re-ranking, offering data-efficient training and strong generalization across several benchmark datasets.  
  </ol>  
</details>  
**comments**: Accepted for publication in ICRA 2024  
  
### [Transformer-based Clipped Contrastive Quantization Learning for Unsupervised Image Retrieval](http://arxiv.org/abs/2401.15362)  
Ayush Dubey, Shiv Ram Dubey, Satish Kumar Singh, Wei-Ta Chu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Unsupervised image retrieval aims to learn the important visual characteristics without any given level to retrieve the similar images for a given query image. The Convolutional Neural Network (CNN)-based approaches have been extensively exploited with self-supervised contrastive learning for image hashing. However, the existing approaches suffer due to lack of effective utilization of global features by CNNs and biased-ness created by false negative pairs in the contrastive learning. In this paper, we propose a TransClippedCLR model by encoding the global context of an image using Transformer having local context through patch based processing, by generating the hash codes through product quantization and by avoiding the potential false negative pairs through clipped contrastive learning. The proposed model is tested with superior performance for unsupervised image retrieval on benchmark datasets, including CIFAR10, NUS-Wide and Flickr25K, as compared to the recent state-of-the-art deep models. The results using the proposed clipped contrastive learning are greatly improved on all datasets as compared to same backbone network with vanilla contrastive learning.  
  </ol>  
</details>  
  
  



## Keypoint Detection  

### [Reconstructing Close Human Interactions from Multiple Views](http://arxiv.org/abs/2401.16173)  
Qing Shuai, Zhiyuan Yu, Zhize Zhou, Lixin Fan, Haijun Yang, Can Yang, Xiaowei Zhou  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper addresses the challenging task of reconstructing the poses of multiple individuals engaged in close interactions, captured by multiple calibrated cameras. The difficulty arises from the noisy or false 2D keypoint detections due to inter-person occlusion, the heavy ambiguity in associating keypoints to individuals due to the close interactions, and the scarcity of training data as collecting and annotating motion data in crowded scenes is resource-intensive. We introduce a novel system to address these challenges. Our system integrates a learning-based pose estimation component and its corresponding training and inference strategies. The pose estimation component takes multi-view 2D keypoint heatmaps as input and reconstructs the pose of each individual using a 3D conditional volumetric network. As the network doesn't need images as input, we can leverage known camera parameters from test scenes and a large quantity of existing motion capture data to synthesize massive training data that mimics the real data distribution in test scenes. Extensive experiments demonstrate that our approach significantly surpasses previous approaches in terms of pose accuracy and is generalizable across various camera setups and population sizes. The code is available on our project page: https://github.com/zju3dv/CloseMoCap.  
  </ol>  
</details>  
**comments**: SIGGRAPH Asia 2023  
  
  



## NeRF  

### [Endo-4DGS: Distilling Depth Ranking for Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting](http://arxiv.org/abs/2401.16416)  
Yiming Huang, Beilei Cui, Long Bai, Ziqi Guo, Mengya Xu, Hongliang Ren  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    In the realm of robot-assisted minimally invasive surgery, dynamic scene reconstruction can significantly enhance downstream tasks and improve surgical outcomes. Neural Radiance Fields (NeRF)-based methods have recently risen to prominence for their exceptional ability to reconstruct scenes. Nonetheless, these methods are hampered by slow inference, prolonged training, and substantial computational demands. Additionally, some rely on stereo depth estimation, which is often infeasible due to the high costs and logistical challenges associated with stereo cameras. Moreover, the monocular reconstruction quality for deformable scenes is currently inadequate. To overcome these obstacles, we present Endo-4DGS, an innovative, real-time endoscopic dynamic reconstruction approach that utilizes 4D Gaussian Splatting (GS) and requires no ground truth depth data. This method extends 3D GS by incorporating a temporal component and leverages a lightweight MLP to capture temporal Gaussian deformations. This effectively facilitates the reconstruction of dynamic surgical scenes with variable conditions. We also integrate Depth-Anything to generate pseudo-depth maps from monocular views, enhancing the depth-guided reconstruction process. Our approach has been validated on two surgical datasets, where it has proven to render in real-time, compute efficiently, and reconstruct with remarkable accuracy. These results underline the vast potential of Endo-4DGS to improve surgical assistance.  
  </ol>  
</details>  
  
### [Divide and Conquer: Rethinking the Training Paradigm of Neural Radiance Fields](http://arxiv.org/abs/2401.16144)  
Rongkai Ma, Leo Lebrat, Rodrigo Santa Cruz, Gil Avraham, Yan Zuo, Clinton Fookes, Olivier Salvado  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural radiance fields (NeRFs) have exhibited potential in synthesizing high-fidelity views of 3D scenes but the standard training paradigm of NeRF presupposes an equal importance for each image in the training set. This assumption poses a significant challenge for rendering specific views presenting intricate geometries, thereby resulting in suboptimal performance. In this paper, we take a closer look at the implications of the current training paradigm and redesign this for more superior rendering quality by NeRFs. Dividing input views into multiple groups based on their visual similarities and training individual models on each of these groups enables each model to specialize on specific regions without sacrificing speed or efficiency. Subsequently, the knowledge of these specialized models is aggregated into a single entity via a teacher-student distillation paradigm, enabling spatial efficiency for online render-ing. Empirically, we evaluate our novel training framework on two publicly available datasets, namely NeRF synthetic and Tanks&Temples. Our evaluation demonstrates that our DaC training pipeline enhances the rendering quality of a state-of-the-art baseline model while exhibiting convergence to a superior minimum.  
  </ol>  
</details>  
  
  



