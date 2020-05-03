import cv2
import datetime


cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_TRIPLEX
        
        datet = str(datetime.datetime.now())
        text = 'Width: ' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
        frame = cv2.putText(frame, datet, (10,50), font,1 ,(0, 255, 255), 2, cv2.LINE_AA)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()