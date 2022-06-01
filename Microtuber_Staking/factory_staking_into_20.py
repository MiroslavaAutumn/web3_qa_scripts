import Microtuber_Staking.preset
from Microtuber_Staking.preset import sign_send_tx, web3_init, get_contract_abi
from datetime import datetime

def create_20_into_20_pool():
    web3 = web3_init()
    factory_staking_into_20_contract_abi = get_contract_abi(Microtuber_Staking.preset.FACTORY_STAKING_INTO_20)

    factory_staking_into_20_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_20),
        abi=factory_staking_into_20_contract_abi)

    reward_token_contract_abi = get_contract_abi(Microtuber_Staking.preset.REWARD_TOKEN_ERC_20)

    reward_token_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_20),
        abi=reward_token_contract_abi)

    start_time = int(datetime.now().timestamp()) + 60
    end_time = int(datetime.now().timestamp()) + 260
    reward_per_second = 1000000000000000000
    penalty_period = 120  # seconds
    fee_percentage = 10
    pool_rewards = (end_time - start_time) * reward_per_second

    approve_rewards = reward_token_contract.functions.approve(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_20,
        pool_rewards
    )
    tx_hash = sign_send_tx(web3, approve_rewards, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    create_staking_20_into_20 = factory_staking_into_20_contract.functions.createStaking20Into20(
        Microtuber_Staking.preset.STAKE_TOKEN_ERC_20,
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_20,
        start_time,
        end_time,
        reward_per_second,
        penalty_period,
        fee_percentage
    )

    tx_hash = sign_send_tx(web3, create_staking_20_into_20, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('create', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def create_20Plus20_into_20_pool():
    web3 = web3_init()
    factory_staking_into_20_contract_abi = get_contract_abi(Microtuber_Staking.preset.FACTORY_STAKING_INTO_20)

    factory_staking_into_20_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_20),
        abi=factory_staking_into_20_contract_abi)

    reward_token_contract_abi = get_contract_abi(Microtuber_Staking.preset.REWARD_TOKEN_ERC_20)

    reward_token_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_20),
        abi=reward_token_contract_abi)

    proportion = [1, 1]
    start_time = int(datetime.now().timestamp()) + 60
    end_time = int(datetime.now().timestamp()) + 260
    reward_per_second = 1000000000000000000
    penalty_period = 120  # seconds
    fee_percentage = 10
    pool_rewards = (end_time - start_time) * reward_per_second

    approve_rewards = reward_token_contract.functions.approve(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_20,
        pool_rewards
    )
    tx_hash = sign_send_tx(web3, approve_rewards, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    create_staking_20plus20_into_20 = factory_staking_into_20_contract.functions.createStaking20Plus20Into20(
        [Microtuber_Staking.preset.STAKE_TOKEN_ERC_20, Microtuber_Staking.preset.STAKE_TOKEN_ERC_20_2],
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_20,
        proportion,
        start_time,
        end_time,
        reward_per_second,
        penalty_period,
        fee_percentage
    )

    tx_hash = sign_send_tx(web3, create_staking_20plus20_into_20, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('create', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    #create_20_into_20_pool()
    create_20Plus20_into_20_pool()