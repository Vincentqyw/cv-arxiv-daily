<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#VQA4CIR:-Boosting-Composed-Image-Retrieval-with-Visual-Question-Answering>VQA4CIR: Boosting Composed Image Retrieval with Visual Question Answering</a></li>
        <li><a href=#Advancing-Image-Retrieval-with-Few-Shot-Learning-and-Relevance-Feedback>Advancing Image Retrieval with Few-Shot Learning and Relevance Feedback</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#An-effective-image-copy-move-forgery-detection-using-entropy-image>An effective image copy-move forgery detection using entropy image</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#MatchDet:-A-Collaborative-Framework-for-Image-Matching-and-Object-Detection>MatchDet: A Collaborative Framework for Image Matching and Object Detection</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#ZS-SRT:-An-Efficient-Zero-Shot-Super-Resolution-Training-Method-for-Neural-Radiance-Fields>ZS-SRT: An Efficient Zero-Shot Super-Resolution Training Method for Neural Radiance Fields</a></li>
        <li><a href=#LHManip:-A-Dataset-for-Long-Horizon-Language-Grounded-Manipulation-Tasks-in-Cluttered-Tabletop-Environments>LHManip: A Dataset for Long-Horizon Language-Grounded Manipulation Tasks in Cluttered Tabletop Environments</a></li>
        <li><a href=#MixRT:-Mixed-Neural-Representations-For-Real-Time-NeRF-Rendering>MixRT: Mixed Neural Representations For Real-Time NeRF Rendering</a></li>
        <li><a href=#Text-Image-Conditioned-Diffusion-for-Consistent-Text-to-3D-Generation>Text-Image Conditioned Diffusion for Consistent Text-to-3D Generation</a></li>
        <li><a href=#GAvatar:-Animatable-3D-Gaussian-Avatars-with-Implicit-Mesh-Learning>GAvatar: Animatable 3D Gaussian Avatars with Implicit Mesh Learning</a></li>
        <li><a href=#AE-NeRF:-Audio-Enhanced-Neural-Radiance-Field-for-Few-Shot-Talking-Head-Synthesis>AE-NeRF: Audio Enhanced Neural Radiance Field for Few Shot Talking Head Synthesis</a></li>
        <li><a href=#FastSR-NeRF:-Improving-NeRF-Efficiency-on-Consumer-Devices-with-A-Simple-Super-Resolution-Pipeline>FastSR-NeRF: Improving NeRF Efficiency on Consumer Devices with A Simple Super-Resolution Pipeline</a></li>
        <li><a href=#Customize-It-3D:-High-Quality-3D-Creation-from-A-Single-Image-Using-Subject-Specific-Knowledge-Prior>Customize-It-3D: High-Quality 3D Creation from A Single Image Using Subject-Specific Knowledge Prior</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [VQA4CIR: Boosting Composed Image Retrieval with Visual Question Answering](http://arxiv.org/abs/2312.12273)  
Chun-Mei Feng, Yang Bai, Tao Luo, Zhen Li, Salman Khan, Wangmeng Zuo, Xinxing Xu, Rick Siow Mong Goh, Yong Liu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Albeit progress has been made in Composed Image Retrieval (CIR), we empirically find that a certain percentage of failure retrieval results are not consistent with their relative captions. To address this issue, this work provides a Visual Question Answering (VQA) perspective to boost the performance of CIR. The resulting VQA4CIR is a post-processing approach and can be directly plugged into existing CIR methods. Given the top-C retrieved images by a CIR method, VQA4CIR aims to decrease the adverse effect of the failure retrieval results being inconsistent with the relative caption. To find the retrieved images inconsistent with the relative caption, we resort to the "QA generation to VQA" self-verification pipeline. For QA generation, we suggest fine-tuning LLM (e.g., LLaMA) to generate several pairs of questions and answers from each relative caption. We then fine-tune LVLM (e.g., LLaVA) to obtain the VQA model. By feeding the retrieved image and question to the VQA model, one can find the images inconsistent with relative caption when the answer by VQA is inconsistent with the answer in the QA pair. Consequently, the CIR performance can be boosted by modifying the ranks of inconsistently retrieved images. Experimental results show that our proposed method outperforms state-of-the-art CIR methods on the CIRR and Fashion-IQ datasets.  
  </ol>  
