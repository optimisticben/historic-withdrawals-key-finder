#!/usr/bin/env python3
import json

fName="ovm1_withdrawals_111521-kovan-orig.json"
with open(fName,'r') as dataFile:
  data=dataFile.read()

obj = json.loads(data)
outData = {}

#for i in range(0,len(obj.keys)):
for key, val in obj.items():
  # Get the keys from the entry
  # Coerce the keys to a list so that you can take the first element
  # entryKey = list(obj[i].keys())[0]
  # print(entryKey)
  outData[key.lower()] = val

json_object = json.dumps(outData, indent = 4)

# Writing to sample.json
with open("sample-kovan.json", "w") as outfile:
    outfile.write(json_object)

# with open('out.json', 'w') as outFile:
#   json.dump(outFile, outData)

# with open('out.jsont', 'w') as outfile:
#     json.dump(data, outfile)