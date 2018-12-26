# Microexpression-Spotting

## Micro-expression spotting code inspired from Davison et al. (2015) and Moilanen et al. (2014).

### The approach uses a sliding window mechanism centered around the current frame. HOG features are extracted from the current frame, and compared with the average of the HOG features from the first and last frame in the window to spot frames exhibiting micro-expressions.

### To extract the face from the input video:
### >>python project.py <input video>

###
