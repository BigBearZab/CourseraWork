import re
# import pandas as pd

# initialise empty dicts
error_dict = {}
user_dict = {}

# def dict_add(item, dict):
#     if item in dict.keys():

def findUser(line):
    return re.findall('\(.+\)', line)[0].strip("()")

def findError(line):
    return re.search("ERROR: ()[\w ']+) \(",line)[0].strip("ERROR: ").strip( " (")

for line in open('sys.log', 'r'):
    if 'INFO' in line:
        print('INFO ' + line)
        user = findUser(line)
        print(user)
    elif 'ERROR' in line:
        print('ERROR ' + line)
        user = findUser(line)
        print(user)
        print(findError(line))
