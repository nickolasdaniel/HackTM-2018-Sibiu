from flask import Flask, request, jsonify
import requests
import base64
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'PUT'])
def send_rotate():
    with open('c.jpeg', 'rb') as imagesFile:
        imagestr = base64.b64encode(imagesFile.read())

    if request.method == 'GET':
        header = {"Content-Type" : "application/octet-stream"}
        response = requests.put('http://192.168.86.105:9999', headers=header, json=imagestr)
        print(jsonify(response))

    if request.method == 'PUT':
        header = {"Content-Type" : "text/plain"}
        response = requests.get('http://192.168.86.105:9999', headers=header).content
        print(jsonify(response))

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port = 9999)
