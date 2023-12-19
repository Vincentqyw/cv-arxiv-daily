<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#Transformers-in-Unsupervised-Structure-from-Motion>Transformers in Unsupervised Structure-from-Motion</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#PNeRFLoc:-Visual-Localization-with-Point-based-Neural-Radiance-Fields>PNeRFLoc: Visual Localization with Point-based Neural Radiance Fields</a></li>
        <li><a href=#DistilVPR:-Cross-Modal-Knowledge-Distillation-for-Visual-Place-Recognition>DistilVPR: Cross-Modal Knowledge Distillation for Visual Place Recognition</a></li>
        <li><a href=#Symmetrical-Bidirectional-Knowledge-Alignment-for-Zero-Shot-Sketch-Based-Image-Retrieval>Symmetrical Bidirectional Knowledge Alignment for Zero-Shot Sketch-Based Image Retrieval</a></li>
        <li><a href=#Data-Efficient-Multimodal-Fusion-on-a-Single-GPU>Data-Efficient Multimodal Fusion on a Single GPU</a></li>
        <li><a href=#Advancements-in-Content-Based-Image-Retrieval:-A-Comprehensive-Survey-of-Relevance-Feedback-Techniques>Advancements in Content-Based Image Retrieval: A Comprehensive Survey of Relevance Feedback Techniques</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#PNeRFLoc:-Visual-Localization-with-Point-based-Neural-Radiance-Fields>PNeRFLoc: Visual Localization with Point-based Neural Radiance Fields</a></li>
        <li><a href=#Learning-Dense-Correspondence-for-NeRF-Based-Face-Reenactment>Learning Dense Correspondence for NeRF-Based Face Reenactment</a></li>
      </ul>
    </li>
  </ol>
</details>

## SFM  

