import cv2 as cv
import numpy as np 


people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']

haarCascade = cv.CascadeClassifier('harr_face.xml')

""" features  = np.load('features.npy')
labels  = np.load('labels.npy') """

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'F:\Computer Vision Stuff\Open CV Tutorial\face_recognition_app\dataset\val\ben_afflek\httpabsolumentgratuitfreefrimagesbenaffleckjpg.jpg')


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('img' , gray)

#Detect the img 

faces_rect = haarCascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=4)

for (x , y ,w , h) in faces_rect:
    face_roi = gray[ y: y + h , x : x + w]

    label , confidence = face_recognizer.predict(face_roi)
    print(f'Label = {label} with confidence of {confidence}')

    cv.putText(img , str(people[label]) , (20 , 20) , cv.FONT_HERSHEY_COMPLEX, 1.0 , (2 ,255 , 0), thickness = 2)

    cv.rectangle(img , (x , y) , (x+w , y+h) , (0 ,255 , 0) , thickness=2)


cv.imshow("detected img" , img)
               







cv.waitKey(0)