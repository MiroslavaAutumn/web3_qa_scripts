import CBlock.preset
from CBlock.preset import sign_send_tx, web3_init


def scanner_test():
    web3 = web3_init()
    crowdsale_factory_abi, token_factory_abi, celo_token_abi = CBlock.preset.get_contract_abi()

    crowdsale_factory_contract = web3.eth.contract(address=web3.toChecksumAddress(CBlock.preset.FACTORY_CROWDSALE),
                                                   abi=crowdsale_factory_abi)
    token_factory_contract = web3.eth.contract(address=web3.toChecksumAddress(CBlock.preset.FACTORY_TOKEN),
                                               abi=token_factory_abi)
    celo_token_contract = web3.eth.contract(address=web3.toChecksumAddress(CBlock.preset.CELO),
                                            abi=celo_token_abi)

    price_token_factory = token_factory_contract.functions.price(
        CBlock.preset.CELO, 0).call()
    (print('t price', price_token_factory))

    price_crowdsale_factory = crowdsale_factory_contract.functions.price(
        CBlock.preset.CELO, 0).call()
    print('c price', price_crowdsale_factory)

    # approve tokens for use by a TOKEN FACTORY smart contract

    approve = celo_token_contract.functions.approve(
        CBlock.preset.FACTORY_TOKEN,
        price_token_factory
    )
    tx_hash = sign_send_tx(web3, approve, CBlock.preset.ADMIN, CBlock.preset.ADMIN_PRIV)
    print('Approve', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())

    create_token = token_factory_contract.functions.deployERC20PausableToken(
        [CBlock.preset.CELO, CBlock.preset.ADMIN],  # token to pay to deploy token and owner address
        str('stresstoken'),  # token name
        str('STRT'),  # token symbol
        int('18'),  # token decimals
        [CBlock.preset.ADMIN],  # token owner
        [int('100000000000000000000000')]  # init supply
    )
    tx_hash = sign_send_tx(web3, create_token, CBlock.preset.ADMIN, CBlock.preset.ADMIN_PRIV)
    print('create token', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())

    # approve tokens for use by a CROWDSALE FACTORY smart contract
    approve = celo_token_contract.functions.approve(
        CBlock.preset.FACTORY_CROWDSALE,
        price_token_factory
    )
    tx_hash = sign_send_tx(web3, approve, CBlock.preset.ADMIN, CBlock.preset.ADMIN_PRIV)
    print('Approve', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())

    create_crowdsale = crowdsale_factory_contract.functions.deployNonSoftCappableCrowdsale(
        [CBlock.preset.CELO, CBlock.preset.ADMIN],  # token to pay to deploy token and owner address
        CBlock.preset.TOKEN_TO_SALE,  # token to sale
        int('18'),  # token decimals
        int('86400'),  # duration
        [CBlock.preset.CELO],  # token to pay
        [int('1000000000000000000')],  # token rate
        [0, 0]  # limits
    )
    tx_hash = sign_send_tx(web3, create_crowdsale, CBlock.preset.ADMIN, CBlock.preset.ADMIN_PRIV)
    print('create crowdsale', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())


if __name__ == '__main__':
    scanner_test()