### [Transformers in Unsupervised Structure-from-Motion](http://arxiv.org/abs/2312.10529)  
[[code](https://github.com/neurai-lab/mt-sfmlearner)]  
Hemang Chawla, Arnav Varma, Elahe Arani, Bahram Zonooz  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Transformers have revolutionized deep learning based computer vision with improved performance as well as robustness to natural corruptions and adversarial attacks. Transformers are used predominantly for 2D vision tasks, including image classification, semantic segmentation, and object detection. However, robots and advanced driver assistance systems also require 3D scene understanding for decision making by extracting structure-from-motion (SfM). We propose a robust transformer-based monocular SfM method that learns to predict monocular pixel-wise depth, ego vehicle's translation and rotation, as well as camera's focal length and principal point, simultaneously. With experiments on KITTI and DDAD datasets, we demonstrate how to adapt different vision transformers and compare them against contemporary CNN-based methods. Our study shows that transformer-based architecture, though lower in run-time efficiency, achieves comparable performance while being more robust against natural corruptions, as well as untargeted and targeted attacks.  
  </ol>  
</details>  
**comments**: International Joint Conference on Computer Vision, Imaging and
  Computer Graphics. Cham: Springer Nature Switzerland, 2022. Published at
  "Communications in Computer and Information Science, vol 1815. Springer
  Nature". arXiv admin note: text overlap with arXiv:2202.03131  
  
  



## Visual Localization  

### [PNeRFLoc: Visual Localization with Point-based Neural Radiance Fields](http://arxiv.org/abs/2312.10649)  
Boming Zhao, Luwei Yang, Mao Mao, Hujun Bao, Zhaopeng Cui  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Due to the ability to synthesize high-quality novel views, Neural Radiance Fields (NeRF) have been recently exploited to improve visual localization in a known environment. However, the existing methods mostly utilize NeRFs for data augmentation to improve the regression model training, and the performance on novel viewpoints and appearances is still limited due to the lack of geometric constraints. In this paper, we propose a novel visual localization framework, \ie, PNeRFLoc, based on a unified point-based representation. On the one hand, PNeRFLoc supports the initial pose estimation by matching 2D and 3D feature points as traditional structure-based methods; on the other hand, it also enables pose refinement with novel view synthesis using rendering-based optimization. Specifically, we propose a novel feature adaption module to close the gaps between the features for visual localization and neural rendering. To improve the efficacy and efficiency of neural rendering-based optimization, we also develop an efficient rendering-based framework with a warping loss function. Furthermore, several robustness techniques are developed to handle illumination changes and dynamic objects for outdoor scenarios. Experiments demonstrate that PNeRFLoc performs the best on synthetic data when the NeRF model can be well learned and performs on par with the SOTA method on the visual localization benchmark datasets.  
  </ol>  
</details>  
**comments**: Accepted to AAAI 2024  
  
### [DistilVPR: Cross-Modal Knowledge Distillation for Visual Place Recognition](http://arxiv.org/abs/2312.10616)  
[[code](https://github.com/sijieaaa/distilvpr)]  
Sijie Wang, Rui She, Qiyu Kang, Xingchao Jian, Kai Zhao, Yang Song, Wee Peng Tay  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The utilization of multi-modal sensor data in visual place recognition (VPR) has demonstrated enhanced performance compared to single-modal counterparts. Nonetheless, integrating additional sensors comes with elevated costs and may not be feasible for systems that demand lightweight operation, thereby impacting the practical deployment of VPR. To address this issue, we resort to knowledge distillation, which empowers single-modal students to learn from cross-modal teachers without introducing additional sensors during inference. Despite the notable advancements achieved by current distillation approaches, the exploration of feature relationships remains an under-explored area. In order to tackle the challenge of cross-modal distillation in VPR, we present DistilVPR, a novel distillation pipeline for VPR. We propose leveraging feature relationships from multiple agents, including self-agents and cross-agents for teacher and student neural networks. Furthermore, we integrate various manifolds, characterized by different space curvatures for exploring feature relationships. This approach enhances the diversity of feature relationships, including Euclidean, spherical, and hyperbolic relationship modules, thereby enhancing the overall representational capacity. The experiments demonstrate that our proposed pipeline achieves state-of-the-art performance compared to other distillation baselines. We also conduct necessary ablation studies to show design effectiveness. The code is released at: https://github.com/sijieaaa/DistilVPR  
  </ol>  
</details>  
**comments**: Accepted by AAAI 2024  
  
### [Symmetrical Bidirectional Knowledge Alignment for Zero-Shot Sketch-Based Image Retrieval](http://arxiv.org/abs/2312.10320)  
Decheng Liu, Xu Luo, Chunlei Peng, Nannan Wang, Ruimin Hu, Xinbo Gao  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper studies the problem of zero-shot sketch-based image retrieval (ZS-SBIR), which aims to use sketches from unseen categories as queries to match the images of the same category. Due to the large cross-modality discrepancy, ZS-SBIR is still a challenging task and mimics realistic zero-shot scenarios. The key is to leverage transferable knowledge from the pre-trained model to improve generalizability. Existing researchers often utilize the simple fine-tuning training strategy or knowledge distillation from a teacher model with fixed parameters, lacking efficient bidirectional knowledge alignment between student and teacher models simultaneously for better generalization. In this paper, we propose a novel Symmetrical Bidirectional Knowledge Alignment for zero-shot sketch-based image retrieval (SBKA). The symmetrical bidirectional knowledge alignment learning framework is designed to effectively learn mutual rich discriminative information between teacher and student models to achieve the goal of knowledge alignment. Instead of the former one-to-one cross-modality matching in the testing stage, a one-to-many cluster cross-modality matching method is proposed to leverage the inherent relationship of intra-class images to reduce the adverse effects of the existing modality gap. Experiments on several representative ZS-SBIR datasets (Sketchy Ext dataset, TU-Berlin Ext dataset and QuickDraw Ext dataset) prove the proposed algorithm can achieve superior performance compared with state-of-the-art methods.  
  </ol>  
</details>  
  
### [Data-Efficient Multimodal Fusion on a Single GPU](http://arxiv.org/abs/2312.10144)  
[[code](https://github.com/layer6ai-labs/fusemix)]  
Noël Vouitsis, Zhaoyan Liu, Satya Krishna Gorti, Valentin Villecroze, Jesse C. Cresswell, Guangwei Yu, Gabriel Loaiza-Ganem, Maksims Volkovs  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The goal of multimodal alignment is to learn a single latent space that is shared between multimodal inputs. The most powerful models in this space have been trained using massive datasets of paired inputs and large-scale computational resources, making them prohibitively expensive to train in many practical scenarios. We surmise that existing unimodal encoders pre-trained on large amounts of unimodal data should provide an effective bootstrap to create multimodal models from unimodal ones at much lower costs. We therefore propose FuseMix, a multimodal augmentation scheme that operates on the latent spaces of arbitrary pre-trained unimodal encoders. Using FuseMix for multimodal alignment, we achieve competitive performance -- and in certain cases outperform state-of-the art methods -- in both image-text and audio-text retrieval, with orders of magnitude less compute and data: for example, we outperform CLIP on the Flickr30K text-to-image retrieval task with $\sim \! 600\times$ fewer GPU days and $\sim \! 80\times$ fewer image-text pairs. Additionally, we show how our method can be applied to convert pre-trained text-to-image generative models into audio-to-image ones. Code is available at: https://github.com/layer6ai-labs/fusemix.  
  </ol>  
</details>  
  
### [Advancements in Content-Based Image Retrieval: A Comprehensive Survey of Relevance Feedback Techniques](http://arxiv.org/abs/2312.10089)  
Hamed Qazanfari, Mohammad M. AlyanNezhadi, Zohreh Nozari Khoshdaregi  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Content-based image retrieval (CBIR) systems have emerged as crucial tools in the field of computer vision, allowing for image search based on visual content rather than relying solely on metadata. This survey paper presents a comprehensive overview of CBIR, emphasizing its role in object detection and its potential to identify and retrieve visually similar images based on content features. Challenges faced by CBIR systems, including the semantic gap and scalability, are discussed, along with potential solutions. It elaborates on the semantic gap, which arises from the disparity between low-level features and high-level semantic concepts, and explores approaches to bridge this gap. One notable solution is the integration of relevance feedback (RF), empowering users to provide feedback on retrieved images and refine search results iteratively. The survey encompasses long-term and short-term learning approaches that leverage RF for enhanced CBIR accuracy and relevance. These methods focus on weight optimization and the utilization of active learning algorithms to select samples for training classifiers. Furthermore, the paper investigates machine learning techniques and the utilization of deep learning and convolutional neural networks to enhance CBIR performance. This survey paper plays a significant role in advancing the understanding of CBIR and RF techniques. It guides researchers and practitioners in comprehending existing methodologies, challenges, and potential solutions while fostering knowledge dissemination and identifying research gaps. By addressing future research directions, it sets the stage for advancements in CBIR that will enhance retrieval accuracy, usability, and effectiveness in various application domains.  
  </ol>  
</details>  
**comments**: 7 pages, 2 figures  
  
  



## NeRF  

### [PNeRFLoc: Visual Localization with Point-based Neural Radiance Fields](http://arxiv.org/abs/2312.10649)  
Boming Zhao, Luwei Yang, Mao Mao, Hujun Bao, Zhaopeng Cui  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Due to the ability to synthesize high-quality novel views, Neural Radiance Fields (NeRF) have been recently exploited to improve visual localization in a known environment. However, the existing methods mostly utilize NeRFs for data augmentation to improve the regression model training, and the performance on novel viewpoints and appearances is still limited due to the lack of geometric constraints. In this paper, we propose a novel visual localization framework, \ie, PNeRFLoc, based on a unified point-based representation. On the one hand, PNeRFLoc supports the initial pose estimation by matching 2D and 3D feature points as traditional structure-based methods; on the other hand, it also enables pose refinement with novel view synthesis using rendering-based optimization. Specifically, we propose a novel feature adaption module to close the gaps between the features for visual localization and neural rendering. To improve the efficacy and efficiency of neural rendering-based optimization, we also develop an efficient rendering-based framework with a warping loss function. Furthermore, several robustness techniques are developed to handle illumination changes and dynamic objects for outdoor scenarios. Experiments demonstrate that PNeRFLoc performs the best on synthetic data when the NeRF model can be well learned and performs on par with the SOTA method on the visual localization benchmark datasets.  
  </ol>  
</details>  
**comments**: Accepted to AAAI 2024  
  
### [Learning Dense Correspondence for NeRF-Based Face Reenactment](http://arxiv.org/abs/2312.10422)  
Songlin Yang, Wei Wang, Yushi Lan, Xiangyu Fan, Bo Peng, Lei Yang, Jing Dong  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Face reenactment is challenging due to the need to establish dense correspondence between various face representations for motion transfer. Recent studies have utilized Neural Radiance Field (NeRF) as fundamental representation, which further enhanced the performance of multi-view face reenactment in photo-realism and 3D consistency. However, establishing dense correspondence between different face NeRFs is non-trivial, because implicit representations lack ground-truth correspondence annotations like mesh-based 3D parametric models (e.g., 3DMM) with index-aligned vertexes. Although aligning 3DMM space with NeRF-based face representations can realize motion control, it is sub-optimal for their limited face-only modeling and low identity fidelity. Therefore, we are inspired to ask: Can we learn the dense correspondence between different NeRF-based face representations without a 3D parametric model prior? To address this challenge, we propose a novel framework, which adopts tri-planes as fundamental NeRF representation and decomposes face tri-planes into three components: canonical tri-planes, identity deformations, and motion. In terms of motion control, our key contribution is proposing a Plane Dictionary (PlaneDict) module, which efficiently maps the motion conditions to a linear weighted addition of learnable orthogonal plane bases. To the best of our knowledge, our framework is the first method that achieves one-shot multi-view face reenactment without a 3D parametric model prior. Extensive experiments demonstrate that we produce better results in fine-grained motion control and identity preservation than previous methods.  
  </ol>  
</details>  
**comments**: Accepted by Proceedings of the AAAI Conference on Artificial
  Intelligence, 2024  
  
  



