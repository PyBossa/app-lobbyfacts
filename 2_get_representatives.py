

import json
import requests

out = []

next = 'http://api.lobbyfacts.eu/api/1/representative?limit=500'

while next:
    print len(out)
    r = requests.get(next)
    res = json.loads(r.text)
    out += res['results']
    if 'next' in res:
        next = res['next']
    else:
        next = False

open('representatives.json', 'wb').write(json.dumps(out))