</details>  
  
### [Advancing Image Retrieval with Few-Shot Learning and Relevance Feedback](http://arxiv.org/abs/2312.11078)  
Boaz Lerner, Nir Darshan, Rami Ben-Ari  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    With such a massive growth in the number of images stored, efficient search in a database has become a crucial endeavor managed by image retrieval systems. Image Retrieval with Relevance Feedback (IRRF) involves iterative human interaction during the retrieval process, yielding more meaningful outcomes. This process can be generally cast as a binary classification problem with only {\it few} labeled samples derived from user feedback. The IRRF task frames a unique few-shot learning characteristics including binary classification of imbalanced and asymmetric classes, all in an open-set regime. In this paper, we study this task through the lens of few-shot learning methods. We propose a new scheme based on a hyper-network, that is tailored to the task and facilitates swift adjustment to user feedback. Our approach's efficacy is validated through comprehensive evaluations on multiple benchmarks and two supplementary tasks, supported by theoretical analysis. We demonstrate the advantage of our model over strong baselines on 4 different datasets in IRRF, addressing also retrieval of images with multiple objects. Furthermore, we show that our method can attain SoTA results in few-shot one-class classification and reach comparable results in binary classification task of few-shot open-set recognition.  
  </ol>  
</details>  
**comments**: A short version of this paper was presented in ICCV-Out Of
  Distribution Generalization on Computer Vision (OOD-CV) Workshop 2023. See
  also
  https://github.com/eccv22-ood-workshop/eccv22-ood-workshop.github.io/blob/new/camera_ready/CameraReady%2053.pdf  
  
  



## Keypoint Detection  

### [An effective image copy-move forgery detection using entropy image](http://arxiv.org/abs/2312.11793)  
Zhaowei Lu, Li Jiang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Image forensics has become increasingly important in our daily lives. As a fundamental type of forgeries, Copy-Move Forgery Detection (CMFD) has received significant attention in the academic community. Keypoint-based algorithms, particularly those based on SIFT, have achieved good results in CMFD. However, the most of keypoint detection algorithms often fail to generate sufficient matches when tampered patches are present in smooth areas. To tackle this problem, we introduce entropy images to determine the coordinates and scales of keypoints, resulting significantly increasing the number of keypoints. Furthermore, we develop an entropy level clustering algorithm to avoid increased matching complexity caused by non-ideal distribution of grayscale values in keypoints. Experimental results demonstrate that our algorithm achieves a good balance between performance and time efficiency.  
  </ol>  
</details>  
  
  



## Image Matching  

### [MatchDet: A Collaborative Framework for Image Matching and Object Detection](http://arxiv.org/abs/2312.10983)  
Jinxiang Lai, Wenlong Wu, Bin-Bin Gao, Jun Liu, Jiawei Zhan, Congchong Nie, Yi Zeng, Chengjie Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Image matching and object detection are two fundamental and challenging tasks, while many related applications consider them two individual tasks (i.e. task-individual). In this paper, a collaborative framework called MatchDet (i.e. task-collaborative) is proposed for image matching and object detection to obtain mutual improvements. To achieve the collaborative learning of the two tasks, we propose three novel modules, including a Weighted Spatial Attention Module (WSAM) for Detector, and Weighted Attention Module (WAM) and Box Filter for Matcher. Specifically, the WSAM highlights the foreground regions of target image to benefit the subsequent detector, the WAM enhances the connection between the foreground regions of pair images to ensure high-quality matches, and Box Filter mitigates the impact of false matches. We evaluate the approaches on a new benchmark with two datasets called Warp-COCO and miniScanNet. Experimental results show our approaches are effective and achieve competitive improvements.  
  </ol>  
