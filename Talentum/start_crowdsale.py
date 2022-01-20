import Talentum.preset
from Talentum.preset import sign_send_tx, web3_init, get_contract_abi

def start_crowdsale():
    web3 = web3_init()
    crowdsale_contract_abi = get_contract_abi(Talentum.preset.CROWDSALE)

    crowdsale_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CROWDSALE),
                                           abi=crowdsale_contract_abi)

    start = crowdsale_contract.functions.start()

    tx_hash = sign_send_tx(web3, start, Talentum.preset.ADMIN, Talentum.preset.ADMIN_PRIV)
    print('Start', 'https://testnet.bscscan.com/tx/'+tx_hash.hex())


if __name__ == '__main__':
    start_crowdsale()
