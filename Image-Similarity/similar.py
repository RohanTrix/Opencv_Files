import cv2
import numpy as np
import matplotlib.pyplot as plt
org = cv2.imread('main_img.png')
duplicate = cv2.imread('test1.png')

cv2.imshow('Main',org)
cv2.imshow('test',duplicate)
same_size_and_channels = False
if org.shape == duplicate.shape:
    diff = cv2.subtract(duplicate, org)
    cv2.imshow('Subtract', diff)
    b, g, r = cv2.split()


cv2.waitKey(0)
cv2.destroyAllWindows()
