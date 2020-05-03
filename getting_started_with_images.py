import cv2
img = cv2.imread('lena.jpg', 1)
k = cv2.imread('jas.jpg',1)
f= img[:]
img = cv2.bitwise_xor(img,k)
cv2.imshow('image', img)
cv2.imshow('im',f)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena-copy.jpg',img)
