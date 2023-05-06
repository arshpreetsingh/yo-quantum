import json

# Read API key from Json
def get_api_key():
    with open('config.json') as f:
        MY_API_KEY = json.load(f)
    return MY_API_KEY['key']
