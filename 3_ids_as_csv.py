
import json

representatives = json.loads(open('representatives.json').read())
out = open('representatives-ids.csv', 'wb')

out.write('id\n')

for r in representatives:
    out.write(r['id']+'\n')

out.close()