import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi


def lottery_init():
    web3 = web3_init()
    token_abi = get_contract_abi(Lottery.preset.LOTTERY)
    lottery_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.LOTTERY),
        abi=token_abi)
    return lottery_contract, web3


def change_fake_time():
    lottery_contract, web3 = lottery_init()

    change_fake_time_listen = lottery_contract.functions.changeFakeTimeListen()
    tx_hash = sign_send_tx(web3, change_fake_time_listen, Lottery.preset.OWNER,
                           Lottery.preset.OWNER_PRIV)
    print('switch', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def set_next_day():
    lottery_contract, web3 = lottery_init()

    get_current_timestamp = lottery_contract.functions.fakeTimestamp().call()
    next_day = int(get_current_timestamp) + 86400

    change_fake_timestamp = lottery_contract.functions.changeFakeTimestamp(
        next_day
    )
    tx_hash = sign_send_tx(web3, change_fake_timestamp, Lottery.preset.OWNER,
                           Lottery.preset.OWNER_PRIV)
    print('next day', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    #set_next_day()
    change_fake_time()
