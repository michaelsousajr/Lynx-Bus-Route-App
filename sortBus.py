import json
from optparse import Values 

info = open('buses.json',)
res = json.load(info)

sorted = json.dumps(res, sort_keys=True)
print(format(sorted))
