# LESS ACCURATE HUMAN DETECTION

import cv2

cap = cv2.VideoCapture('in.avi')

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


while(True):
    ret, frame = cap.read()#capturinf multiple frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)
    
    for (x,y,w,h) in humans:# rectangular boxes
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()# releasing the captured frame