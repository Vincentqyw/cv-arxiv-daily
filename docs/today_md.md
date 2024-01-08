<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#Benchmarking-PathCLIP-for-Pathology-Image-Analysis>Benchmarking PathCLIP for Pathology Image Analysis</a></li>
      </ul>
    </li>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#CoCoT:-Contrastive-Chain-of-Thought-Prompting-for-Large-Multimodal-Models-with-Multiple-Image-Inputs>CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#Progress-and-Prospects-in-3D-Generative-AI:-A-Technical-Overview-including-3D-human>Progress and Prospects in 3D Generative AI: A Technical Overview including 3D human</a></li>
        <li><a href=#FED-NeRF:-Achieve-High-3D-Consistency-and-Temporal-Coherence-for-Face-Video-Editing-on-Dynamic-NeRF>FED-NeRF: Achieve High 3D Consistency and Temporal Coherence for Face Video Editing on Dynamic NeRF</a></li>
        <li><a href=#Characterizing-Satellite-Geometry-via-Accelerated-3D-Gaussian-Splatting>Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [Benchmarking PathCLIP for Pathology Image Analysis](http://arxiv.org/abs/2401.02651)  
Sunyi Zheng, Xiaonan Cui, Yuxuan Sun, Jingxiong Li, Honglin Li, Yunlong Zhang, Pingyi Chen, Xueping Jing, Zhaoxiang Ye, Lin Yang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Accurate image classification and retrieval are of importance for clinical diagnosis and treatment decision-making. The recent contrastive language-image pretraining (CLIP) model has shown remarkable proficiency in understanding natural images. Drawing inspiration from CLIP, PathCLIP is specifically designed for pathology image analysis, utilizing over 200,000 image and text pairs in training. While the performance the PathCLIP is impressive, its robustness under a wide range of image corruptions remains unknown. Therefore, we conduct an extensive evaluation to analyze the performance of PathCLIP on various corrupted images from the datasets of Osteosarcoma and WSSS4LUAD. In our experiments, we introduce seven corruption types including brightness, contrast, Gaussian blur, resolution, saturation, hue, and markup at four severity levels. Through experiments, we find that PathCLIP is relatively robustness to image corruptions and surpasses OpenAI-CLIP and PLIP in zero-shot classification. Among the seven corruptions, blur and resolution can cause server performance degradation of the PathCLIP. This indicates that ensuring the quality of images is crucial before conducting a clinical test. Additionally, we assess the robustness of PathCLIP in the task of image-image retrieval, revealing that PathCLIP performs less effectively than PLIP on Osteosarcoma but performs better on WSSS4LUAD under diverse corruptions. Overall, PathCLIP presents impressive zero-shot classification and retrieval performance for pathology images, but appropriate care needs to be taken when using it. We hope this study provides a qualitative impression of PathCLIP and helps understand its differences from other CLIP models.  
  </ol>  
</details>  
  
  



## Image Matching  

### [CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](http://arxiv.org/abs/2401.02582)  
Daoan Zhang, Junming Yang, Hanjia Lyu, Zijian Jin, Yuan Yao, Mingkai Chen, Jiebo Luo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    When exploring the development of Artificial General Intelligence (AGI), a critical task for these models involves interpreting and processing information from multiple image inputs. However, Large Multimodal Models (LMMs) encounter two issues in such scenarios: (1) a lack of fine-grained perception, and (2) a tendency to blend information across multiple images. We first extensively investigate the capability of LMMs to perceive fine-grained visual details when dealing with multiple input images. The research focuses on two aspects: first, image-to-image matching (to evaluate whether LMMs can effectively reason and pair relevant images), and second, multi-image-to-text matching (to assess whether LMMs can accurately capture and summarize detailed image information). We conduct evaluations on a range of both open-source and closed-source large models, including GPT-4V, Gemini, OpenFlamingo, and MMICL. To enhance model performance, we further develop a Contrastive Chain-of-Thought (CoCoT) prompting approach based on multi-input multimodal models. This method requires LMMs to compare the similarities and differences among multiple image inputs, and then guide the models to answer detailed questions about multi-image inputs based on the identified similarities and differences. Our experimental results showcase CoCoT's proficiency in enhancing the multi-image comprehension capabilities of large multimodal models.  
  </ol>  
