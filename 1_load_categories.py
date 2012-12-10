import re
import requests
from bs4 import BeautifulSoup
import json

r = requests.get('http://www.opensecrets.org/lobby/list_indus.php')
s = BeautifulSoup(r.text)

links = s.find_all('a', href=re.compile("/lobby/indus(client|code|)\.php\?id="))

categories = []


for a in links:
    m = re.search("\?id=([^&]+)", a['href'])
    category = dict(id=m.group(1), title=a.text.strip(), url=a['href'])
    if 'induscode' in a['href']:
        if 'children' not in categories[-1]:
            # creating a fake parent w/o id and title
            categories[-1]['children'] = [dict(children = [])]
        p = categories[-1]['children'][-1]
        if 'children' in p:
            parent = p['children']
        else:
            parent = p['children'] = []
    elif 'indusclient' in a['href']:
        p = categories[-1]
        if 'children' in p:
            parent = p['children']
        else:
            parent = p['children'] = []
    else:
        parent = categories
    parent.append(category)


open('categories.json', 'wb').write(json.dumps(categories))