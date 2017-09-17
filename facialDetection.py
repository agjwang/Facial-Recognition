import numpy as nump
import cv2
variable = cv2.CascadeClassifier('lbpcascade_animeface.xml')
print 'here'

img=cv2.imread('lelouch.jpg')

print 'image load works'

while True:
    grey_color=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_detecct=variable.detectMultiScale(grey_color, 1.3, 5)