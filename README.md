# Image Conversion for 3DS
#### Video Demo:
[TODO] Will eventually make something for this.
#### Description:
These files allow you to convert an image (as long as it's within the size limit and uses the supported formats) to be converted for use on the 3DS. All the previous methods I had found did not work for my New3DS, so I made this.

## Dependencies
- [`PIL`](https://github.com/python-pillow/Pillow) Python Imaging Library

#### How to use the application:
To convert a file to be compatible with the 3DS, you first have to make sure the dimensions do not exceed ***640x480***. This code supports *JPG*, *JPEG*, and *PNG*, so be sure to use one of these formats when resizing your image. After your image meet the size requirements, put it into the `input` folder and then run `convert.py`. When prompted with the question of the highest file name, input the highest number seen when viewing your 3DS images. **Example:** `HNI_0192.JPG` you would enter `192`.

#### Features:

- The `convert.py` allows you to convert all the images in the `input` folder and automatically name them based on your input. 
*NOTE:* The program will just ignore an image if it cannot be converted.
- `make_exif_file.py` Allows you to create a new `.exif` file based on a given image from a 3DS, e.g. one from your own. The `.exif` file is what `convert.py` uses to encode metadata that allows the image to be recognized by the 3DS.
*NOTE:* `sample.exif` is an exported file from a black image I took using my 3DS. I haven't tested using this picture with a different 3DS, so you may *have* to make your own from an image you take.