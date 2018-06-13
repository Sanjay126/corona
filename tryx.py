# import the necessary packages
import sys
sys.path.append("/home/sanjay")
import Sticher
import argparse
import imutils
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
help="path to the first image")
ap.add_argument("-s", "--second", required=True,
help="path to the second image")
args = vars(ap.parse_args())
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
#imageA = imutils.resize(imageA, 1000,1000)
#imageB = imutils.resize(imageB, 1000,1000)
 
# stitch the images together to create a panorama
stitcher =Sticher.Sticher()
(result, vis) = stitcher.stich(imageA, imageB, showMatches=True)
# show the images
#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)