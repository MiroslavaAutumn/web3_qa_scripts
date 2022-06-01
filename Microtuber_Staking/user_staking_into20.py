import Microtuber_Staking.preset
from Microtuber_Staking.preset import sign_send_tx, web3_init, get_contract_abi


def stake_20_into_20():
    web3 = web3_init()
    pool_contract_address = ''

    pool_contract_abi = get_contract_abi(pool_contract_address)
    pool_contract = web3.eth.contract(address=web3.toChecksumAddress(pool_contract_address),
                                      abi=pool_contract_abi)

    stake_token_contract_abi = get_contract_abi(Microtuber_Staking.preset.STAKE_TOKEN_ERC_20)
    stake_token_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.STAKE_TOKEN_ERC_20),
        abi=stake_token_contract_abi)

    approve_token = stake_token_contract.functions.approve(
        pool_contract_address,
        10000 * (10 ** 18)
    )
    tx_hash = sign_send_tx(web3, approve_token, Microtuber_Staking.preset.USER,
                           Microtuber_Staking.preset.USER_PRIV)
    print('approve token ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    deposit = pool_contract.functions.deposit(
        1000 * 10 ** 18
    )
    tx_hash = sign_send_tx(web3, deposit, Microtuber_Staking.preset.USER,
                           Microtuber_Staking.preset.USER_PRIV)
    print('Deposit 20', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def stake_20plus20_into_20():
    web3 = web3_init()
    pool_contract_address = ''
    pool_contract_abi = get_contract_abi(pool_contract_address)

    pool_contract = web3.eth.contract(address=web3.toChecksumAddress(pool_contract_address),
                                      abi=pool_contract_abi)

    stake_token_1_contract_abi = get_contract_abi(Microtuber_Staking.preset.STAKE_TOKEN_ERC_20)
    stake_token_1_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.STAKE_TOKEN_ERC_20),
        abi=stake_token_1_contract_abi)

    stake_token_2_contract_abi = get_contract_abi(Microtuber_Staking.preset.STAKE_TOKEN_ERC_20_2)
    stake_token_2_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.STAKE_TOKEN_ERC_20_2),
        abi=stake_token_2_contract_abi)

    approve_token_1 = stake_token_1_contract.functions.approve(
        pool_contract_address,
        10000 * (10 ** 18)
    )
    tx_hash = sign_send_tx(web3, approve_token_1, Microtuber_Staking.preset.USER,
                           Microtuber_Staking.preset.USER_PRIV)
    print('approve token1 ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    approve_token_2 = stake_token_2_contract.functions.approve(
        pool_contract_address,
        10000 * (10 ** 18)
    )
    tx_hash = sign_send_tx(web3, approve_token_2, Microtuber_Staking.preset.USER,
                           Microtuber_Staking.preset.USER_PRIV)
    print('approve token2 ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    deposit = pool_contract.functions.deposit(
        1000 * (10 ** 18)
    )
    tx_hash = sign_send_tx(web3, deposit, Microtuber_Staking.preset.USER,
                           Microtuber_Staking.preset.USER_PRIV)
    print('Deposit 20+20', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def withdraw_20():
    web3 = web3_init()
    pool_contract_address = ''
    pool_contract_abi = get_contract_abi(pool_contract_address)

    pool_contract = web3.eth.contract(address=web3.toChecksumAddress(pool_contract_address),
                                      abi=pool_contract_abi)

    withdraw = pool_contract.functions.withdraw(
        1000 * 10 ** 18
    )
    tx_hash = sign_send_tx(web3, withdraw, Microtuber_Staking.preset.USER,
                           Microtuber_Staking.preset.USER_PRIV)
    print('Withdraw', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    stake_20_into_20()
    stake_20plus20_into_20()
    #withdraw_20()
