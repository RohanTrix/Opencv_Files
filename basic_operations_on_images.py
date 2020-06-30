import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape) #Returns tuple of number of rows,columns and channels
print(img.size)  #Restuns total numbers of pixels which are accessed
print(img.dtype) #returns dataype of image
b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))


dst = cv2.add(img2, img)

dst2 = cv2.addWeighted(img,0.7,img2,0.3,0)
cv2.imshow('image', dst)

cv2.imshow('image', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
