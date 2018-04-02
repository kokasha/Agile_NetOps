#!/usr/bin/python

import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import re
from pprint import pprint
from netaddr import *


ENV = Environment(loader=FileSystemLoader('.'),trim_blocks=True,lstrip_blocks=True)
ENV.filters['ipaddr'] = IPNetwork

filename = re.sub('\.\w+$','',sys.argv[1])

print ('--- Reading YAML file '+filename+'.yml ---')
#with open(filename + '.yaml') as _: yamldict = yaml.load(_)
with open (filename + '.yaml') as _: text = _.read()
yamldict = yaml.load(text)
print ('--- YAML dictionary in '+filename+'.yml ---')
#pprint(yamldict)
print (text)

print ('--- Rendering template '+filename+'.j2 ---')
template = ENV.get_template(filename + ".j2")
print(template.render(**yamldict))
