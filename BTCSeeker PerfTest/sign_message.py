import requests
import json
from web3.auto import w3
from eth_account.messages import encode_defunct
import secret


def get_jwt_token():
    with open('address_list.json', 'r') as file:
        address_list = json.load(file)

    jwt_list = []

    for priv in address_list.values():
        jwt_list.append(sign(priv))

    with open('jwt_list.json', 'w') as file:
        json.dump(jwt_list, file, indent=4, sort_keys=True)


def sign(priv):
    base_uri = secret.BASE_URI
    msg = requests.get(f'{base_uri}/api/v1/auth/message').json().get('message')
    message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=priv)
    data = {'message': msg, 'signature': signed_message.signature.hex()}
    # print(data)
    res = requests.post(
        url=f'{base_uri}/api/v1/auth/jwt',
        data=json.dumps(data),
        headers={"Content-Type": 'application/json', 'accept': 'application/json'}
    )
    print(res.json())
    return res.json().get('token')


if __name__ == '__main__':
    get_jwt_token()