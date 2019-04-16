import json

with open('./000.json','r') as f:
    content = f.read()
d = json.loads(content)

print(d['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']) 

print(d.get('GlossSeeAlso')) # print(d['glossary'])

d['age'] = 20
d['glossary']['title'] = 'my glossary'


print(d)



