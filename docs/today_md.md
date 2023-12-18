<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#slam>SLAM</a></li>
      <ul>
        <li><a href=#Deep-Event-Visual-Odometry>Deep Event Visual Odometry</a></li>
      </ul>
    </li>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Let-All-be-Whitened:-Multi-teacher-Distillation-for-Efficient-Visual-Retrieval>Let All be Whitened: Multi-teacher Distillation for Efficient Visual Retrieval</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#SlimmeRF:-Slimmable-Radiance-Fields>SlimmeRF: Slimmable Radiance Fields</a></li>
        <li><a href=#LAENeRF:-Local-Appearance-Editing-for-Neural-Radiance-Fields>LAENeRF: Local Appearance Editing for Neural Radiance Fields</a></li>
        <li><a href=#SLS4D:-Sparse-Latent-Space-for-4D-Novel-View-Synthesis>SLS4D: Sparse Latent Space for 4D Novel View Synthesis</a></li>
        <li><a href=#Towards-Transferable-Targeted-3D-Adversarial-Attack-in-the-Physical-World>Towards Transferable Targeted 3D Adversarial Attack in the Physical World</a></li>
        <li><a href=#LatentEditor:-Text-Driven-Local-Editing-of-3D-Scenes>LatentEditor: Text Driven Local Editing of 3D Scenes</a></li>
        <li><a href=#Stable-Score-Distillation-for-High-Quality-3D-Generation>Stable Score Distillation for High-Quality 3D Generation</a></li>
      </ul>
    </li>
  </ol>
</details>

## SLAM  

### [Deep Event Visual Odometry](http://arxiv.org/abs/2312.09800)  
Simon Klenk, Marvin Motzet, Lukas Koestler, Daniel Cremers  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Event cameras offer the exciting possibility of tracking the camera's pose during high-speed motion and in adverse lighting conditions. Despite this promise, existing event-based monocular visual odometry (VO) approaches demonstrate limited performance on recent benchmarks. To address this limitation, some methods resort to additional sensors such as IMUs, stereo event cameras, or frame-based cameras. Nonetheless, these additional sensors limit the application of event cameras in real-world devices since they increase cost and complicate system requirements. Moreover, relying on a frame-based camera makes the system susceptible to motion blur and HDR. To remove the dependency on additional sensors and to push the limits of using only a single event camera, we present Deep Event VO (DEVO), the first monocular event-only system with strong performance on a large number of real-world benchmarks. DEVO sparsely tracks selected event patches over time. A key component of DEVO is a novel deep patch selection mechanism tailored to event data. We significantly decrease the pose tracking error on seven real-world benchmarks by up to 97% compared to event-only methods and often surpass or are close to stereo or inertial methods. Code is available at https://github.com/tum-vision/DEVO  
  </ol>  
</details>  
**comments**: Accepted by 3DV 2024  
  
  



## Visual Localization  

