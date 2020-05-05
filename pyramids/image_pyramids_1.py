import cv2
import numpy as np
img = cv2.imread('lena.jpg')

#Guassian Pyramids
lr1 = cv2.pyrDown(img)# Decreases resolution of image
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)



cv2.imshow('Original image',img)
cv2.imshow('PyrDown 1 image',lr1)
cv2.imshow('PyrDown 2 image',lr2)
cv2.imshow('PyrUp 1 image',hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()

