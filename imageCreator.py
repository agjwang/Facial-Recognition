from PIL import Image
from facialDetection import classifyFaces

def overlayImage(image_path, overlay_path, output_path):
   face_data = classifyFaces(image_path)
   overlay = Image.open(overlay_path)
   image = Image.open(image_path)

   overlay = resizeImage(overlay, face_data)
   Image.alpha_composite(image, overlay).save(output_path)

def resizeImage(image, face_data)
   image.thumbnail(face_data['w'])
   image.transform(image.size, Image.AFFINE, (1, 0, face_data['x'], 0, 1, face_data['y']))

   return image
