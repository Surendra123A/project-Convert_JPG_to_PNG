from PIL import Image
import sys
import os
import cv2
from os import listdir

# grab the first and second arugs from the promt

folder1 = str(sys.argv[1])
folder2 = str(sys.argv[2])

# check if new/ exists, if not create one
newImages = []
if not (os.path.isdir(folder2)):
    os.mkdir(r'newPokedex')
    folder2 = 'newPokedex'

# loop through pokedex
for images in os.listdir(folder1):
    img_name = os.path.splitext(images)[0]

    # convert images to png
    img = Image.open(fr'F:\python projects\\convert jpg to png\pokedex\{images}')
    # save them to the new/ folder
    img.save(f'./{folder2}/{img_name}.png')

print('All Done !!!')









