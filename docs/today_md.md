<details>
  <summary><b>TOC</b></summary>
  <ol>
    <li><a href=#slam>SLAM</a></li>
      <ul>
        <li><a href=#Event-Based-Visual-Odometry-on-Non-Holonomic-Ground-Vehicles>Event-Based Visual Odometry on Non-Holonomic Ground Vehicles</a></li>
      </ul>
    </li>
    <li><a href=#sfm>SFM</a></li>
      <ul>
        <li><a href=#3D-Scene-Geometry-Estimation-from-360$^\circ$-Imagery:-A-Survey>3D Scene Geometry Estimation from 360$^\circ$ Imagery: A Survey</a></li>
        <li><a href=#ICON:-Incremental-CONfidence-for-Joint-Pose-and-Radiance-Field-Optimization>ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization</a></li>
      </ul>
    </li>
    <li><a href=#keypoint-detection>Keypoint Detection</a></li>
      <ul>
        <li><a href=#To-deform-or-not:-treatment-aware-longitudinal-registration-for-breast-DCE-MRI-during-neoadjuvant-chemotherapy-via-unsupervised-keypoints-detection>To deform or not: treatment-aware longitudinal registration for breast DCE-MRI during neoadjuvant chemotherapy via unsupervised keypoints detection</a></li>
      </ul>
    </li>
    <li><a href=#nerf>NeRF</a></li>
      <ul>
        <li><a href=#ICON:-Incremental-CONfidence-for-Joint-Pose-and-Radiance-Field-Optimization>ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization</a></li>
      </ul>
    </li>
  </ol>
</details>

## SLAM  

