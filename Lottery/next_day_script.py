import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi


def set_next_day():
    web3 = web3_init()
    lottery_contract_abi = get_contract_abi(Lottery.preset.LOTTERY)
    lottery_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.LOTTERY),
        abi=lottery_contract_abi)

    get_current_timestamp = lottery_contract.functions.fakeTimestamp().call()
    next_day = int(get_current_timestamp) + 86400

    change_fake_timestamp = lottery_contract.functions.changeFakeTimestamp(
        next_day

    )
    tx_hash = sign_send_tx(web3, change_fake_timestamp, Lottery.preset.OWNER,
                           Lottery.preset.OWNER_PRIV)
    print('next day', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    set_next_day()
