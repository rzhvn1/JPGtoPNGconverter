import sys
import os

from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check is new/exists, if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#loop through Pokedex
for filename in os.listdir(image_folder):
	img = Image.open(f"{image_folder}{filename}")
	clean_name = os.path.splitext(filename)[0] #get a filename without an extension
	img.save(f"{output_folder}{clean_name}.png", "png") #convert images to png and save to new folder
	print('converting...')
print('all done!')





