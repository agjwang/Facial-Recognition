import numpy as np
import cv2

from PIL import Image
from facialDetection import classifyFaces

def overlayImage(image_path, overlay_path, output_path):
    face_data = classifyFaces(image_path)
    image = cv2.imread(image_path)

    overlay = cv2.imread(overlay_path, -1)
    new_image = image

    for face in face_data:
        face = repositionOverlay(overlay_path, face)
        x, y, h, w = face['x'], face['y'], face['h'], face['w']
        overlay = resizeOverlay(overlay, face, image)

        for c in range(0, 3):
            alpha = overlay[:, :, 3] / 255.0
            overlay_values = overlay[:, :, c] * alpha

            if (y < 0):
                h = h + y
                y = 0

            background_values = image[y : y + h, x : x + w, c] * (1 - alpha)
            image[y : y + h, x : x + w, c] = overlay_values + background_values

    cv2.imwrite(output_path, new_image)
    return

def resizeOverlay(overlay, face_data, image):
    x, y, w, h = face_data['x'], face_data['y'], face_data['w'], face_data['h']
    overlay = cv2.resize(overlay, (w, h))

    image_height, image_width = image.shape[ : 2]
    if y < 0:
        overlay = overlay[-y : h, :]
    if y + h >= image_height:
        overlay = overlay[0 : image_height - (y + h), :]

    return overlay

def repositionOverlay(overlay_path, face_data):
    if overlay_path == 'scarf.png':
        face_data['y'] = face_data['y'] + int(face_data['h'] * 0.8)
    elif overlay_path == 'dark_magician_girl_hat.png':
        face_data['y'] = face_data['y'] - int(face_data['h'] * 0.5)
    else:
        face_data['y'] = face_data['y'] - int(face_data['h'] * 0.5)

    return face_data

overlayImage('idolmaster.jpg', 'cat_ears.png', 'new.jpg')