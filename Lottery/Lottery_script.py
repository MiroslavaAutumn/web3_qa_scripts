import time

import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi
import Lottery.secret


def create_lottery():
    web3 = web3_init()

    factory_abi = get_contract_abi(Lottery.preset.FACTORY)
    factory_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.FACTORY),
        abi=factory_abi)

    #  lottery params
    A = '1'  # amount of numbers
    B = '1'  # reward for the first 10 addresses
    R = '000000'  # ref code
    amount = int(A + B + R) * 10 ** 10
    print(amount)

    #  creator
    address = Lottery.secret.OWNER
    nonce = web3.eth.getTransactionCount(address)

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.FACTORY,
        'value': web3.toWei(amount, 'wei'),
        'gas': 3000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, Lottery.secret.OWNER_PRIV)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('Create lottery', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    event_deployed = factory_contract.events.DeployedLottery().processReceipt(receipt)
    print('Lottery address', event_deployed[0].get('args').get('lottery'))


def multiple_bid():
    basic_bid = 1000000000000000
    d = 1
    w = 10
    m = 100
    multiplier = d  # set the required multiplier

    users = {
        Lottery.secret.OWNER: {
            'priv': Lottery.secret.OWNER_PRIV,
            'amount': (basic_bid + 100000000000000) * multiplier
        },
        Lottery.secret.USER: {
            'priv': Lottery.secret.USER_PRIV,
            'amount': (basic_bid + 200000000000000) * multiplier
        },
        Lottery.secret.USER_2: {
            'priv': Lottery.secret.USER_2_PRIV,
            'amount': (basic_bid + 300000000000000) * multiplier
        },
        Lottery.secret.USER_3: {
            'priv': Lottery.secret.USER_3_PRIV,
            'amount': (basic_bid + 400000000000000) * multiplier
        },
        Lottery.secret.USER_4: {
            'priv': Lottery.secret.USER_4_PRIV,
            'amount': (basic_bid + 500000000000000) * multiplier
        },
        Lottery.secret.USER_5: {
            'priv': Lottery.secret.USER_5_PRIV,
            'amount': (basic_bid + 600000000000000) * multiplier
        },
        Lottery.secret.USER_6: {
            'priv': Lottery.secret.USER_6_PRIV,
            'amount': (basic_bid + 700000000000000) * multiplier
        },
        Lottery.secret.USER_7: {
            'priv': Lottery.secret.USER_7_PRIV,
            'amount': (basic_bid + 800000000000000) * multiplier
        },
        Lottery.secret.USER_8: {
            'priv': Lottery.secret.USER_8_PRIV,
            'amount': (basic_bid + 900000000000000) * multiplier
        }
    }

    for user, values in users.items():
        # create_bid_bnb(user, values.get('priv'), values.get('amount'))
        create_bid_LTON(user, values.get('priv'), values.get('amount'))


def create_bid_bnb(address=Lottery.secret.USER, priv=Lottery.secret.USER_PRIV, amount=1000000000000000):
    web3 = web3_init()

    nonce = web3.eth.getTransactionCount(address)

    # daily_amount = 0.001
    week_amount = 10000000000000000
    month_amount = 100000000000000000

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.LOTTERY,
        'value': web3.toWei(amount, 'wei'),
        'gas': 3000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, priv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('Daily bid ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
    web3.eth.wait_for_transaction_receipt(tx_hash.hex())


def create_bid_LTON(address=Lottery.secret.USER, priv=Lottery.secret.USER_PRIV, amount=None):
    web3 = web3_init()
    token_abi = get_contract_abi(Lottery.preset.TOKEN)
    token = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.TOKEN),
        abi=token_abi)

    if amount is None:
        w = 100
        m = 1000
        amount = w  # set the required lottery type
    print(amount)

    approve = token.functions.approve(
        Lottery.preset.TOKEN,
        amount
    )

    tx_hash = sign_send_tx(web3, approve, address, priv)

    print('Approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
    web3.eth.wait_for_transaction_receipt(tx_hash.hex())

    transfer = token.functions.transfer(
        Lottery.preset.LOTTERY,
        amount
    )
    tx_hash = sign_send_tx(web3, transfer, address, priv)
    print('Transfer', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def calc_lotteries():
    web3 = web3_init()

    factory_abi = get_contract_abi(Lottery.preset.FACTORY)
    factory_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.FACTORY),
        abi=factory_abi)

    calc_lottery = factory_contract.functions.calcLotteries(
        [Lottery.preset.LOTTERY]
    )
    tx_hash = sign_send_tx(web3, calc_lottery, Lottery.secret.OWNER,
                           Lottery.secret.OWNER_PRIV)
    print('previous day calculation', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def get_balance():
    web3 = web3_init()
    address = '0xAa200F0266bC546B1B660326390528e2219F439a'
    balance = web3.eth.get_balance(address)
    result = web3.fromWei(balance, 'ether')
    print(result)


if __name__ == '__main__':
    create_lottery()
    # create_bid_bnb()
    # multiple_bid()
    # create_bid_LTON()
    # calc_lotteries()
    # get_balance()
