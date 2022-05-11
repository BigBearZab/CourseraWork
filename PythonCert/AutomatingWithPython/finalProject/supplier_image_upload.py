#!/usr/bin/env python3
import requests
import os
import re

url = "http://localhost/upload/"

def image_upload(image):
    print(f'Uploading {image}')
    with open('supplier-data/images/' + image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

def get_image_list():
    im_list = [f for f in os.listdir('supplier-data/images') if re.match(r'[0-9]+\.jpeg', f)]
    print(im_list)
    return(im_list)

if __name__ == '__main__':
    for image in get_image_list():
        image_upload(image)