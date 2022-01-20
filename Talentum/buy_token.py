import time
import Talentum.preset
from Talentum.preset import sign_send_tx, web3_init, get_contract_abi
import requests

#replace all CUSTOM_TOKEN with the required one from the preset.py
def buy_token():
    web3 = web3_init()
    token_contract_abi = get_contract_abi(Talentum.preset.CUSTOM_TOKEN)
    crowdsale_contract_abi = get_contract_abi(Talentum.preset.CROWDSALE)

    token_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CUSTOM_TOKEN),
                                       abi=token_contract_abi)
    crowdsale_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CROWDSALE),
                                           abi=crowdsale_contract_abi)

    amount_to_pay = 300 * 10 ** 18

    #approve tokens for use by a smart contract
    approve = token_contract.functions.approve(
        Talentum.preset.CROWDSALE,
        amount_to_pay
    )
    tx_hash = sign_send_tx(web3, approve, Talentum.preset.USER, Talentum.preset.USER_PRIV)
    print('Approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    time.sleep(5)

    #getting amount_to_receive, signature_expiration_timestamp and signature from backend
    signature_params = {'token_address': Talentum.preset.CUSTOM_TOKEN,
                        'amount_to_pay': str(amount_to_pay)}
    result = requests.post(url='swagger url', #add swagger url
                           data=signature_params)
    function_data = result.json()

    print(int(function_data.get('amount_to_receive')) * 10 ** -18)

    #buy tokens
    buy = crowdsale_contract.functions.buy(
        Talentum.preset.CUSTOM_TOKEN,
        amount_to_pay,
        int(function_data.get('amount_to_receive')),
        int(function_data.get('signature_expiration_timestamp')),
        function_data.get('signature')
    )

    tx_hash = sign_send_tx(web3, buy, Talentum.preset.USER, Talentum.preset.USER_PRIV)
    print('Buy', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    buy_token()
