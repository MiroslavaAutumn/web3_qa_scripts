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

FACTORY_STAKING_INTO_20 = '0x0753A20Cdb660a16B2010f1fcED8E999C63F3cC4'
FACTORY_STAKING_INTO_1155 = '0x623D6201C6756470Df0fcD447c1EB3980529DB5C'

STAKE_TOKEN_ERC_20 = '0xB1BF76226F903e3d257C5b0390cdcfeC094CD751'  # vrk test token, 18 decimals
STAKE_TOKEN_ERC_20_2 = '0xd584e695D6bc250084D1FC472792A2E0E1303D4C'  # Kchay test token 8 decimals
REWARD_TOKEN_ERC_20 = '0xC016ade316C401fFFd2998Da3F00683b2D793350'  # rec test token 18 decimals

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
