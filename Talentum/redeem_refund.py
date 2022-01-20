import Talentum.preset
from Talentum.preset import sign_send_tx, web3_init, get_contract_abi


def redeem():
    web3 = web3_init()
    crowdsale_contract_abi = get_contract_abi(Talentum.preset.CROWDSALE)

    crowdsale_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CROWDSALE),
                                           abi=crowdsale_contract_abi)

    redeem = crowdsale_contract.functions.redeem()

    tx_hash = sign_send_tx(web3, redeem, Talentum.preset.USER, Talentum.preset.USER_PRIV)
    print('Redeem', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    redeem()


#def refund():
#    web3 = web3_init()
#    crowdsale_contract_abi = get_contract_abi(Talentum.preset.CROWDSALE)
#
#    crowdsale_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CROWDSALE),
#                                           abi=crowdsale_contract_abi)
#
#    refund = crowdsale_contract.functions.refund()
#
#    tx_hash = sign_send_tx(web3, refund, Talentum.preset.USER, Talentum.preset.USER_PRIV)
#    print('Refund', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
#
#
#if __name__ == '__main__':
#    refund()
