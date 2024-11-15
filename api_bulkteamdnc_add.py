import requests
import json
import csv
import time

##Script to find current calls for a specific Ringover account. First you need to create an API key on that account.

print('''


This script takes a CSV file named numbers.csv with numbers and uploads it to the DNC team list using the Ringover API:


''')

infra = 0
# while (infra != 1) and (infra !=2):
while True:
    infra = input("Press 1 for US and 2 for EU: ")
    try:
        infra = int(infra)
    except:
        print("Invalid option, please try again.\n")
    if infra == 1:
        url = "https://public-api-us.ringover.com/v2/blacklists/numbers"
        break
    elif infra == 2:
        url = "https://public-api.ringover.com/v2/blacklists/numbers"
        break


option_direction = 0
while (option_direction != 1) and (option_direction !=2):
    option_direction = input("Which direction is the block? Press 1 to block IN or 2 to block OUT (this will affect all the numbers): ")
    try:
        option_direction = int(option_direction)
    except:
        print("Invalid option, please try again.\n")
    if option_direction == 1:
        direction = "IN"
        break
    elif option_direction == 2:
        direction = "OUT"
        break

api_key = input("What is the API Key of the account?: ")



with open('numbers.csv', newline='') as csvfile:
    numbers = csv.reader(csvfile)
    for number in numbers:
        print(number[0])
        payload = json.dumps({
            "number": int(number[0]),  # from the CSV file
            "comment": "CSV bulk",
            "direction": direction  # from the CSV file
        })

        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        time.sleep(0.5) #Delay because API rate limit is 2 calls per second




print("Finish uploading!")