### [Event-Based Visual Odometry on Non-Holonomic Ground Vehicles](http://arxiv.org/abs/2401.09331)  
[[code](https://github.com/gowanting/nhevo)]  
Wanting Xu, Si'ao Zhang, Li Cui, Xin Peng, Laurent Kneip  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Despite the promise of superior performance under challenging conditions, event-based motion estimation remains a hard problem owing to the difficulty of extracting and tracking stable features from event streams. In order to robustify the estimation, it is generally believed that fusion with other sensors is a requirement. In this work, we demonstrate reliable, purely event-based visual odometry on planar ground vehicles by employing the constrained non-holonomic motion model of Ackermann steering platforms. We extend single feature n-linearities for regular frame-based cameras to the case of quasi time-continuous event-tracks, and achieve a polynomial form via variable degree Taylor expansions. Robust averaging over multiple event tracks is simply achieved via histogram voting. As demonstrated on both simulated and real data, our algorithm achieves accurate and robust estimates of the vehicle's instantaneous rotational velocity, and thus results that are comparable to the delta rotations obtained by frame-based sensors under normal conditions. We furthermore significantly outperform the more traditional alternatives in challenging illumination scenarios. The code is available at \url{https://github.com/gowanting/NHEVO}.  
  </ol>  
</details>  
**comments**: Accepted by 3DV 2024  
  
  



## SFM  

### [3D Scene Geometry Estimation from 360 $^\circ$ Imagery: A Survey](http://arxiv.org/abs/2401.09252)  
Thiago Lopes Trugillo da Silveira, Paulo Gamarra Lessa Pinto, Jeffri Erwin Murrugarra Llerena, Claudio Rosito Jung  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    This paper provides a comprehensive survey on pioneer and state-of-the-art 3D scene geometry estimation methodologies based on single, two, or multiple images captured under the omnidirectional optics. We first revisit the basic concepts of the spherical camera model, and review the most common acquisition technologies and representation formats suitable for omnidirectional (also called 360$^\circ$, spherical or panoramic) images and videos. We then survey monocular layout and depth inference approaches, highlighting the recent advances in learning-based solutions suited for spherical data. The classical stereo matching is then revised on the spherical domain, where methodologies for detecting and describing sparse and dense features become crucial. The stereo matching concepts are then extrapolated for multiple view camera setups, categorizing them among light fields, multi-view stereo, and structure from motion (or visual simultaneous localization and mapping). We also compile and discuss commonly adopted datasets and figures of merit indicated for each purpose and list recent results for completeness. We conclude this paper by pointing out current and future trends.  
  </ol>  
</details>  
**comments**: Published in ACM Computing Surveys  
  
### [ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization](http://arxiv.org/abs/2401.08937)  
Weiyao Wang, Pierre Gleize, Hao Tang, Xingyu Chen, Kevin J Liang, Matt Feiszli  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Fields (NeRF) exhibit remarkable performance for Novel View Synthesis (NVS) given a set of 2D images. However, NeRF training requires accurate camera pose for each input view, typically obtained by Structure-from-Motion (SfM) pipelines. Recent works have attempted to relax this constraint, but they still often rely on decent initial poses which they can refine. Here we aim at removing the requirement for pose initialization. We present Incremental CONfidence (ICON), an optimization procedure for training NeRFs from 2D video frames. ICON only assumes smooth camera motion to estimate initial guess for poses. Further, ICON introduces ``confidence": an adaptive measure of model quality used to dynamically reweight gradients. ICON relies on high-confidence poses to learn NeRF, and high-confidence 3D structure (as encoded by NeRF) to learn poses. We show that ICON, without prior pose initialization, achieves superior performance in both CO3D and HO3D versus methods which use SfM pose.  
  </ol>  
</details>  
  
  



## Keypoint Detection  

### [To deform or not: treatment-aware longitudinal registration for breast DCE-MRI during neoadjuvant chemotherapy via unsupervised keypoints detection](http://arxiv.org/abs/2401.09336)  
[[code](https://github.com/fiy2w/treatment-aware-longitudinal-registration)]  
Luyi Han, Tao Tan, Tianyu Zhang, Yuan Gao, Xin Wang, Valentina Longo, Sofía Ventura-Díaz, Anna D'Angelo, Jonas Teuwen, Ritse Mann  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Clinicians compare breast DCE-MRI after neoadjuvant chemotherapy (NAC) with pre-treatment scans to evaluate the response to NAC. Clinical evidence supports that accurate longitudinal deformable registration without deforming treated tumor regions is key to quantifying tumor changes. We propose a conditional pyramid registration network based on unsupervised keypoint detection and selective volume-preserving to quantify changes over time. In this approach, we extract the structural and the abnormal keypoints from DCE-MRI, apply the structural keypoints for the registration algorithm to restrict large deformation, and employ volume-preserving loss based on abnormal keypoints to keep the volume of the tumor unchanged after registration. We use a clinical dataset with 1630 MRI scans from 314 patients treated with NAC. The results demonstrate that our method registers with better performance and better volume preservation of the tumors. Furthermore, a local-global-combining biomarker based on the proposed method achieves high accuracy in pathological complete response (pCR) prediction, indicating that predictive information exists outside tumor regions. The biomarkers could potentially be used to avoid unnecessary surgeries for certain patients. It may be valuable for clinicians and/or computer systems to conduct follow-up tumor segmentation and response prediction on images registered by our method. Our code is available on \url{https://github.com/fiy2W/Treatment-aware-Longitudinal-Registration}.  
  </ol>  
</details>  
  
  



## NeRF  

### [ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization](http://arxiv.org/abs/2401.08937)  
Weiyao Wang, Pierre Gleize, Hao Tang, Xingyu Chen, Kevin J Liang, Matt Feiszli  
<details>  
  <summary>Abstract</summary>  
  <ol>  
    Neural Radiance Fields (NeRF) exhibit remarkable performance for Novel View Synthesis (NVS) given a set of 2D images. However, NeRF training requires accurate camera pose for each input view, typically obtained by Structure-from-Motion (SfM) pipelines. Recent works have attempted to relax this constraint, but they still often rely on decent initial poses which they can refine. Here we aim at removing the requirement for pose initialization. We present Incremental CONfidence (ICON), an optimization procedure for training NeRFs from 2D video frames. ICON only assumes smooth camera motion to estimate initial guess for poses. Further, ICON introduces ``confidence": an adaptive measure of model quality used to dynamically reweight gradients. ICON relies on high-confidence poses to learn NeRF, and high-confidence 3D structure (as encoded by NeRF) to learn poses. We show that ICON, without prior pose initialization, achieves superior performance in both CO3D and HO3D versus methods which use SfM pose.  
  </ol>  
</details>  
  
  



