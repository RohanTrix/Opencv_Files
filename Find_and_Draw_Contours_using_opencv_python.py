import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
#The findContours method's return values are changed in OpenCV 4
_,contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)


#print(contours)

cv2.drawContours(img,contours,-1,(0,255,255),3)


cv2.imshow('Image',img)
cv2.imshow('Image GRAY',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()




