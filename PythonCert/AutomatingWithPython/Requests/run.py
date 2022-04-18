
#! /usr/bin/env python3

import os
import requests
import json
list_to_parse = os.listdir('/data/feedback')

def text_to_dict(text_file):
    with open(text_file, 'r') as f:
        out_ls = [line.strip('\n') for line in f.readlines()]
        out_dict = {
            "title":out_ls[0],
            "name":out_ls[1],
            "date":out_ls[2],
            "feedback":out_ls[3]
        }
    return out_dict

for file in list_to_parse:
        p = text_to_dict('/data/feedback/'+file)
        print(json.dumps(p))
        response = requests.post('http://34.121.3.189/feedback', json=json.dumps(p))
        if response.status_code != 201:
                print(response.status_code)
                print(response.request.url)
                print(response.reason)
                print(response)

