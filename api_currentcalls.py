import requests
import json

##Script to find current calls for a specific Ringover account. First you need to create an API key on that account.

print('''


This script helps you find the current calls for an account:


''')

infra = 0
while (infra != 1) and (infra !=2):
    infra = int(input("Press 1 for US and 2 for EU: "))
    if infra == 1:
        url = "https://public-api-us.ringover.com/v2/calls/current"
    elif infra == 2:
        url = "https://public-api.ringover.com/v2/calls/current"

api_key = input("What is the API Key of the account?: ")

payload = "{\n  \"status\": [\n    \"ANSWERED\",\n    \"RINGING\"\n  ],\n  \"interface\": null,\n  \"direction\": null,\n  \"advanced\": null,\n    \"groups\": null,\n    \"users\": null\n  },\n  \"limit_count\": 1,\n  \"limit_offset\": 0\n}"
headers = {
  'Authorization': api_key,
  'Content-Type': 'application/json'
}

try:
    response = requests.request("POST", url, headers=headers, data=payload)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)


API_Data = response.json()
print(json.dumps(API_Data, indent=4, sort_keys=True))

