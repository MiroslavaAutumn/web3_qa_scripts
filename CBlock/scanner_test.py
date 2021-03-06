import time
import CBlock.preset
from CBlock.preset import sign_send_tx, web3_init
import datetime

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
    token_random_user, t_private_key = CBlock.preset.get_random_user()
    def token_approve():
        approve = celo_token_contract.functions.approve(
            CBlock.preset.FACTORY_TOKEN,
            price_token_factory
        )
        tx_hash = sign_send_tx(web3, approve, token_random_user, t_private_key)
        print('Approve', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash.hex())
        if tx_receipt.get('status'):
            with open('error_log.txt', 'a') as error_file:
                error_file.write(f'"A" Token approve transaction status is success {datetime.datetime.now()}\r\n')
    try:
        token_approve()
    except:
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f'"B" Token approve failed at {datetime.datetime.now()}\r\n')
        token_approve()

    def create_token():
        create_token = token_factory_contract.functions.deployERC20PausableToken(
            [CBlock.preset.CELO, token_random_user],  # token to pay to deploy token and owner address
            str('stresstoken'),  # token name
            str('STRT'),  # token symbol
            int('18'),  # token decimals
            [token_random_user],  # token owner
            [int('100000000000000000000000')]  # init supply
        )
        tx_hash = sign_send_tx(web3, create_token, token_random_user, t_private_key)
        print('create token', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash.hex())
        if tx_receipt.get('status'):
            with open('error_log.txt', 'a') as error_file:
                error_file.write(f'"A" Token transaction status is success {datetime.datetime.now()}\r\n')
    try:
        create_token()
    except:
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f'"B" Token creation failed at {datetime.datetime.now()}\r\n')
        create_token()

    crowdsale_random_user, c_private_key = CBlock.preset.get_random_user()
    def crowdsale_approve():
        # approve tokens for use by a CROWDSALE FACTORY smart contract
        approve = celo_token_contract.functions.approve(
            CBlock.preset.FACTORY_CROWDSALE,
            price_token_factory
        )
        tx_hash = sign_send_tx(web3, approve, crowdsale_random_user, c_private_key)
        print('Approve', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash.hex())
        if tx_receipt.get('status'):
            with open('error_log.txt', 'a') as error_file:
                error_file.write(f'"A" Crowdsale approve transaction status is success {datetime.datetime.now()}\r\n')
    try:
        crowdsale_approve()
    except:
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f'"B" Crowdsale approve failed at {datetime.datetime.now()}\r\n')
        crowdsale_approve()

    def create_crowdsale():
        create_crowdsale = crowdsale_factory_contract.functions.deployNonSoftCappableCrowdsale(
            [CBlock.preset.CELO, crowdsale_random_user],  # token to pay to deploy token and owner address
            CBlock.preset.TOKEN_TO_SALE,  # token to sale
            int('18'),  # token decimals
            int('86400'),  # duration
            [CBlock.preset.CELO],  # token to pay
            [int('1000000000000000000')],  # token rate
            [0, 0]  # limits
        )
        tx_hash = sign_send_tx(web3, create_crowdsale, crowdsale_random_user, c_private_key)
        print('create crowdsale', 'https://alfajores-blockscout.celo-testnet.org/tx/' + tx_hash.hex())
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash.hex())
        if tx_receipt.get('status'):
            with open('error_log.txt', 'a') as error_file:
                error_file.write(f'"A" Crowdsale transaction status is success {datetime.datetime.now()}\r\n')
    try:
        create_crowdsale()
    except:
        with open('error_log.txt', 'a') as error_file:
            error_file.write(f'"B" Crowdsale creation failed at {datetime.datetime.now()}\r\n')
        create_crowdsale()


for i in range(180):
    scanner_test()
    time.sleep(1)

#if __name__ == '__main__':
#    scanner_test()