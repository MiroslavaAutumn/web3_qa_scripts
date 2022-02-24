import json
from web3 import Web3, HTTPProvider
import priv_keys

BROWSER_HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Geko/20100101 Firefox/69.0'}

ADMIN = priv_keys.ADMIN
ADMIN_PRIV = priv_keys.ADMIN_PRIV

USER = priv_keys.USER
USER_PRIV = priv_keys.USER_PRIV

USER_2 = priv_keys.USER_2
USER_2_PRIV = priv_keys.USER_2_PRIV

FACTORY_CROWDSALE = '0x8129A40EA8fA34C342b04BE1a9Ba379148F99D7F'
FACTORY_TOKEN = '0x568EE75009950B15e9e91a9A99DedF749f3AcBBf'

CELO = '0xF194afDf50B03e69Bd7D057c1Aa9e10c9954E4C9'
TOKEN_TO_SALE = '0xF13961823401A01bcC1b04176aa12Df226cA6172'

GAS_LIMIT = 3000000
GAS_PRICE = 1

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
    return Web3(HTTPProvider('https://alfajores-forno.celo-testnet.org/'))


def get_contract_abi():
    with open('Crowdsale_abi.json', 'r') as crowdsale_file:
        crowdsale_factory_abi = json.load(crowdsale_file)
    with open('Token_abi.json', 'r') as token_file:
        token_factory_abi = json.load(token_file)
    with open('Celo_token_abi.json', 'r') as celo_token_file:
        celo_token_abi = json.load(celo_token_file)
    return crowdsale_factory_abi, token_factory_abi, celo_token_abi