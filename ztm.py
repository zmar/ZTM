import urllib
import json # baza jason
from pprint import pprint # baza jason

u = urllib.urlopen('')


with open('data.json') as data_file:    
    data = json.load(data_file)

pprint(data)
