import requests
import json
import re
import os

def text_to_dict(text_file):
    with open('supplier-data/descriptions/' + text_file, 'r') as f:
        out_ls = [line.strip('\n') for line in f.readlines()]
        out_dict = {
            "name":out_ls[0],
            "weight":int(re.findall(r'\d+ ',out_ls[1])[0].strip()),
            "description":out_ls[2],
            "image_name":re.sub('txt','jpeg',text_file)
        }
    return out_dict

if __name__ == '__main__':
    for file in os.listdir('supplier-data/descriptions/'):
        body = text_to_dict(file)
        print(body)
        resp = requests.post('http://104.154.149.51/fruits',json = body)
        print(resp,resp.reason)
