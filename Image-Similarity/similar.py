import cv2
import numpy as np
import matplotlib.pyplot as plt
org = cv2.imread('main_img.png')
img_to_compare = cv2.imread('test2.png')

#######################
plt.imshow(org)
#######################
org = org[88:682, 508: 843]
img_to_compare = img_to_compare[88:682, 508: 843]

cv2.imshow('Main',org)
cv2.imshow('test',img_to_compare)
same_image = False
if org.shape == img_to_compare.shape:
    diff = cv2.subtract(img_to_compare, org)
    cv2.imshow('Subtract', diff)
    b, g, r = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r):
        same_image = True
    if same_image:
        quit()

sift = cv2.xfeatures2d.SIFT_create()

# keypoints and descriptors
kp_1, desc_1 = sift.detectAndCompute(org, None)
kp_2, desc_2 = sift.detectAndCompute(img_to_compare, None)

index_params = dict(algorithm=0, trees=5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)  
        
matches = flann.knnMatch(desc_1, desc_2, k = 2)
print(len(matches))


good_points = []


result = cv2.drawMatchesKnn(org, kp_1, 
                         img_to_compare, kp_2,
                         matches,None, flags=2)

cv2.imshow('Matched',result)


cv2.waitKey(0)
cv2.destroyAllWindows()
