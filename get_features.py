import matplotlib.pyplot as plt

import cv2
import sys
import os
import re
from skimage.feature import hog
from skimage import data, exposure
import numpy as np

import chisquared



#
# micro interval frame length
#
N = 81

k = (N - 1)/2
thres = 0.55


folder = sys.argv[1]


old_fd = 0.0
window = [0.0] * N


files = os.listdir(folder)

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


count = 0


for img in sorted(files, key=numericalSort)[:N-1]:

	#print img
	image = cv2.imread(folder + '/' + img)
	#print image


	# We want the image divided into 5 X 5 cells
	# Image size: 180 X 180 therefore 36 X 36 pixels per cell
	# No block normalization as per paper

	old_fd = hog(image, orientations=8, pixels_per_cell=(36, 36),
			    cells_per_block=(1, 1), block_norm='L2-Hys', visualize=False, feature_vector=True, multichannel=True)

	#print old_fd

	window[count] = old_fd

	count += 1



out = open('distance.txt','w')


for img in sorted(files, key=numericalSort)[N-1:]:

	#print img
	image = cv2.imread(folder + '/' + img)
	#print image

	fd = hog(image, orientations=8, pixels_per_cell=(36, 36),
		            cells_per_block=(1, 1), block_norm='L2-Hys', visualize=False, feature_vector=True, multichannel=True)


	window[(count % N)] = fd

	#distance = np.linalg.norm((fd - old_fd))


	# To calcluate distance between consecutive frames
	'''
	distance = chisquared.chisquared(fd, old_fd)
	
	if(distance>2):
		print count
		print distance
	'''

	# To get peak in a window (Moilanen et al, 2014)

	CF = (count - k) % N 
	TF = (count - N + 1) % N
	HF = count % N
	
	feat_AFF = (np.array(window[CF]) + np.array(window[HF])) / 2
	feat_CF = window[CF]

	distance = chisquared.chisquared(feat_AFF, feat_CF)

	#contrasted_distance = distance - 0.5*(distance_1 + distance_2)

	out.write(str(distance))
	out.write('\n')


	if(distance > thres):
		print ''
		print count
		print ''
	
	#print distance

	
	count+=1

	old_fd = fd

