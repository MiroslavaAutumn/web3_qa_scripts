import time

import Microtuber_vesting.preset
from Microtuber_vesting.preset import sign_send_tx, web3_init, get_contract_abi
from Microtuber_vesting.preset import ADDRESSES
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)


def vesting(address, priv):
    web3 = web3_init()
    vesting_contract_abi = get_contract_abi(Microtuber_vesting.preset.VESTING)

    vesting_contract = web3.eth.contract(address=web3.toChecksumAddress(Microtuber_vesting.preset.VESTING),
                                         abi=vesting_contract_abi)

    token_contract_abi = get_contract_abi(Microtuber_vesting.preset.TOKEN)

    token_contract = web3.eth.contract(address=web3.toChecksumAddress(Microtuber_vesting.preset.TOKEN),
                                       abi=token_contract_abi)

    claim = vesting_contract.functions.claim()

    tx_hash = sign_send_tx(web3, claim, address, priv)
    print('Claim', address, 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
    logging.info(f'Claim {address} https://testnet.bscscan.com/tx/{tx_hash.hex()}')

    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    event = token_contract.events.Transfer().processReceipt(tx_receipt)
    print('Claimed', event[0].args.value)
    logging.info(f'Claimed {event[0].args.value}')


if __name__ == '__main__':
    for i in range(48):
        logging.info(f'-------------STEP------------- {i}')
        for address, priv in ADDRESSES.items():
            try:
                if i == 5:  # пропускаем, чтоб в 6 получить за 5 и 6
                    continue
                if address != Microtuber_vesting.preset.SEEDBOX and i in range(27, 38): # пропускаем чтоб склеймить потом
                    continue
                else:
                    vesting(address, priv)

            except Exception as e:
                logging.error(f'ERROR {e}')
            if i == 2:  # Клеймим повторно после того как уже склеймили
                logging.info('повторный клейм')
                try:
                    vesting(address, priv)
                except Exception as e:
                    logging.error(f'ERROR {e}')
        time.sleep(120)
