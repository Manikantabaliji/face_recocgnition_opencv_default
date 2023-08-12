import os
import cv2 as cv
import numpy as np

people=[]
for i in os.listdir(r'D:/Face_rec/images'):
    people.append(i)

# print(people)
DIR=r'D:/Face_rec/images'
haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]

def training():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in face_rect:
                face_crop=gray[y:y+h,x:x+w]
                features.append(face_crop)
                labels.append(label)
                break

training()
features=np.array(features, dtype='object')
labels=np.array(labels)

face_recocgnizer=cv.face.LBPHFaceRecognizer.create()

face_recocgnizer.train(features,labels)

face_recocgnizer.save('face_trained.yml')



