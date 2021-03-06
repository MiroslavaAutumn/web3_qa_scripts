import requests
from web3 import Web3, HTTPProvider
import secret

INFURA_PROJECT_ID = secret.INFURA_PROJECT_ID
BSCSCAN_API_KEY = secret.BSCSCAN_API_KEY
BROWSER_HEADERS = secret.BROWSER_HEADERS

OWNER = secret.OWNER
OWNER_PRIV = secret.OWNER_PRIV

USER = secret.USER
USER_PRIV = secret.USER_PRIV

USER_2 = secret.USER_2
USER_2_PRIV = secret.USER_2_PRIV

TOKEN_ADDRESS = '0x514b5EC40DF8e051dcD2f0bD58411c466528BD08'

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
    return Web3(HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545/'))


def get_contract_abi(contract_address):
    url = 'https://api-testnet.bscscan.com/api?module=contract&action=getabi&address=' \
          '{contract_address}&apikey={etherscan_api_key}'.format(
        contract_address=contract_address, etherscan_api_key=BSCSCAN_API_KEY)

    res = requests.get(url=url, headers=BROWSER_HEADERS)
    return res.json().get('result')
