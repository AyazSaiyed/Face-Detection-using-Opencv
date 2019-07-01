#Developed By - Ayaz Saiyed
#YudizSolutions

import numpy as np
import cv2


def face_detect() :
    face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        cv2.namedWindow('Face Detect', cv2.WINDOW_AUTOSIZE)
        while cv2.getWindowProperty('Face Detect',0) >= 0:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            cv2.imshow('Face Detect',img)
            keyCode = cv2.waitKey(30) & 0xff
            # Press ESC key to stop the program 
            if keyCode == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to Open Camera")

if __name__ == '__main__':
    face_detect()
