import json
import os
from astropy.io import fits 
import random
import numpy as np 
from image_utils import encode_image_to_base64


Galaxy_Dir = '/Users/jackskinner/Documents/3rd Year/Computer Science/astrodataset/astrodataset/outputdata/outputfits/galaxies'
GC_Dir = '/Users/jackskinner/Documents/3rd Year/Computer Science/astrodataset/astrodataset/outputdata/outputfits/fitsgcs'
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
data.extend(load_images(Galaxy_Dir, 5, "Galaxies"))
data.extend(load_images(GC_Dir, 5, "GCs"))
random.shuffle(data)
with open(output, "w") as json_file:
    json.dump(data, json_file, indent=4)