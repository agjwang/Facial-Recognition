import numpy as nump
import cv2
variable = cv2.CascadeClassifier('lbpcascade_animeface.xml')
print 'here'

img=cv2.imread('lelouch.jpg')

print 'image load works'