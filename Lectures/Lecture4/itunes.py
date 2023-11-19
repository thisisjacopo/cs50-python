import json
import requests
import sys

base_url = 'https://itunes.apple.com/search?entity=song&limit=10&term='

if len(sys.argv) != 2:
    sys.exit("Too few arguments.")
    
response = requests.get(f"{base_url}{sys.argv[1]}")

res = response.json()

for result in res['results']:
    print(result['trackName'])
