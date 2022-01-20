import Talentum.preset
from Talentum.preset import sign_send_tx, web3_init, get_contract_abi

#only for owner
#replace CUSTOM_TOKEN with the required one from the preset.py
def get_token():
    web3 = web3_init()
    crowdsale_contract_abi = get_contract_abi(Talentum.preset.CROWDSALE)

    crowdsale_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CROWDSALE),
                                           abi=crowdsale_contract_abi)

    get = crowdsale_contract.functions.getToken(Talentum.preset.CUSTOM_TOKEN)

    tx_hash = sign_send_tx(web3, get, Talentum.preset.ADMIN, Talentum.preset.ADMIN_PRIV)
    print('Get Token', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    get_token()
