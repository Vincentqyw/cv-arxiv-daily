<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#Learning-Robust-Generalizable-Radiance-Field-with-Visibility-and-Feature-Augmented-Point-Representation>Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation</a></li>
        <li><a href=#Sketch2NeRF:-Multi-view-Sketch-guided-Text-to-3D-Generation>Sketch2NeRF: Multi-view Sketch-guided Text-to-3D Generation</a></li>
      </ul>
    </li>
  </ol>
</details>

## NeRF  

### [Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation](http://arxiv.org/abs/2401.14354)  
Jiaxu Wang, Ziyi Zhang, Renjing Xu  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper introduces a novel paradigm for the generalizable neural radiance field (NeRF). Previous generic NeRF methods combine multiview stereo techniques with image-based neural rendering for generalization, yielding impressive results, while suffering from three issues. First, occlusions often result in inconsistent feature matching. Then, they deliver distortions and artifacts in geometric discontinuities and locally sharp shapes due to their individual process of sampled points and rough feature aggregation. Third, their image-based representations experience severe degradations when source views are not near enough to the target view. To address challenges, we propose the first paradigm that constructs the generalizable neural field based on point-based rather than image-based rendering, which we call the Generalizable neural Point Field (GPF). Our approach explicitly models visibilities by geometric priors and augments them with neural features. We propose a novel nonuniform log sampling strategy to improve both rendering speed and reconstruction quality. Moreover, we present a learnable kernel spatially augmented with features for feature aggregations, mitigating distortions at places with drastically varying geometries. Besides, our representation can be easily manipulated. Experiments show that our model can deliver better geometries, view consistencies, and rendering quality than all counterparts and benchmarks on three datasets in both generalization and finetuning settings, preliminarily proving the potential of the new paradigm for generalizable NeRF.  
  </ol>  
</details>  
**comments**: International Conference on Learning Representations 2024  
  
### [Sketch2NeRF: Multi-view Sketch-guided Text-to-3D Generation](http://arxiv.org/abs/2401.14257)  
Minglin Chen, Longguang Wang, Weihao Yuan, Yukun Wang, Zhe Sheng, Yisheng He, Zilong Dong, Liefeng Bo, Yulan Guo  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Recently, text-to-3D approaches have achieved high-fidelity 3D content generation using text description. However, the generated objects are stochastic and lack fine-grained control. Sketches provide a cheap approach to introduce such fine-grained control. Nevertheless, it is challenging to achieve flexible control from these sketches due to their abstraction and ambiguity. In this paper, we present a multi-view sketch-guided text-to-3D generation framework (namely, Sketch2NeRF) to add sketch control to 3D generation. Specifically, our method leverages pretrained 2D diffusion models (e.g., Stable Diffusion and ControlNet) to supervise the optimization of a 3D scene represented by a neural radiance field (NeRF). We propose a novel synchronized generation and reconstruction method to effectively optimize the NeRF. In the experiments, we collected two kinds of multi-view sketch datasets to evaluate the proposed method. We demonstrate that our method can synthesize 3D consistent contents with fine-grained sketch control while being high-fidelity to text prompts. Extensive results show that our method achieves state-of-the-art performance in terms of sketch similarity and text alignment.  
  </ol>  
</details>  
**comments**: 11 pages, 9 figures  
  
  



