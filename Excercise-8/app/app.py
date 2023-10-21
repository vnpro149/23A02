from flask import Flask, request
import re, os

current_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

def sanitize_string(filename):
    if re.search('^[\w\-\.]+$', filename):
        pass
    else:
        raise ValueError(f'Can not use special characters in file name {filename}')

def cat(filename):
    sanitize_string(filename)
    try:
        with open(f'{current_path}/{filename}') as file:
           data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'No such file: {filename}')
    return data

@app.route('/')
def home():
    return 'Home page'

@app.route('/get_file')
def get_file():
    filename = request.args['filename']
    return '''Content of the file {} is...\n\n  {}'''.format(filename, cat(filename))

@app.errorhandler(ValueError)
def value_error(e):
    return f'<h1>{e}<h1>', 500

@app.errorhandler(FileNotFoundError)
def value_error(e):
    return f'<h1>{e}<h1>', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')

