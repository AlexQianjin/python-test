import os
from dotenv import load_dotenv
load_dotenv()

import json
import requests
from datetime import datetime
import utils.config as config

print(config.TEST_ENV_URL)

TEAMS_WEBHOOK_URL = os.getenv('TEAMS_WEBHOOK_URL')
print(TEAMS_WEBHOOK_URL)

data = {"text":"Hello World!"}
headers = {'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': str(len(data))}   
r = requests.post(TEAMS_WEBHOOK_URL, data=json.dumps(data)) 
print(r.text)
print(r.status_code)
