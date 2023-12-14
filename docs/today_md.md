<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#visual-localization>Visual Localization</a></li>
      <ul>
        <li><a href=#C-BEV:-Contrastive-Bird's-Eye-View-Training-for-Cross-View-Image-Retrieval-and-3-DoF-Pose-Estimation>C-BEV: Contrastive Bird's Eye View Training for Cross-View Image Retrieval and 3-DoF Pose Estimation</a></li>
        <li><a href=#Contextually-Affinitive-Neighborhood-Refinery-for-Deep-Clustering>Contextually Affinitive Neighborhood Refinery for Deep Clustering</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#ProNeRF:-Learning-Efficient-Projection-Aware-Ray-Sampling-for-Fine-Grained-Implicit-Neural-Radiance-Fields>ProNeRF: Learning Efficient Projection-Aware Ray Sampling for Fine-Grained Implicit Neural Radiance Fields</a></li>
        <li><a href=#Neural-Radiance-Fields-for-Transparent-Object-Using-Visual-Hull>Neural Radiance Fields for Transparent Object Using Visual Hull</a></li>
        <li><a href=#uSF:-Learning-Neural-Semantic-Field-with-Uncertainty>uSF: Learning Neural Semantic Field with Uncertainty</a></li>
      </ul>
    </li>
  </ol>
</details>

## Visual Localization  

### [C-BEV: Contrastive Bird's Eye View Training for Cross-View Image Retrieval and 3-DoF Pose Estimation](http://arxiv.org/abs/2312.08060)  
Florian Fervers, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens, Rainer Stiefelhagen  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    To find the geolocation of a street-view image, cross-view geolocalization (CVGL) methods typically perform image retrieval on a database of georeferenced aerial images and determine the location from the visually most similar match. Recent approaches focus mainly on settings where street-view and aerial images are preselected to align w.r.t. translation or orientation, but struggle in challenging real-world scenarios where varying camera poses have to be matched to the same aerial image. We propose a novel trainable retrieval architecture that uses bird's eye view (BEV) maps rather than vectors as embedding representation, and explicitly addresses the many-to-one ambiguity that arises in real-world scenarios. The BEV-based retrieval is trained using the same contrastive setting and loss as classical retrieval.   Our method C-BEV surpasses the state-of-the-art on the retrieval task on multiple datasets by a large margin. It is particularly effective in challenging many-to-one scenarios, e.g. increasing the top-1 recall on VIGOR's cross-area split with unknown orientation from 31.1% to 65.0%. Although the model is supervised only through a contrastive objective applied on image pairings, it additionally learns to infer the 3-DoF camera pose on the matching aerial image, and even yields a lower mean pose error than recent methods that are explicitly trained with metric groundtruth.  
  </ol>  
</details>  
  
### [Contextually Affinitive Neighborhood Refinery for Deep Clustering](http://arxiv.org/abs/2312.07806)  
[[code](https://github.com/cly234/deepclustering-connr)]  
Chunlin Yu, Ye Shi, Jingya Wang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Previous endeavors in self-supervised learning have enlightened the research of deep clustering from an instance discrimination perspective. Built upon this foundation, recent studies further highlight the importance of grouping semantically similar instances. One effective method to achieve this is by promoting the semantic structure preserved by neighborhood consistency. However, the samples in the local neighborhood may be limited due to their close proximity to each other, which may not provide substantial and diverse supervision signals. Inspired by the versatile re-ranking methods in the context of image retrieval, we propose to employ an efficient online re-ranking process to mine more informative neighbors in a Contextually Affinitive (ConAff) Neighborhood, and then encourage the cross-view neighborhood consistency. To further mitigate the intrinsic neighborhood noises near cluster boundaries, we propose a progressively relaxed boundary filtering strategy to circumvent the issues brought by noisy neighbors. Our method can be easily integrated into the generic self-supervised frameworks and outperforms the state-of-the-art methods on several popular benchmarks.  
  </ol>  
</details>  
**comments**: Accepted to NeurIPS 2023  
  
  



## NeRF  

### [ProNeRF: Learning Efficient Projection-Aware Ray Sampling for Fine-Grained Implicit Neural Radiance Fields](http://arxiv.org/abs/2312.08136)  
Juan Luis Gonzalez Bello, Minh-Quan Viet Bui, Munchurl Kim  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Recent advances in neural rendering have shown that, albeit slow, implicit compact models can learn a scene's geometries and view-dependent appearances from multiple views. To maintain such a small memory footprint but achieve faster inference times, recent works have adopted `sampler' networks that adaptively sample a small subset of points along each ray in the implicit neural radiance fields. Although these methods achieve up to a 10 $\times$ reduction in rendering time, they still suffer from considerable quality degradation compared to the vanilla NeRF. In contrast, we propose ProNeRF, which provides an optimal trade-off between memory footprint (similar to NeRF), speed (faster than HyperReel), and quality (better than K-Planes). ProNeRF is equipped with a novel projection-aware sampling (PAS) network together with a new training strategy for ray exploration and exploitation, allowing for efficient fine-grained particle sampling. Our ProNeRF yields state-of-the-art metrics, being 15-23x faster with 0.65dB higher PSNR than NeRF and yielding 0.95dB higher PSNR than the best published sampler-based method, HyperReel. Our exploration and exploitation training strategy allows ProNeRF to learn the full scenes' color and density distributions while also learning efficient ray sampling focused on the highest-density regions. We provide extensive experimental results that support the effectiveness of our method on the widely adopted forward-facing and 360 datasets, LLFF and Blender, respectively.  
  </ol>  
</details>  
**comments**: Visit our project website at
  https://kaist-viclab.github.io/pronerf-site/  
  
### [Neural Radiance Fields for Transparent Object Using Visual Hull](http://arxiv.org/abs/2312.08118)  
Heechan Yoon, Seungkyu Lee  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Unlike opaque object, novel view synthesis of transparent object is a challenging task, because transparent object refracts light of background causing visual distortions on the transparent object surface along the viewpoint change. Recently introduced Neural Radiance Fields (NeRF) is a view synthesis method. Thanks to its remarkable performance improvement, lots of following applications based on NeRF in various topics have been developed. However, if an object with a different refractive index is included in a scene such as transparent object, NeRF shows limited performance because refracted light ray at the surface of the transparent object is not appropriately considered. To resolve the problem, we propose a NeRF-based method consisting of the following three steps: First, we reconstruct a three-dimensional shape of a transparent object using visual hull. Second, we simulate the refraction of the rays inside of the transparent object according to Snell's law. Last, we sample points through refracted rays and put them into NeRF. Experimental evaluation results demonstrate that our method addresses the limitation of conventional NeRF with transparent objects.  
  </ol>  
</details>  
  
### [uSF: Learning Neural Semantic Field with Uncertainty](http://arxiv.org/abs/2312.08012)  
[[code](https://github.com/sevashasla/usf)]  
Vsevolod Skorokhodov, Darya Drozdova, Dmitry Yudin  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Recently, there has been an increased interest in NeRF methods which reconstruct differentiable representation of three-dimensional scenes. One of the main limitations of such methods is their inability to assess the confidence of the model in its predictions. In this paper, we propose a new neural network model for the formation of extended vector representations, called uSF, which allows the model to predict not only color and semantic label of each point, but also estimate the corresponding values of uncertainty. We show that with a small number of images available for training, a model quantifying uncertainty performs better than a model without such functionality. Code of the uSF approach is publicly available at https://github.com/sevashasla/usf/.  
  </ol>  
</details>  
**comments**: 12 pages, 4 figures  
  
  



