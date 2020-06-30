import cv2 as cv
import numpy as np

img = cv.imread('Test_1006.jpg',0)
screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)



th1 = cv.adaptiveThreshold(img,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 2)
th2 = cv.adaptiveThreshold(img,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
                           cv.THRESH_BINARY, 11, 2)

cv.resizeWindow('image',window_width,window_height)
cv.imshow('image',img)
cv.imshow('mean_thresholding',th1)
cv.imshow('gaussian_thresholding',th2)