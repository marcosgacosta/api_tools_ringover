import requests
import json
import csv
import time


##Script to find current calls for a specific Ringover account. First you need to create an API key on that account.

print('''


This script takes a CSV file named numbers.csv with numbers and removes them from the DNC team list using the Ringover API:


''')

infra = 0
while (infra != 1) and (infra !=2):
    infra = int(input("Press 1 for US and 2 for EU: "))
    if infra == 1:
        url = "https://public-api-us.ringover.com/v2/blacklists/numbers/"
    elif infra == 2:
        url = "https://public-api.ringover.com/v2/blacklists/numbers/"


api_key = input("What is the API Key of the account?: ")

with open('numbers.csv', newline='') as csvfile:
    numbers = csv.reader(csvfile)
    for number in numbers:
        print(number[0])
        payload = {}
        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request("DELETE", url + number[0], headers=headers, data=payload)

            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        time.sleep(0.5) #Delay to respect API rate / 2 calls per second



print("Finish uploading!")

#US_19a1d8fcc58e56fcc9d469cbc930caa4273bc



