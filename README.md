## Micro-expression spotting code inspired from Davison et al. (2015) and Moilanen et al. (2014).

#### The approach uses a sliding window mechanism centered around the current frame. HOG features are extracted from the current frame, and compared with the average of the HOG features from the first and last frame in the window to spot frames exhibiting micro-expressions. </br>

### Running the Code
#### To extract the face from the input video:
#### >>python project.py \<input video\>

#### This saves the cropped and aligned frames to a folder 'aligned_frames'.

#### To display frames exhibiting micro-expressions:
#### >>python get_features.py aligned_frames </br>

### To Do
#### Implement mechanism to set threshold. </br>


### References
#### Davison, A. K., Yap, M. H., & Lansley, C. (2015, October). Micro-facial movement detection using individualised baselines and histogram-based descriptors. In Systems, Man, and Cybernetics (SMC), 2015 IEEE International Conference on (pp. 1864-1869). IEEE.

#### Moilanen, A., Zhao, G., & Pietikäinen, M. (2014, August). Spotting rapid facial movements from videos using appearance-based feature difference analysis. In Pattern Recognition (ICPR), 2014 22nd International Conference on (pp. 1722-1727). IEEE.
