import numpy as nump
import cv2

def classifyFaces(str):
    face_cascade = cv2.CascadeClassifier('lbpcascade_animeface.xml')
    img = cv2.imread(str)

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_info = list()
    faces = face_cascade.detectMultiScale(grey, 1.01, 5)
    for (x, y, w, h) in faces:
        face_info = dict()
        face_info['x'] = x
        face_info['y'] = y
        face_info['w'] = w
        face_info['h'] = h
        faces_info.append(face_info)

    return faces_info

#print(classifyFaces('lelouch.jpg'))
#classifyFaces('idolmaster.jpg')
#classifyFaces('fma.jpg')
