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
        x, y, h, w = face['x'], face['y'], face['h'], face['w']
        overlay = resizeOverlay(overlay, face)

        for c in range(0, 3):
            alpha = overlay[:, :, 3] / 255.0
            overlay_values = overlay[:, :, c] * alpha
            background_values = image[y : y + h, x : x + h, c] * (1 - alpha)
            image[y : y + h, x : x + w, c] = overlay_values + background_values

        cv2.rectangle(new_image, (face['x'], face['y']), (face['x'] + face['w'], face['y'] + face['h']), (255, 0, 0), 2)

    cv2.imwrite(output_path, new_image)
    return

def resizeOverlay(overlay, face_data):
    overlay = cv2.resize(overlay, (face_data['w'], face_data['h']))
    return overlay

overlayImage('lelouch.jpg', 'dark_magician_girl_hat.png', 'new.jpg')