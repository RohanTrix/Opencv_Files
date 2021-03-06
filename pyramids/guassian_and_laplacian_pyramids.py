import cv2
img = cv2.imread('lena.jpg')
layer = img.copy()
gp=[layer]

#Guassian Pyramids

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer.copy())
    #cv2.imshow(str(i),layer)
    
#Laplacian Pyramids (formed form Gaussian pyramids)
layer = gp[5]
cv2.imshow('Upper level Gussian Pyramid',layer)
lp = [layer]
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()

