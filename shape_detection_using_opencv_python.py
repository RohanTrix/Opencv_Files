import cv2

img = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
_,contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,closed = True
                                                         ),closed = True)
    
    cv2.drawContours(img, [approx],0,(0,0,0),5)
    
    x = approx.ravel()[0]
    y= approx.ravel()[1]-10
    
    if len(approx) ==3:
        cv2.putText(img, "TRIANGLE",(x,y),cv2.FONT_HERSHEY_SIMPLEX
                    ,0.5,(0,0,0))
    elif len(approx) == 4:
        x1,y1,w,h =cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if 1.05>=aspectRatio>= 0.95:
            cv2.putText(img,'Square',(x,y),cv2.FONT_HERSHEY_SIMPLEX
                    ,0.5,(0,0,0))
        else:
            cv2.putText(img,'Rectange',(x,y),cv2.FONT_HERSHEY_SIMPLEX
                    ,0.5,(0,0,0))
    
    
    elif len(approx) == 5:
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX
                    ,0.5,(0,0,0))
    else:
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX
                    ,0.5,(0,0,0))

    
    
    
cv2.imshow('Original',img)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()