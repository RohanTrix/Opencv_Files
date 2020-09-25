import sys
import cv2
import numpy as np
org = cv2.imread('images/main_img.png')
img_to_compare = cv2.imread('images/test2.png')


org = org[88:682, 508: 843]
img_to_compare = img_to_compare[88:682, 508: 843]

cv2.imshow('Main',org)
cv2.imshow('test',img_to_compare)


same_image = False
if org.shape == img_to_compare.shape:
    diff = cv2.subtract(img_to_compare, org)
    b, g, r = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r):
        same_image = True
    if same_image:
        print('same image')
        sys.exit()

sift = cv2.xfeatures2d.SIFT_create()

# keypoints and descriptors
kp_1, desc_1 = sift.detectAndCompute(org, None)
kp_2, desc_2 = sift.detectAndCompute(img_to_compare, None)


print("Key Points IMG1", len(kp_1))
print("Key Points IMG2", len(kp_2))
index_params = dict(algorithm=0, trees=5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)  
        
matches = flann.knnMatch(desc_1, desc_2, k = 2)


good_points = []

for m, n in matches:
    if m.distance < 0.4* n.distance:
        good_points.append(m)

print("Good Matches" ,len(good_points))

number_keypoints = min(len(kp_1), len(kp_2))

percent =(len(good_points)/ number_keypoints) * 100

print("How good is the match: ",round(percent), "%")


result = cv2.drawMatches(org, kp_1, 
                         img_to_compare, kp_2,
                         good_points,None, flags=2)

cv2.imshow('Matched',result)


cv2.waitKey(0)
cv2.destroyAllWindows()