</details>  
  
  



## NeRF  

### [ZS-SRT: An Efficient Zero-Shot Super-Resolution Training Method for Neural Radiance Fields](http://arxiv.org/abs/2312.12122)  
Xiang Feng, Yongbo He, Yubo Wang, Chengkai Wang, Zhenzhong Kuang, Jiajun Ding, Feiwei Qin, Jun Yu, Jianping Fan  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Fields (NeRF) have achieved great success in the task of synthesizing novel views that preserve the same resolution as the training views. However, it is challenging for NeRF to synthesize high-quality high-resolution novel views with low-resolution training data. To solve this problem, we propose a zero-shot super-resolution training framework for NeRF. This framework aims to guide the NeRF model to synthesize high-resolution novel views via single-scene internal learning rather than requiring any external high-resolution training data. Our approach consists of two stages. First, we learn a scene-specific degradation mapping by performing internal learning on a pretrained low-resolution coarse NeRF. Second, we optimize a super-resolution fine NeRF by conducting inverse rendering with our mapping function so as to backpropagate the gradients from low-resolution 2D space into the super-resolution 3D sampling space. Then, we further introduce a temporal ensemble strategy in the inference phase to compensate for the scene estimation errors. Our method is featured on two points: (1) it does not consume high-resolution views or additional scene data to train super-resolution NeRF; (2) it can speed up the training process by adopting a coarse-to-fine strategy. By conducting extensive experiments on public datasets, we have qualitatively and quantitatively demonstrated the effectiveness of our method.  
  </ol>  
</details>  
  
