import time
import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi
import Lottery.secret


def lottery_init():
    web3 = web3_init()
    token_abi = get_contract_abi(Lottery.preset.LOTTERY)
    lottery_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.LOTTERY),
        abi=token_abi)
    return lottery_contract, web3


def change_fake_time():
    lottery_contract, web3 = lottery_init()
    web3 = web3_init()

    get_fake_time_status = lottery_contract.functions.fakeTimeListen().call()
    print(get_fake_time_status)

    if get_fake_time_status == False:
        change_fake_time_listen = lottery_contract.functions.changeFakeTimeListen()
        tx_hash = sign_send_tx(web3, change_fake_time_listen, Lottery.secret.USER_1,
                               Lottery.secret.USER_1_PRIV)
        print('switch', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
    else:
        print('Status is already true')


def set_next_day():
    lottery_contract, web3 = lottery_init()

    get_current_timestamp = lottery_contract.functions.fakeTimestamp().call()
    print(get_current_timestamp)
    if get_current_timestamp == 0:
        ts_now = int(time.time())
        next_day = ts_now + 86400
        print(next_day, 'First time set')
    else:
        next_day = int(get_current_timestamp) + 86400
        print('Time set', next_day)

    change_fake_timestamp = lottery_contract.functions.changeFakeTimestamp(
        next_day
    )
    tx_hash = sign_send_tx(web3, change_fake_timestamp, Lottery.secret.USER_1,
                           Lottery.secret.USER_1_PRIV)
    print('next day', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def set_custom_day():
    lottery_contract, web3 = lottery_init()

    custom_timestamp = 1677686400

    change_fake_timestamp = lottery_contract.functions.changeFakeTimestamp(
        custom_timestamp
    )
    tx_hash = sign_send_tx(web3, change_fake_timestamp, Lottery.secret.USER_1,
                           Lottery.secret.USER_1_PRIV)
    print('custom day', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    #set_next_day()
    #change_fake_time()
    set_custom_day()
