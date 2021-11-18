from flask import Flask, abort, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def main():
    print("Starting up!")

def loadData(filename):
    print(f"Loading {filename}")
    with open(filename,'r') as dataFile:
        data=dataFile.read()
    obj = json.loads(data)
    return obj

keyData = loadData('ovm1_withdrawals_111521-kovan.json')

@app.route('/<string:key_id>')
def keyLookup(key_id):
    addressData = {}
    lookup_key_id = key_id.lower()
    if lookup_key_id in keyData:
        addressData = keyData[lookup_key_id]
        return jsonify(addressData)
    else:
        return abort(404)
