<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#Informative-Rays-Selection-for-Few-Shot-Neural-Radiance-Fields>Informative Rays Selection for Few-Shot Neural Radiance Fields</a></li>
      </ul>
    </li>
  </ol>
</details>

## NeRF  

### [Informative Rays Selection for Few-Shot Neural Radiance Fields](http://arxiv.org/abs/2312.17561)  
Marco Orsingher, Anthony Dell'Eva, Paolo Zani, Paolo Medici, Massimo Bertozzi  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Fields (NeRF) have recently emerged as a powerful method for image-based 3D reconstruction, but the lengthy per-scene optimization limits their practical usage, especially in resource-constrained settings. Existing approaches solve this issue by reducing the number of input views and regularizing the learned volumetric representation with either complex losses or additional inputs from other modalities. In this paper, we present KeyNeRF, a simple yet effective method for training NeRF in few-shot scenarios by focusing on key informative rays. Such rays are first selected at camera level by a view selection algorithm that promotes baseline diversity while guaranteeing scene coverage, then at pixel level by sampling from a probability distribution based on local image entropy. Our approach performs favorably against state-of-the-art methods, while requiring minimal changes to existing NeRF codebases.  
  </ol>  
</details>  
**comments**: To appear at VISAPP 2024  
  
  



