import requests
from web3 import Web3, HTTPProvider
import secret

INFURA_PROJECT_ID = secret.INFURA_PROJECT_ID
BSCSCAN_API_KEY = secret.BSCSCAN_API_KEY
BROWSER_HEADERS = secret.BROWSER_HEADERS

TEAM = secret.TEAM
TEAM_PRIV = secret.TEAM_PRIV

INVESTORS = secret.INVESTORS
INVESTORS_PRIV = secret.INVESTORS_PRIV

COMPANY_RESERVE = secret.COMPANY_RESERVE
COMPANY_RESERVE_PRIV = secret.COMPANY_RESERVE_PRIV

MARKETING = secret.MARKETING
MARKETING_PRIV = secret.MARKETING_PRIV

BOUNTY = secret.BOUNTY
BOUNTY_PRIV = secret.BOUNTY_PRIV

SEEDBOX = secret.SEEDBOX
SEEDBOX_PRIV = secret.SEEDBOX_PRIV

ADDRESSES = {
    TEAM: TEAM_PRIV,
    INVESTORS: INVESTORS_PRIV,
    COMPANY_RESERVE: COMPANY_RESERVE_PRIV,
    MARKETING: MARKETING_PRIV,
    BOUNTY: BOUNTY_PRIV,
    SEEDBOX: SEEDBOX_PRIV
}

VESTING = '0x58cB6186554BA29471a6d73C6C17209dB8AD2F91'
TOKEN = '0xC016ade316C401fFFd2998Da3F00683b2D793350'

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
