
import json

representatives = json.loads(open('representatives.json').read())
out = open('representatives-ids.csv', 'wb')

out.write('id,n_answers\n')

for r in representatives:
    out.write(r['id'] + ',5\n')

out.close()
