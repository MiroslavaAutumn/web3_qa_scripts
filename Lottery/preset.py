import requests
from web3 import Web3, HTTPProvider
import secret

INFURA_PROJECT_ID = secret.INFURA_PROJECT_ID
BSCSCAN_API_KEY = secret.BSCSCAN_API_KEY
BROWSER_HEADERS = secret.BROWSER_HEADERS

FACTORY = '0x800516F78e730D1e2c671EFb0071254A7517d046'
LOTTERY = '0x4842954941317DDB0a106DFFC8cf2DD9FbE97227'
TOKEN = '0xf7dFbf73bf9393598664EFE3d13829AdaCAFc167'

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
    return web3_interface.eth.send_raw_transaction(raw_tx)


def web3_init():
    return Web3(HTTPProvider('https://bsc.getblock.io/4ed994ca-64fc-42fb-933c-914c004550a5/testnet/'))


def get_contract_abi(contract_address):
    url = 'https://api-testnet.bscscan.com/api?module=contract&action=getabi&address=' \
          '{contract_address}&apikey={etherscan_api_key}'.format(
        contract_address=contract_address, etherscan_api_key=BSCSCAN_API_KEY)

    res = requests.get(url=url, headers=BROWSER_HEADERS)
    return res.json().get('result')
