import json
from googlesearch import *

sr = Search("DRW")
sr.load()
mapped = sr.as_dict()
print(type(mapped))
print(sr.as_dict())
