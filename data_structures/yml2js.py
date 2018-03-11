#!/usr/bin/env python

import yaml
import os
import json
import sys
from pprint import pprint

# Read YAML and change to Python Data Strucutre
with open(sys.argv[1]) as f:
    text = f.read()

# takes a YAML document and transfer it to Python Object
py_obj = yaml.load(text)

# Read Python Data Strucure and convert it to JSON
json_obj = json.dumps(py_obj,indent=2,separators=(',',':'))

## Print Python Data Strucutre
print ('##### Python Object ######')
pprint (py_obj)

## Print YAML Data Strucutre
print ('##### YAML Document ######')
print text
#print yaml.dump(py_obj,default_flow_style = False)

## Print JSON Data Structure
print ('##### JSON DATA Strucutre ######')
print json.dumps(py_obj,indent=2,separators=(',',':'))

## Print Type of YAML Data Structure
print ('##### Type of YAML DATA Strucutre ######')
print type(py_obj)

## Print Type of JSON Data Structure
print ('##### Type of JSON DATA Strucutre ######')
json_obj = json.dumps(py_obj,indent=2,separators=(',',':'))
print type(json.loads(json_obj))

