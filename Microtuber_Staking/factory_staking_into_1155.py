import Microtuber_Staking.preset
from Microtuber_Staking.preset import sign_send_tx, web3_init, get_contract_abi
from datetime import datetime

def create_20plus1155_into_1155_pool():
    web3 = web3_init()
    factory_staking_into_1155_contract_abi = get_contract_abi(Microtuber_Staking.preset.FACTORY_STAKING_INTO_1155)

    factory_staking_into_1155_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_1155),
        abi=factory_staking_into_1155_contract_abi)

    reward_token_contract_abi = get_contract_abi(Microtuber_Staking.preset.REWARD_TOKEN_ERC_1155)

    reward_token_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_1155),
        abi=reward_token_contract_abi)

    start_time = int(datetime.now().timestamp()) + 60
    duration = [3600, 3600]
    stake_1155_id = 0
    reward_1155_id = 1
    reward_1155_amount = 1
    stake_20_amount = 1000000000000000000

    approve_rewards = reward_token_contract.functions.setApprovalForAll(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_1155,
        True
    )
    tx_hash = sign_send_tx(web3, approve_rewards, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    create_staking_20_plus_1155_into_1155 = factory_staking_into_1155_contract.functions.createStaking20Plus1155Into1155(
        Microtuber_Staking.preset.STAKE_TOKEN_ERC_20,
        stake_20_amount,
        Microtuber_Staking.preset.STAKE_TOKEN_ERC_1155,
        stake_1155_id,
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_1155,
        reward_1155_id,
        reward_1155_amount,
        start_time,
        duration
    )

    tx_hash = sign_send_tx(web3, create_staking_20_plus_1155_into_1155, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('create 20+1155=1155', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def create_20plus20_into_1155_pool():
    web3 = web3_init()
    factory_staking_into_1155_contract_abi = get_contract_abi(Microtuber_Staking.preset.FACTORY_STAKING_INTO_1155)

    factory_staking_into_1155_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_1155),
        abi=factory_staking_into_1155_contract_abi)

    reward_token_contract_abi = get_contract_abi(Microtuber_Staking.preset.REWARD_TOKEN_ERC_1155)

    reward_token_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_1155),
        abi=reward_token_contract_abi)

    start_time = int(datetime.now().timestamp()) + 60
    duration = [3600, 3600]
    reward_1155_id = 1
    reward_1155_amount = 1
    stake_20_amount = [1000000000000000000, 2000000000000000000]

    approve_rewards = reward_token_contract.functions.setApprovalForAll(
        Microtuber_Staking.preset.FACTORY_STAKING_INTO_1155,
        True
    )
    tx_hash = sign_send_tx(web3, approve_rewards, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    create_staking = factory_staking_into_1155_contract.functions.createStaking20Plus20Into1155(
        [Microtuber_Staking.preset.STAKE_TOKEN_ERC_20, Microtuber_Staking.preset.STAKE_TOKEN_ERC_20_2],
        stake_20_amount,
        Microtuber_Staking.preset.REWARD_TOKEN_ERC_1155,
        reward_1155_id,
        reward_1155_amount,
        start_time,
        duration
    )

    tx_hash = sign_send_tx(web3, create_staking, Microtuber_Staking.preset.OWNER,
                           Microtuber_Staking.preset.OWNER_PRIV)
    print('create 20+20=1155', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    create_20plus1155_into_1155_pool()
    create_20plus20_into_1155_pool()
