import numpy as nump
import cv2
variable = cv2.CascadeClassifier('lbpcascade_animeface.xml')
print 'here'

img = cv2.imread('lelouch.jpg')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_detect = variable.detectMultiScale(grey, 1.3, 5)

for(x, y, w, h) in face_detect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = grey[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
