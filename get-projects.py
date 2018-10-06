#!/usr/bin/python3

import requests as req
import pprint
from togglConstants import BASE_URL, WORKSPACE_ID, API_TOKEN, API_TOKEN_KEY

pp = pprint.PrettyPrinter(indent=4)

url = BASE_URL + 'workspaces/' + str(WORKSPACE_ID) + '/projects'

print('GET: ' + url)
response = req.get(url, auth=(API_TOKEN, API_TOKEN_KEY))
print(response)
pp.pprint(response.text)

