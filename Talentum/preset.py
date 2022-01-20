import requests
from web3 import Web3, HTTPProvider
import priv_keys

INFURA_PROJECT_ID = priv_keys.INFURA_PROJECT_ID
BSCSCAN_API_KEY = priv_keys.BSCSCAN_API_KEY
BROWSER_HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Geko/20100101 Firefox/69.0'}

ADMIN = priv_keys.ADMIN
ADMIN_PRIV = priv_keys.ADMIN_PRIV

USER = priv_keys.USER  #0xc36
USER_PRIV = priv_keys.USER_PRIV

USER_2 = priv_keys.USER_2 #0xD51
USER_2_PRIV = priv_keys.USER_2_PRIV

CROWDSALE = ''
VESTING = ''
TOKEN = ''

USDT = ''
BUSD = ''
WETH = ''
BNB = ''
CUSTOM_TOKEN = ''

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
        #Если надо купить за bnb - передаем сюда, при этом в buy_tokens.py в amount_to_pay ставим 0
        #'value': 10 ** 18
    }

    tx = contract_tx.buildTransaction(tx_fields)
    signed = web3_interface.eth.account.sign_transaction(tx, priv)
    raw_tx = signed.rawTransaction
    return web3_interface.eth.send_raw_transaction(raw_tx)


def web3_init():
    return Web3(HTTPProvider('https://data-seed-prebsc-1-s2.binance.org:8545/'))


def get_contract_abi(contract_address):
    url = 'https://api-testnet.bscscan.com/api?module=contract&action=getabi&address=' \
          '{contract_address}&apikey={etherscan_api_key}'.format(
        contract_address=contract_address, etherscan_api_key=BSCSCAN_API_KEY)

    res = requests.get(url=url, headers=BROWSER_HEADERS)
    return res.json().get('result')