</details>  
  
  



## NeRF  

### [Progress and Prospects in 3D Generative AI: A Technical Overview including 3D human](http://arxiv.org/abs/2401.02620)  
Song Bai, Jie Li  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    While AI-generated text and 2D images continue to expand its territory, 3D generation has gradually emerged as a trend that cannot be ignored. Since the year 2023 an abundant amount of research papers has emerged in the domain of 3D generation. This growth encompasses not just the creation of 3D objects, but also the rapid development of 3D character and motion generation. Several key factors contribute to this progress. The enhanced fidelity in stable diffusion, coupled with control methods that ensure multi-view consistency, and realistic human models like SMPL-X, contribute synergistically to the production of 3D models with remarkable consistency and near-realistic appearances. The advancements in neural network-based 3D storing and rendering models, such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), have accelerated the efficiency and realism of neural rendered models. Furthermore, the multimodality capabilities of large language models have enabled language inputs to transcend into human motion outputs. This paper aims to provide a comprehensive overview and summary of the relevant papers published mostly during the latter half year of 2023. It will begin by discussing the AI generated object models in 3D, followed by the generated 3D human models, and finally, the generated 3D human motions, culminating in a conclusive summary and a vision for the future.  
  </ol>  
</details>  
  
### [FED-NeRF: Achieve High 3D Consistency and Temporal Coherence for Face Video Editing on Dynamic NeRF](http://arxiv.org/abs/2401.02616)  
Hao Zhang, Yu-Wing Tai, Chi-Keung Tang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The success of the GAN-NeRF structure has enabled face editing on NeRF to maintain 3D view consistency. However, achieving simultaneously multi-view consistency and temporal coherence while editing video sequences remains a formidable challenge. This paper proposes a novel face video editing architecture built upon the dynamic face GAN-NeRF structure, which effectively utilizes video sequences to restore the latent code and 3D face geometry. By editing the latent code, multi-view consistent editing on the face can be ensured, as validated by multiview stereo reconstruction on the resulting edited images in our dynamic NeRF. As the estimation of face geometries occurs on a frame-by-frame basis, this may introduce a jittering issue. We propose a stabilizer that maintains temporal coherence by preserving smooth changes of face expressions in consecutive frames. Quantitative and qualitative analyses reveal that our method, as the pioneering 4D face video editor, achieves state-of-the-art performance in comparison to existing 2D or 3D-based approaches independently addressing identity and motion. Codes will be released.  
  </ol>  
</details>  
**comments**: Our code will be available at: https://github.com/ZHANG1023/FED-NeRF  
  
### [Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting](http://arxiv.org/abs/2401.02588)  
Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, Ryan T. White  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    The accelerating deployment of spacecraft in orbit have generated interest in on-orbit servicing (OOS), inspection of spacecraft, and active debris removal (ADR). Such missions require precise rendezvous and proximity operations in the vicinity of non-cooperative, possible unknown, resident space objects. Safety concerns with manned missions and lag times with ground-based control necessitate complete autonomy. This requires robust characterization of the target's geometry. In this article, we present an approach for mapping geometries of satellites on orbit based on 3D Gaussian Splatting that can run on computing resources available on current spaceflight hardware. We demonstrate model training and 3D rendering performance on a hardware-in-the-loop satellite mock-up under several realistic lighting and motion conditions. Our model is shown to be capable of training on-board and rendering higher quality novel views of an unknown satellite nearly 2 orders of magnitude faster than previous NeRF-based algorithms. Such on-board capabilities are critical to enable downstream machine intelligence tasks necessary for autonomous guidance, navigation, and control tasks.  
  </ol>  
</details>  
**comments**: 11 pages, 5 figures  
  
  



