import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ori_open = True
hello_open = True

while(True):
    ret, frame = cap.read()
    if not ret :
        break

    frame = cv2.flip(frame, 1)

    if ori_open:
        cv2.imshow('ori frame', frame)    
    
    font = cv2.FONT_HERSHEY_TRIPLEX
    frame_text = cv2.putText(frame, 'Hallo rek!', (10,50), font, 1, (111,198,15), 2, cv2.LINE_AA)
    cv2.imshow('hello frame', frame_text)
    
    if hello_open:
        cv2.imshow('hello frame', frame_text)
    
    
    if ori_open and cv2.getWindowProperty('ori frame', cv2.WND_PROP_VISIBLE) < 1:
        ori_open = False
        cv2.destroyWindow('ori frame')

    if hello_open and cv2.getWindowProperty('hello frame', cv2.WND_PROP_VISIBLE) < 1:
        hello_open = False
        cv2.destroyWindow('hello frame')

    if not ori_open and not hello_open:
        break
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
    
    
cap.release()
cv2.destroyAllWindows()