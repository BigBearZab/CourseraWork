#!/usr/bin/env python3

import os
import re
from PIL import Image as im
def transform_image(original_image):
    
    og_im = im.open('supplier-data/images/'+original_image)
    new_im = og_im.resize((600,400)).convert('RGB')
    new_im.save('supplier-data/images/'+ original_image[0:3] + '.jpeg', 'JPEG')

def get_image_list():
    im_list = [f for f in os.listdir('supplier-data/images') if re.match(r'[0-9]+\.tiff', f)]
    return(im_list)

if __name__ == '__main__':
    for image in get_image_list():
        transform_image(image)
