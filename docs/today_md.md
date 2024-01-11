<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#image-matching>Image Matching</a></li>
      <ul>
        <li><a href=#RomniStereo:-Recurrent-Omnidirectional-Stereo-Matching>RomniStereo: Recurrent Omnidirectional Stereo Matching</a></li>
      </ul>
    </li>
  </ol>
</details>

## Image Matching  

### [RomniStereo: Recurrent Omnidirectional Stereo Matching](http://arxiv.org/abs/2401.04345)  
[[code](https://github.com/halleyjiang/romnistereo)]  
Hualie Jiang, Rui Xu, Minglang Tan, Wenjie Jiang  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Omnidirectional stereo matching (OSM) is an essential and reliable means for $360^{\circ}$ depth sensing. However, following earlier works on conventional stereo matching, prior state-of-the-art (SOTA) methods rely on a 3D encoder-decoder block to regularize the cost volume, causing the whole system complicated and sub-optimal results. Recently, the Recurrent All-pairs Field Transforms (RAFT) based approach employs the recurrent update in 2D and has efficiently improved image-matching tasks, \ie, optical flow, and stereo matching. To bridge the gap between OSM and RAFT, we mainly propose an opposite adaptive weighting scheme to seamlessly transform the outputs of spherical sweeping of OSM into the required inputs for the recurrent update, thus creating a recurrent omnidirectional stereo matching (RomniStereo) algorithm. Furthermore, we introduce two techniques, \ie, grid embedding and adaptive context feature generation, which also contribute to RomniStereo's performance. Our best model improves the average MAE metric by 40.7\% over the previous SOTA baseline across five datasets. When visualizing the results, our models demonstrate clear advantages on both synthetic and realistic examples. The code is available at \url{https://github.com/HalleyJiang/RomniStereo}.  
  </ol>  
</details>  
**comments**: accepted by IEEE RA-L, https://github.com/HalleyJiang/RomniStereo  
  
  



