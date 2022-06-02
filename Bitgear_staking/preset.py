import requests
from web3 import Web3, HTTPProvider
import secret

INFURA_PROJECT_ID = secret.INFURA_PROJECT_ID
ETHERSCAN_API_KEY = secret.ETHERSCAN_API_KEY
BROWSER_HEADERS = secret.BROWSER_HEADERS

OWNER = secret.OWNER
OWNER_PRIV = secret.OWNER_PRIV

USER = secret.USER
USER_PRIV = secret.USER_PRIV

USER_2 = secret.USER_2
USER_2_PRIV = secret.USER_2_PRIV

COIN_STAKING = '0x52Ec8c87FC09C1eF75fAe44139cE8A0A425f9B40'
TOKEN_VAULT = '0xdf0E7F1df4BCA344e006428B59321653bC0b5daF'

GEAR_TOKEN = '0x080d1263989C08430b85f864C100eE63d67D499D'
LP_TOKEN = '0xa43FDccF4d23D5eC7b6F2F946e2Dd17A9B6C1E8D'

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
    url = 'https://api-rinkeby.etherscan.io/api?module=contract&action=getabi&address=' \
          '{contract_address}&apikey={etherscan_api_key}'.format(
        contract_address=contract_address, etherscan_api_key=ETHERSCAN_API_KEY)

    res = requests.get(url=url, headers=BROWSER_HEADERS)
    return res.json().get('result')