### [LHManip: A Dataset for Long-Horizon Language-Grounded Manipulation Tasks in Cluttered Tabletop Environments](http://arxiv.org/abs/2312.12036)  
[[code](https://github.com/fedeceola/lhmanip)]  
Federico Ceola, Lorenzo Natale, Niko Sünderhauf, Krishan Rana  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Instructing a robot to complete an everyday task within our homes has been a long-standing challenge for robotics. While recent progress in language-conditioned imitation learning and offline reinforcement learning has demonstrated impressive performance across a wide range of tasks, they are typically limited to short-horizon tasks -- not reflective of those a home robot would be expected to complete. While existing architectures have the potential to learn these desired behaviours, the lack of the necessary long-horizon, multi-step datasets for real robotic systems poses a significant challenge. To this end, we present the Long-Horizon Manipulation (LHManip) dataset comprising 200 episodes, demonstrating 20 different manipulation tasks via real robot teleoperation. The tasks entail multiple sub-tasks, including grasping, pushing, stacking and throwing objects in highly cluttered environments. Each task is paired with a natural language instruction and multi-camera viewpoints for point-cloud or NeRF reconstruction. In total, the dataset comprises 176,278 observation-action pairs which form part of the Open X-Embodiment dataset. The full LHManip dataset is made publicly available \href{https://github.com/fedeceola/LHManip}{here}.  
  </ol>  
</details>  
**comments**: Submitted to IJRR  
  
### [MixRT: Mixed Neural Representations For Real-Time NeRF Rendering](http://arxiv.org/abs/2312.11841)  
Chaojian Li, Bichen Wu, Peter Vajda, Yingyan, Lin  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Field (NeRF) has emerged as a leading technique for novel view synthesis, owing to its impressive photorealistic reconstruction and rendering capability. Nevertheless, achieving real-time NeRF rendering in large-scale scenes has presented challenges, often leading to the adoption of either intricate baked mesh representations with a substantial number of triangles or resource-intensive ray marching in baked representations. We challenge these conventions, observing that high-quality geometry, represented by meshes with substantial triangles, is not necessary for achieving photorealistic rendering quality. Consequently, we propose MixRT, a novel NeRF representation that includes a low-quality mesh, a view-dependent displacement map, and a compressed NeRF model. This design effectively harnesses the capabilities of existing graphics hardware, thus enabling real-time NeRF rendering on edge devices. Leveraging a highly-optimized WebGL-based rendering framework, our proposed MixRT attains real-time rendering speeds on edge devices (over 30 FPS at a resolution of 1280 x 720 on a MacBook M1 Pro laptop), better rendering quality (0.2 PSNR higher in indoor scenes of the Unbounded-360 datasets), and a smaller storage size (less than 80% compared to state-of-the-art methods).  
  </ol>  
</details>  
**comments**: Accepted by 3DV'24. Project Page: https://licj15.github.io/MixRT/  
  
### [Text-Image Conditioned Diffusion for Consistent Text-to-3D Generation](http://arxiv.org/abs/2312.11774)  
Yuze He, Yushi Bai, Matthieu Lin, Jenny Sheng, Yubin Hu, Qi Wang, Yu-Hui Wen, Yong-Jin Liu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    By lifting the pre-trained 2D diffusion models into Neural Radiance Fields (NeRFs), text-to-3D generation methods have made great progress. Many state-of-the-art approaches usually apply score distillation sampling (SDS) to optimize the NeRF representations, which supervises the NeRF optimization with pre-trained text-conditioned 2D diffusion models such as Imagen. However, the supervision signal provided by such pre-trained diffusion models only depends on text prompts and does not constrain the multi-view consistency. To inject the cross-view consistency into diffusion priors, some recent works finetune the 2D diffusion model with multi-view data, but still lack fine-grained view coherence. To tackle this challenge, we incorporate multi-view image conditions into the supervision signal of NeRF optimization, which explicitly enforces fine-grained view consistency. With such stronger supervision, our proposed text-to-3D method effectively mitigates the generation of floaters (due to excessive densities) and completely empty spaces (due to insufficient densities). Our quantitative evaluations on the T $^3$ Bench dataset demonstrate that our method achieves state-of-the-art performance over existing text-to-3D methods. We will make the code publicly available.  
  </ol>  
</details>  
  
### [FastSR-NeRF: Improving NeRF Efficiency on Consumer Devices with A Simple Super-Resolution Pipeline](http://arxiv.org/abs/2312.11537)  
Chien-Yu Lin, Qichen Fu, Thomas Merth, Karren Yang, Anurag Ranjan  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Super-resolution (SR) techniques have recently been proposed to upscale the outputs of neural radiance fields (NeRF) and generate high-quality images with enhanced inference speeds. However, existing NeRF+SR methods increase training overhead by using extra input features, loss functions, and/or expensive training procedures such as knowledge distillation. In this paper, we aim to leverage SR for efficiency gains without costly training or architectural changes. Specifically, we build a simple NeRF+SR pipeline that directly combines existing modules, and we propose a lightweight augmentation technique, random patch sampling, for training. Compared to existing NeRF+SR methods, our pipeline mitigates the SR computing overhead and can be trained up to 23x faster, making it feasible to run on consumer devices such as the Apple MacBook. Experiments show our pipeline can upscale NeRF outputs by 2-4x while maintaining high quality, increasing inference speeds by up to 18x on an NVIDIA V100 GPU and 12.8x on an M1 Pro chip. We conclude that SR can be a simple but effective technique for improving the efficiency of NeRF models for consumer devices.  
  </ol>  
</details>  
**comments**: WACV 2024 (Oral)  
  
### [Customize-It-3D: High-Quality 3D Creation from A Single Image Using Subject-Specific Knowledge Prior](http://arxiv.org/abs/2312.11535)  
Nan Huang, Ting Zhang, Yuhui Yuan, Dong Chen, Shanghang Zhang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    In this paper, we present a novel two-stage approach that fully utilizes the information provided by the reference image to establish a customized knowledge prior for image-to-3D generation. While previous approaches primarily rely on a general diffusion prior, which struggles to yield consistent results with the reference image, we propose a subject-specific and multi-modal diffusion model. This model not only aids NeRF optimization by considering the shading mode for improved geometry but also enhances texture from the coarse results to achieve superior refinement. Both aspects contribute to faithfully aligning the 3D content with the subject. Extensive experiments showcase the superiority of our method, Customize-It-3D, outperforming previous works by a substantial margin. It produces faithful 360-degree reconstructions with impressive visual quality, making it well-suited for various applications, including text-to-3D creation.  
  </ol>  
</details>  
**comments**: Project Page: https://nnanhuang.github.io/projects/customize-it-3d/  
  
### [GAvatar: Animatable 3D Gaussian Avatars with Implicit Mesh Learning](http://arxiv.org/abs/2312.11461)  
Ye Yuan, Xueting Li, Yangyi Huang, Shalini De Mello, Koki Nagano, Jan Kautz, Umar Iqbal  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Gaussian splatting has emerged as a powerful 3D representation that harnesses the advantages of both explicit (mesh) and implicit (NeRF) 3D representations. In this paper, we seek to leverage Gaussian splatting to generate realistic animatable avatars from textual descriptions, addressing the limitations (e.g., flexibility and efficiency) imposed by mesh or NeRF-based representations. However, a naive application of Gaussian splatting cannot generate high-quality animatable avatars and suffers from learning instability; it also cannot capture fine avatar geometries and often leads to degenerate body parts. To tackle these problems, we first propose a primitive-based 3D Gaussian representation where Gaussians are defined inside pose-driven primitives to facilitate animation. Second, to stabilize and amortize the learning of millions of Gaussians, we propose to use neural implicit fields to predict the Gaussian attributes (e.g., colors). Finally, to capture fine avatar geometries and extract detailed meshes, we propose a novel SDF-based implicit mesh learning approach for 3D Gaussians that regularizes the underlying geometries and extracts highly detailed textured meshes. Our proposed method, GAvatar, enables the large-scale generation of diverse animatable avatars using only text prompts. GAvatar significantly surpasses existing methods in terms of both appearance and geometry quality, and achieves extremely fast rendering (100 fps) at 1K resolution.  
  </ol>  
</details>  
**comments**: Project website: https://nvlabs.github.io/GAvatar  
  
### [AE-NeRF: Audio Enhanced Neural Radiance Field for Few Shot Talking Head Synthesis](http://arxiv.org/abs/2312.10921)  
Dongze Li, Kang Zhao, Wei Wang, Bo Peng, Yingya Zhang, Jing Dong, Tieniu Tan  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Audio-driven talking head synthesis is a promising topic with wide applications in digital human, film making and virtual reality. Recent NeRF-based approaches have shown superiority in quality and fidelity compared to previous studies. However, when it comes to few-shot talking head generation, a practical scenario where only few seconds of talking video is available for one identity, two limitations emerge: 1) they either have no base model, which serves as a facial prior for fast convergence, or ignore the importance of audio when building the prior; 2) most of them overlook the degree of correlation between different face regions and audio, e.g., mouth is audio related, while ear is audio independent. In this paper, we present Audio Enhanced Neural Radiance Field (AE-NeRF) to tackle the above issues, which can generate realistic portraits of a new speaker with fewshot dataset. Specifically, we introduce an Audio Aware Aggregation module into the feature fusion stage of the reference scheme, where the weight is determined by the similarity of audio between reference and target image. Then, an Audio-Aligned Face Generation strategy is proposed to model the audio related and audio independent regions respectively, with a dual-NeRF framework. Extensive experiments have shown AE-NeRF surpasses the state-of-the-art on image fidelity, audio-lip synchronization, and generalization ability, even in limited training set or training iterations.  
  </ol>  
</details>  
**comments**: Accepted by AAAI 2024  
  
  



