"""
this file will open a frame showing video feed from webcamera, detect and identify faces
wich has been previously trained with "faces-train.py"

Based on opencv tutorial by joincfe.com
"""

import numpy
import cv2
import pickle

face_cascade = cv2.CascadeClassifier("cascades\\data\\haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {}
with open ("labels.pickel", "rb") as f:
    og_labels = pickle.load( f )
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #recognize opencv recognizer
        id_ , conf = recognizer.predict(roi_gray) # id_ and conf= confidence level of recognizer 
        if conf >= 60 and conf <= 85 :
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame,name,(x,y), font, 1, color, stroke, cv2.LINE_AA)
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255,0,0) #BGR - blue-green-red
        stroke = 2
        width = x + w
        height = y + h
        cv2.rectangle(frame, (x,y), (width, height), color, stroke)
    #Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


# When everyting done, release the capture
cap.release()
cv2.destroyAllWindows