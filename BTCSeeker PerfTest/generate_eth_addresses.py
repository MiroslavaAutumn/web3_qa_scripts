from web3.auto import w3
import json

COUNT = 100  # Set your amount here

address_list = {}

for i in range(COUNT):
    new_account = w3.eth.account.create()
    a = address_list[new_account.address] = new_account.key.hex()[2:]

with open('address_list.json', 'w') as file:
    json.dump(address_list, file, indent=4, sort_keys=True)
