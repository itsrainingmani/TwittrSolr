import json, io
from pprint import pprint

json_file = 'mess.json'

jso = open(json_file, 'r')
data = json.load(jso)
jso.close()

for i in data:
    i["created_at"] += "Z"

with io.open('newmess.json', 'w', encoding='utf8') as json_file:
    dat = json.dumps(data, ensure_ascii=False, encoding='utf8')
    json_file.write(unicode(dat))
#data[0]["created_at"] += "Z"
#print data[0]["created_at"]
