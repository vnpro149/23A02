from flask import Flask,request
app = Flask(__name__)
@app.route('/get_file', methods=['GET'])
def get_file():
    filename = request.args['filename']
    return '''Content of the file {} is...\n\n {}'''.format(filename, cat(filename))
def cat(filename):
    with open(filename) as file:
        data = file.read()
        return data
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"))

    