### [Let All be Whitened: Multi-teacher Distillation for Efficient Visual Retrieval](http://arxiv.org/abs/2312.09716)  
[[code](https://github.com/maryeon/whiten_mtd)]  
Zhe Ma, Jianfeng Dong, Shouling Ji, Zhenguang Liu, Xuhong Zhang, Zonghui Wang, Sifeng He, Feng Qian, Xiaobo Zhang, Lei Yang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Visual retrieval aims to search for the most relevant visual items, e.g., images and videos, from a candidate gallery with a given query item. Accuracy and efficiency are two competing objectives in retrieval tasks. Instead of crafting a new method pursuing further improvement on accuracy, in this paper we propose a multi-teacher distillation framework Whiten-MTD, which is able to transfer knowledge from off-the-shelf pre-trained retrieval models to a lightweight student model for efficient visual retrieval. Furthermore, we discover that the similarities obtained by different retrieval models are diversified and incommensurable, which makes it challenging to jointly distill knowledge from multiple models. Therefore, we propose to whiten the output of teacher models before fusion, which enables effective multi-teacher distillation for retrieval models. Whiten-MTD is conceptually simple and practically effective. Extensive experiments on two landmark image retrieval datasets and one video retrieval dataset demonstrate the effectiveness of our proposed method, and its good balance of retrieval performance and efficiency. Our source code is released at https://github.com/Maryeon/whiten_mtd.  
  </ol>  
</details>  
**comments**: Accepted by AAAI 2024  
  
  



## NeRF  

### [SlimmeRF: Slimmable Radiance Fields](http://arxiv.org/abs/2312.10034)  
[[code](https://github.com/shiran-yuan/slimmerf)]  
Shiran Yuan, Hao Zhao  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Field (NeRF) and its variants have recently emerged as successful methods for novel view synthesis and 3D scene reconstruction. However, most current NeRF models either achieve high accuracy using large model sizes, or achieve high memory-efficiency by trading off accuracy. This limits the applicable scope of any single model, since high-accuracy models might not fit in low-memory devices, and memory-efficient models might not satisfy high-quality requirements. To this end, we present SlimmeRF, a model that allows for instant test-time trade-offs between model size and accuracy through slimming, thus making the model simultaneously suitable for scenarios with different computing budgets. We achieve this through a newly proposed algorithm named Tensorial Rank Incrementation (TRaIn) which increases the rank of the model's tensorial representation gradually during training. We also observe that our model allows for more effective trade-offs in sparse-view scenarios, at times even achieving higher accuracy after being slimmed. We credit this to the fact that erroneous information such as floaters tend to be stored in components corresponding to higher ranks. Our implementation is available at https://github.com/Shiran-Yuan/SlimmeRF.  
  </ol>  
</details>  
**comments**: 3DV 2024 Oral, Project Page: https://shiran-yuan.github.io/SlimmeRF/,
  Code: https://github.com/Shiran-Yuan/SlimmeRF/  
  
### [LAENeRF: Local Appearance Editing for Neural Radiance Fields](http://arxiv.org/abs/2312.09913)  
Lukas Radl, Michael Steiner, Andreas Kurz, Markus Steinberger  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Due to the omnipresence of Neural Radiance Fields (NeRFs), the interest towards editable implicit 3D representations has surged over the last years. However, editing implicit or hybrid representations as used for NeRFs is difficult due to the entanglement of appearance and geometry encoded in the model parameters. Despite these challenges, recent research has shown first promising steps towards photorealistic and non-photorealistic appearance edits. The main open issues of related work include limited interactivity, a lack of support for local edits and large memory requirements, rendering them less useful in practice. We address these limitations with LAENeRF, a unified framework for photorealistic and non-photorealistic appearance editing of NeRFs. To tackle local editing, we leverage a voxel grid as starting point for region selection. We learn a mapping from expected ray terminations to final output color, which can optionally be supervised by a style loss, resulting in a framework which can perform photorealistic and non-photorealistic appearance editing of selected regions. Relying on a single point per ray for our mapping, we limit memory requirements and enable fast optimization. To guarantee interactivity, we compose the output color using a set of learned, modifiable base colors, composed with additive layer mixing. Compared to concurrent work, LAENeRF enables recoloring and stylization while keeping processing time low. Furthermore, we demonstrate that our approach surpasses baseline methods both quantitatively and qualitatively.  
  </ol>  
</details>  
**comments**: Project website: https://r4dl.github.io/LAENeRF/  
  
### [SLS4D: Sparse Latent Space for 4D Novel View Synthesis](http://arxiv.org/abs/2312.09743)  
Qi-Yuan Feng, Hao-Xiang Chen, Qun-Ce Xu, Tai-Jiang Mu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural radiance field (NeRF) has achieved great success in novel view synthesis and 3D representation for static scenarios. Existing dynamic NeRFs usually exploit a locally dense grid to fit the deformation field; however, they fail to capture the global dynamics and concomitantly yield models of heavy parameters. We observe that the 4D space is inherently sparse. Firstly, the deformation field is sparse in spatial but dense in temporal due to the continuity of of motion. Secondly, the radiance field is only valid on the surface of the underlying scene, usually occupying a small fraction of the whole space. We thus propose to represent the 4D scene using a learnable sparse latent space, a.k.a. SLS4D. Specifically, SLS4D first uses dense learnable time slot features to depict the temporal space, from which the deformation field is fitted with linear multi-layer perceptions (MLP) to predict the displacement of a 3D position at any time. It then learns the spatial features of a 3D position using another sparse latent space. This is achieved by learning the adaptive weights of each latent code with the attention mechanism. Extensive experiments demonstrate the effectiveness of our SLS4D: it achieves the best 4D novel view synthesis using only about $6\%$ parameters of the most recent work.  
  </ol>  
</details>  
**comments**: 10 pages, 6 figures  
  
### [Towards Transferable Targeted 3D Adversarial Attack in the Physical World](http://arxiv.org/abs/2312.09558)  
Yao Huang, Yinpeng Dong, Shouwei Ruan, Xiao Yang, Hang Su, Xingxing Wei  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Compared with transferable untargeted attacks, transferable targeted adversarial attacks could specify the misclassification categories of adversarial samples, posing a greater threat to security-critical tasks. In the meanwhile, 3D adversarial samples, due to their potential of multi-view robustness, can more comprehensively identify weaknesses in existing deep learning systems, possessing great application value. However, the field of transferable targeted 3D adversarial attacks remains vacant. The goal of this work is to develop a more effective technique that could generate transferable targeted 3D adversarial examples, filling the gap in this field. To achieve this goal, we design a novel framework named TT3D that could rapidly reconstruct from few multi-view images into Transferable Targeted 3D textured meshes. While existing mesh-based texture optimization methods compute gradients in the high-dimensional mesh space and easily fall into local optima, leading to unsatisfactory transferability and distinct distortions, TT3D innovatively performs dual optimization towards both feature grid and Multi-layer Perceptron (MLP) parameters in the grid-based NeRF space, which significantly enhances black-box transferability while enjoying naturalness. Experimental results show that TT3D not only exhibits superior cross-model transferability but also maintains considerable adaptability across different renders and vision tasks. More importantly, we produce 3D adversarial examples with 3D printing techniques in the real world and verify their robust performance under various scenarios.  
  </ol>  
</details>  
**comments**: 11 pages, 7 figures  
  
### [LatentEditor: Text Driven Local Editing of 3D Scenes](http://arxiv.org/abs/2312.09313)  
[[code](https://github.com/umarkhalidAI/LatentEditor)]  
Umar Khalid, Hasan Iqbal, Nazmul Karim, Jing Hua, Chen Chen  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    While neural fields have made significant strides in view synthesis and scene reconstruction, editing them poses a formidable challenge due to their implicit encoding of geometry and texture information from multi-view inputs. In this paper, we introduce \textsc{LatentEditor}, an innovative framework designed to empower users with the ability to perform precise and locally controlled editing of neural fields using text prompts. Leveraging denoising diffusion models, we successfully embed real-world scenes into the latent space, resulting in a faster and more adaptable NeRF backbone for editing compared to traditional methods. To enhance editing precision, we introduce a delta score to calculate the 2D mask in the latent space that serves as a guide for local modifications while preserving irrelevant regions. Our novel pixel-level scoring approach harnesses the power of InstructPix2Pix (IP2P) to discern the disparity between IP2P conditional and unconditional noise predictions in the latent space. The edited latents conditioned on the 2D masks are then iteratively updated in the training set to achieve 3D local editing. Our approach achieves faster editing speeds and superior output quality compared to existing 3D editing models, bridging the gap between textual instructions and high-quality 3D scene editing in latent space. We show the superiority of our approach on four benchmark 3D datasets, LLFF, IN2N, NeRFStudio and NeRF-Art.  
  </ol>  
</details>  
**comments**: Project Page: https://latenteditor.github.io/  
  
### [Stable Score Distillation for High-Quality 3D Generation](http://arxiv.org/abs/2312.09305)  
Boshi Tang, Jianan Wang, Zhiyong Wu, Lei Zhang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Score Distillation Sampling (SDS) has exhibited remarkable performance in conditional 3D content generation. However, a comprehensive understanding of the SDS formulation is still lacking, hindering the development of 3D generation. In this work, we present an interpretation of SDS as a combination of three functional components: mode-disengaging, mode-seeking and variance-reducing terms, and analyze the properties of each. We show that problems such as over-smoothness and color-saturation result from the intrinsic deficiency of the supervision terms and reveal that the variance-reducing term introduced by SDS is sub-optimal. Additionally, we shed light on the adoption of large Classifier-Free Guidance (CFG) scale for 3D generation. Based on the analysis, we propose a simple yet effective approach named Stable Score Distillation (SSD) which strategically orchestrates each term for high-quality 3D generation. Extensive experiments validate the efficacy of our approach, demonstrating its ability to generate high-fidelity 3D content without succumbing to issues such as over-smoothness and over-saturation, even under low CFG conditions with the most challenging NeRF representation.  
  </ol>  
</details>  
  
  



