import json
import os
from astropy.io import fits 
import random
import numpy as np 
from image_utils import encode_image_to_base64


Galaxy_Dir = 'OpenAI-venv/galaxyimages'
GC_Dir = 'OpenAI-venv/gcimages'
Large_Galaxy_Dir = 'OpenAI-venv/LargeGalaxyImages'
Large_GC_Dir = 'OpenAI-venv/largegcimages'
output = 'OpenAI-venv/data.json'
data = []

def load_images(path, noimages, filetype): 
    with os.scandir(path) as files:
        images = []
        nofiles = 0
        for file in files: 
            if file.name.startswith('.') or nofiles == noimages:
                continue  
            #Exeption handling if dataset contains non fits file
            try: 
                image = fits.open(file)
            except:
                continue


            data = image[0].data
            image = encode_image_to_base64(data)

            images.append({
                "file_name": file.name,
                "metadata": {
                    "object_type" : filetype
                },
                "image_data": image
            })
            nofiles += 1 
    return (images)
data.extend(load_images(Large_Galaxy_Dir, 50, ""))
data.extend(load_images(Large_GC_Dir, 50, ""))
random.shuffle(data)
with open(output, "w") as json_file:
    json.dump(data, json_file, indent=4)