import Talentum.preset
from Talentum.preset import web3_init, get_contract_abi

def read():
    web3 = web3_init()
    crowdsale_contract_abi = get_contract_abi(Talentum.preset.CROWDSALE)
    crowdsale_contract = web3.eth.contract(address=web3.toChecksumAddress(Talentum.preset.CROWDSALE),
                                           abi=crowdsale_contract_abi)

    price = crowdsale_contract.functions.price().call()
    print('Price', price)

    total_sold = crowdsale_contract.functions.totalSold().call()
    print('Total Sold', total_sold * 10 ** -18)

    stage = 0
    amounts_sold = crowdsale_contract.functions.amountsSold(stage).call()
    print('Amounts sold on stage', stage, amounts_sold)


if __name__ == '__main__':
    read()
