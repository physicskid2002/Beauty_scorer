# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=False,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=False,
	help="path to input image")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#shape_predictor_68_face_landmarks.dat
#args["shape_predictor"]
p=0
#os.chdir(r"C:\Users\Win8.1\source\repos\Face_stuff\facial-landmarks")
os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
images= os.listdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
#os.chdir(r"C:\Users\Win8.1\source\repos\Face_stuff\facial-landmarks\points")
for img in images:
# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(img)
	#args["image"]
	image = imutils.resize(image, width=300)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
	rects = detector(gray, 1)

# loop over the face detections
	for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
		shape = predictor(gray, rect)
		#f.write(shape)
		shape = face_utils.shape_to_np(shape)
		ls=[",".join(item) for item in shape.astype(str)]
		os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\facial_landmarks\68\CM")
		f = open("points{}.txt".format(img),"w")
		for j in ls:
			f.write(j)
			f.write("\n")
			p+=1
		print(shape)
		print(p)
		os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_images\CM")
		#f.write(shape)
	# convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then draw the face bounding box
		(x, y, w, h) = face_utils.rect_to_bb(rect)
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the face number
		cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
		for (x, y) in shape:
			cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

# show the output image with the face detections + facial landmarks
	#cv2.imshow("Output", image)
	#cv2.waitKey(0)