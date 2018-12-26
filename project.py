'''
Extract and align faces using opencv dlib library. 

Usage:
>> python project.py <foldername>

Output:
./aligned_frames
'''

import sys
import dlib
import cv2
import openface
import os

# You can download the required pre-trained face detection model here:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

# Take the folder name from the command line
folder_name = sys.argv[1]


count = 0

for img in os.listdir(folder_name):

	print img
	count = img[3:-4]

	# Load the image
	image = cv2.imread(folder_name+'/'+img)

	# Run the HOG face detector on the image data
	detected_faces = face_detector(image, 1)

	print("Found {} faces in the image file {}".format(len(detected_faces), img))

	# Loop through each face we found in the image
	for i, face_rect in enumerate(detected_faces):

		# Detected faces are returned as an object with the coordinates 
		# of the top, left, right and bottom edges
		print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))

		#
		#	Optional Alignment of faces
		#
		
		# Get the the face's pose
		#pose_landmarks = face_pose_predictor(image, face_rect)

		# Use openface to calculate and perform the face alignment
		#alignedFace = face_aligner.align(400, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)


        	face = image[face_rect.top():face_rect.bottom(), face_rect.left():face_rect.right()]
		alignedFace = cv2.resize(face, (400, 400)) 


		# Save the aligned image to a file
		cv2.imwrite("aligned_frames6/aligned_face_{}.jpg".format(count), alignedFace)

		
