#!/usr/bin/python3

import requests as req
import pprint
import json
import sys
from togglconstants import BASE_URL, PROJECTS, API_TOKEN, API_TOKEN_KEY

pp = pprint.PrettyPrinter(indent=4)

projectName = sys.argv[1];
if not projectName:
    print('trying to start timer without a project')
    exit()

requestHeaders = {
    'Content-Type': 'application/json'
}

data = {
    'time_entry': {
        'description': '',
        'tags': [],
        'pid': PROJECTS[projectName],
        'created_with': 'curl'
    }
}

requestBody = eval(json.dumps(data))
print(requestBody)

url = BASE_URL + 'time_entries/start';
print(url)

response = req.post(url, auth=(API_TOKEN, API_TOKEN_KEY), headers=requestHeaders, json=requestBody)
print(response)
pp.pprint(response.text)

