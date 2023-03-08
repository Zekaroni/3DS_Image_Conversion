from os import listdir, path, remove
from PIL import Image

print("(WARNING: Images in the input folder will be moved(deleted) to the output folder with exif data modified)")

try:
    ending_num = int(input('Enter the highest file number ending (E.g. 63) : '))
except ValueError:
    print('Make sure to input an integer\nExiting...')

# Adds the exif data to a variable called metadata
with open('sample.exif','rb') as exif_file:
    metadata = exif_file.read()


if path.exists('./input'): # Checks if input folder exists
    for image_file in listdir('./input'): # Loops over every file in input
        if image_file.split('.')[-1].lower() in ['jpg','jpeg','png']: # Checks for supported extensions
            tmp_image = Image.open(f'./input/{image_file}') # Loads the image into an Image object
            x,y = tmp_image.size # Assigns the height and width of the image to variables

            if x > 640 or y > 480: # Checks if the image is too large
                print(f'Image "{image_file}" is too big. Limited to 640 x 480.')
            else:
                ending_num+=1
                tmp_image.save(f'{"./output/" if path.exists("./output") else ""}HNI_{str(ending_num).zfill(4)}.JPG', exif=metadata) # Creates the file with metadata to be read by 3DS
                remove(f'./input/{image_file}')
        else:
            if image_file == "PUT IMAGES HERE":
                pass # Ignores the basic file placeholder
            else:
                print(f'"{image_file}" has an unsupported file extension.')
