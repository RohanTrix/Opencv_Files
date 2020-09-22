import cv2
import numpy as np

org = cv2.imread('main_img.png')

cv2.imshow('MAIN', org)

cv2.waitKey(0)
cv2.destroyAllWindows()
