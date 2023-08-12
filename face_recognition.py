import cv2 as cv
import os

people=[]
for i in os.listdir(r'D:/Face_rec/images'):
    people.append(i)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
face_recognizer=cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('face_trained.yml')
img=cv.imread('images/virat_kohli/f0e40d891d.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in face_rect:
    face_crop=gray[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(face_crop)
    print(f'label={label} and confidence={confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected',img)
cv.waitKey(0)