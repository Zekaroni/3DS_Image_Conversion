from os import path
from PIL import Image

file_path = input("Enter file path of your HNI_xxxx.JPG image from 3DS : ")
if path.exists(file_path):
    dummy_image = Image.open(file_path)
    exif = dummy_image.info['exif']
    with open('sample.exif', 'wb') as sample_out:
        sample_out.write(exif)
else:
    print("Path not found.")
