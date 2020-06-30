import cv2
import numpy as np
img = cv2.imread('shapes.jpg')
n_rows,n_cols = img.shape[:2]

rot_mat = cv2.getRotationMatrix2D((n_rows/2,n_cols/2), 90,0.7)
img_rot = cv2.warpAffine(img, rot_mat, (n_cols, n_rows))
cv2.imshow('Rotated', img_rot)
cv2.waitKey(0)