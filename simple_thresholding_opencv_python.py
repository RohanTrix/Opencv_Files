import cv2 as cv

img = cv.imread('gradient.png', 0)

_,th1 = cv.threshold(img, 50,255,cv.THRESH_BINARY)
_,th2 = cv.threshold(img, 200,255,cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img, 127,255,cv.THRESH_TRUNC)
_,th4 = cv.threshold(img, 127,255,cv.THRESH_TOZERO)
_,th5 = cv.threshold(img, 127,255,cv.THRESH_TOZERO_INV)
cv.imshow("Image", img)
cv.imshow("Thresh",th1)
cv.imshow("Thresh2",th2)
cv.imshow('Thresh3',th3)
cv.imshow('Thresh4',th4)
cv.imshow('Thresh5',th5)

cv.waitKey(0)
cv.destroyAllWindows()
