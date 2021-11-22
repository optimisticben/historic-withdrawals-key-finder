from flask import Flask, abort, jsonify
from flask_cors import CORS
import json
import re
import os
import sys

if os.environ.get('DATA_FILE') is None:
    print(f'DATA_FILE envrionment variable is required')
    sys.exit(1)

app = Flask(__name__)
CORS(app)
ETH_ADDRESS_RE = re.compile(r'^0x[0-9a-fA-F]{40}$', re.IGNORECASE)

def main():
    print("Starting up!")

def loadData(filename):
    print(f"Loading {filename}")
    with open(filename,'r') as dataFile:
        data=dataFile.read()
    obj = json.loads(data)
    return obj

keyData = loadData(os.environ.get('DATA_FILE'))

@app.route('/<string:key_id>')
def keyLookup(key_id):
    if re.match(ETH_ADDRESS_RE, key_id) is None:
        return abort(404)
    addressData = {}
    lookup_key_id = key_id.lower()
    if lookup_key_id in keyData:
        addressData = keyData[lookup_key_id]
        return jsonify(addressData)
    else:
        return jsonify(list())
