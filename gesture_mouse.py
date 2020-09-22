import numpy as np
import cv2
import pyautogui

cap=cv2.VideoCapture(0)
cv2.CAP_PROP_FPS = 60
low_green = np.array([36, 25, 25])
high_green = np.array([70, 255, 255])

low_red = np.array([0,150,200])
high_red = np.array([177,255,255])
def move_mouse_to(x,y):
    pyautogui.moveTo(1920-x,y,duration=0)
'''
def mouse_click():
    pyautogui.click()
'''
while True:
    ret, img=cap.read()
    img = cv2.resize(img,(1920,1080),interpolation=cv2.INTER_LINEAR)
    roi = img[:100,:100]
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    kernel=np.ones((5,5),np.uint8)
    
    mask1=cv2.inRange(hsv,low_green,high_green)
    mask1 = cv2.erode(mask1, kernel, iterations=2)
    mask1 = cv2.dilate(mask1, kernel, iterations=1)
    
     
    
    _,cnts,_=cv2.findContours(mask1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    '''
    for i in range(3):
        ret, img1=cap.read()
        img1 = cv2.resize(img,(1920,1080),interpolation=cv2.INTER_LINEAR)
        hsv1=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
        mask2=cv2.inRange(hsv1,low_red,high_red)
        mask2 = cv2.erode(mask2, kernel, iterations=2)
        mask2 = cv2.dilate(mask2, kernel, iterations=1)
        cv2.imshow('mask',mask2)
        _,cnts1,_=cv2.findContours(mask2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts1)>0:
            count+=1
    if count==3:
        mouse_click()
        '''
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        move_mouse_to(int(x),int(y))
        img = cv2.circle(img,(int(x),int(y)),20,(0,255,255),-1)
    
    #cv2.imshow('mask',mask1)
    cv2.imshow('orig',cv2.rectangle(img,(0,0),(100,100),(0,0,255),5))
    if cv2.waitKey(1)==ord(' '):
        break
cap.release()
cv2.destroyAllWindows() 