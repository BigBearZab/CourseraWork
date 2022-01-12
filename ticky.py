import re
# import pandas as pd

# initialise empty dicts
error_dict = {}
user_dict = {}

# def dict_add(item, dict):
#     if item in dict.keys():

def findUser(line):
    username = re.search('\((.+)\)', line)
    if username:
        return username.group(1)

def findError(line):
    error = re.search("ERROR: ([\w ]+) \(", line)
    if error:
        return error.group(1)

for line in open('sys.log', 'r'):
    if 'INFO' in line:
        user = findUser(line)
        print(user)
        if user in user_dict.keys():
            user_dict[user]['INFO'] += 1
        else:
             user_dict[user] = {'INFO':1,'ERROR':0}

    elif 'ERROR' in line:
        user = findUser(line)
        print(user)
        if user in user_dict.keys():
            user_dict[user]['ERROR'] += 1
        else:
             user_dict[user] = {'INFO':0,'ERROR':1}
        print(findError(line))
        error = findError(line)
        if error in error_dict.keys():
            error_dict[error] += 1
        else:
            error_dict[error] = 1

print(error_dict)
print(user_dict)
