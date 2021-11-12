from flask import Flask, abort, jsonify
import json

app = Flask(__name__)
def main():
    print("Starting up!")

def loadData(filename):
    print(f"Loading {filename}")
    with open(filename,'r') as dataFile:
        data=dataFile.read()
    obj = json.loads(data)
    return obj

keyData = loadData('fe9f9eba-process.json')

@app.route('/<string:key_id>')
def keyLookup(key_id):
    addressData = {}
    if key_id in keyData:
        addressData = keyData[key_id]
        return jsonify(addressData[0])
    else:
        return abort(404)
