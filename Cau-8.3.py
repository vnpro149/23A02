import re
def sanitize_string(filename):
    if re.search('^[\w\-\.]+$', filename):
        pass
    else:
        raise ValueError('Can not use special characters')
def cat(filename): 
    sanitize_string(filename)
    with open(filename) as file:
        data = file.read()
        return data
