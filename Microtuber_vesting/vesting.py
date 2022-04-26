import Microtuber_vesting.preset
from Microtuber_vesting.preset import sign_send_tx, web3_init, get_contract_abi

def vesting(address, priv, logger):
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
    logger.info(f'Claim {address} https://testnet.bscscan.com/tx/{tx_hash.hex()}')

    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    event = token_contract.events.Transfer().processReceipt(tx_receipt)
    print('Claimed', event[0].args.value)
    logger.info(f'Claimed {event[0].args.value}')
