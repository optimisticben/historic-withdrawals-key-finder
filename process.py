#!/usr/bin/env python3
import json

fName="fe9f9eba-remove-double-double-quotes.json"
with open(fName,'r') as dataFile:
  data=dataFile.read()

obj = json.loads(data)
outData = {}

for i in range(0,len(obj)):
  # Get the keys from the entry
  # Coerce the keys to a list so that you can take the first element
  entryKey = list(obj[i].keys())[0]
  print(entryKey)
  outData[entryKey.lower()] = obj[i][entryKey]

json_object = json.dumps(outData, indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# with open('out.json', 'w') as outFile:
#   json.dump(outFile, outData)

# with open('out.jsont', 'w') as outfile:
#     json.dump(data, outfile)