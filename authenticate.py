#!/usr/bin/python3

import requests as req
import pprint
from togglConstants import BASE_URL

pp = pprint.PrettyPrinter(indent=4)

url = BASE_URL + 'me';

print('GET: ' + url)
response = req.get(url, auth=('8a0956adb698e0e677e3f3249620369e','api_token'))

pp.pprint(response.text)

