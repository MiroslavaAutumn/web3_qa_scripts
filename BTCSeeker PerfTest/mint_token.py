import requests
from web3 import Web3, HTTPProvider
import secret
import json

INFURA_PROJECT_ID = secret.INFURA_PROJECT_ID
ETHERSCAN_API_KEY = secret.ETHERSCAN_API_KEY
BROWSER_HEADERS = secret.BROWSER_HEADERS

SENDER = secret.SENDER
SENDER_PRIV = secret.SENDER_PRIV

TOKEN_ADDRESS = '0x08b0dfe30438ef9b3d267d9618dfc5cf9dd83b5d'

GAS_LIMIT = 3000000
GAS_PRICE = 30


def sign_send_tx(web3_interface, contract_tx, address, priv):
    nonce = web3_interface.eth.get_transaction_count(address, 'pending')
    chain_id = web3_interface.eth.chainId

    tx_fields = {
        'chainId': chain_id,
        'gas': int(GAS_LIMIT),
        'gasPrice': web3_interface.toWei(GAS_PRICE, 'gwei'),
        'nonce': nonce,
    }

    tx = contract_tx.buildTransaction(tx_fields)
    signed = web3_interface.eth.account.sign_transaction(tx, priv)
    raw_tx = signed.rawTransaction
    tx_hash = web3_interface.eth.send_raw_transaction(raw_tx)
    web3_interface.eth.wait_for_transaction_receipt(tx_hash.hex())
    return tx_hash.hex()


def web3_init():
    return Web3(HTTPProvider('https://goerli.infura.io/v3/9accd918cd184f14a64be027e36d52da'))


def get_contract_abi(contract_address):
    url = 'https://api-goerli.etherscan.io/api?module=contract&action=getabi&address=' \
          '{contract_address}&apikey={etherscan_api_key}'.format(
        contract_address=contract_address, etherscan_api_key=ETHERSCAN_API_KEY)

    res = requests.get(url=url, headers=BROWSER_HEADERS)
    return res.json().get('result')


def mint_token():
    with open('address_list.json', 'r') as file:
        address_list = json.load(file)
    for address in address_list.keys():
        create_transaction(address)


def create_transaction(address):
    web3 = web3_init()
    token_abi = get_contract_abi(TOKEN_ADDRESS)
    token = web3.eth.contract(address=web3.toChecksumAddress(
        TOKEN_ADDRESS),
        abi=token_abi)

    amount = 100000 * 10 ** 18

    mint = token.functions.mint(
        address,
        amount
    )
    tx_hash = sign_send_tx(web3, mint, SENDER,
                           SENDER_PRIV)
    print('Mint', 'https://goerli.etherscan.io/tx/' + tx_hash)


if __name__ == '__main__':
    mint_token()
