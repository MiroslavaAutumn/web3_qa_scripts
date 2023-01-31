import time
import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi
import Lottery.secret


def create_bid_bnb(address=Lottery.secret.USER_1, priv=Lottery.secret.USER_1_PRIV, amount=1000000000000000):
    web3 = web3_init()

    nonce = web3.eth.getTransactionCount(address)

    # daily_amount = 1000000000000000
    # week_amount  = 10000000000000000
    # month_amount = 100000000000000000

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
    print(' Bid ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
    web3.eth.wait_for_transaction_receipt(tx_hash.hex())


def create_bid_LTON(address=Lottery.secret.USER_1, priv=Lottery.secret.USER_1_PRIV, amount=None):
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
        Lottery.preset.LOTTERY,
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


def multiple_bid_BNB():
    basic_bid = 1000000000000000
    d = 1
    w = 10
    m = 100
    multiplier = d  # set the required multiplier
    for i in range(1):  # cycle count
        users = {
            Lottery.secret.USER_1: {
                'priv': Lottery.secret.USER_1_PRIV,
                'amount': basic_bid * multiplier + 100000000000000
            },
            Lottery.secret.USER_2: {
                'priv': Lottery.secret.USER_2_PRIV,
                'amount': basic_bid * multiplier + 200000000000000
            },
            Lottery.secret.USER_3: {
                'priv': Lottery.secret.USER_3_PRIV,
                'amount': basic_bid * multiplier + 300000000000000
            },
            Lottery.secret.USER_4: {
                'priv': Lottery.secret.USER_4_PRIV,
                'amount': basic_bid * multiplier + 400000000000000
            },
            Lottery.secret.USER_5: {
                'priv': Lottery.secret.USER_5_PRIV,
                'amount': basic_bid * multiplier + 500000000000000
            },
            Lottery.secret.USER_6: {
                'priv': Lottery.secret.USER_6_PRIV,
                'amount': basic_bid * multiplier + 600000000000000
            },
            Lottery.secret.USER_7: {
                'priv': Lottery.secret.USER_7_PRIV,
                'amount': basic_bid * multiplier + 700000000000000
            },
            Lottery.secret.USER_8: {
                'priv': Lottery.secret.USER_8_PRIV,
                'amount': basic_bid * multiplier + 800000000000000
            },
            Lottery.secret.USER_9: {
                'priv': Lottery.secret.USER_9_PRIV,
                'amount': basic_bid * multiplier + 900000000000000
            }
        }

        for user, values in users.items():
            create_bid_bnb(user, values.get('priv'), values.get('amount'))

        ### Use time.sleep if you want to make transactions faster.
        ### To do this, comment out "web3.eth.wait_for_transaction_receipt" in the bid creation function
        ### DO NOT CHANGE THE DURATION OF TIME SLEEP BELOW 8

        #time.sleep(8)


def multiple_bid_LTON():
    basic_bid = 100*10**14
    w = 1
    m = 10
    multiplier = w  # set the required multiplier
    for i in range(1):  # cycle count
        users = {
            Lottery.secret.USER_1: {
                'priv': Lottery.secret.USER_1_PRIV,
                'amount': basic_bid * multiplier + 10**13
            },
            Lottery.secret.USER_2: {
                'priv': Lottery.secret.USER_2_PRIV,
                'amount': basic_bid * multiplier + 2*10**13
            },
            Lottery.secret.USER_3: {
                'priv': Lottery.secret.USER_3_PRIV,
                'amount': basic_bid * multiplier + 3*10**13
            },
            Lottery.secret.USER_4: {
                'priv': Lottery.secret.USER_4_PRIV,
                'amount': basic_bid * multiplier + 4*10**13
            },
            Lottery.secret.USER_5: {
                'priv': Lottery.secret.USER_5_PRIV,
                'amount': basic_bid * multiplier + 5*10**13
            },
            Lottery.secret.USER_6: {
                'priv': Lottery.secret.USER_6_PRIV,
                'amount': basic_bid * multiplier + 6*10**13
            },
            Lottery.secret.USER_7: {
                'priv': Lottery.secret.USER_7_PRIV,
                'amount': basic_bid * multiplier + 7*10**13
            },
            Lottery.secret.USER_8: {
                'priv': Lottery.secret.USER_8_PRIV,
                'amount': basic_bid * multiplier + 8*10**13
            },
            Lottery.secret.USER_9: {
                'priv': Lottery.secret.USER_9_PRIV,
                'amount': basic_bid * multiplier + 9*10**13
            }
        }

        for user, values in users.items():
            create_bid_LTON(user, values.get('priv'), values.get('amount'))


if __name__ == '__main__':
    # create_bid_bnb()
    # create_bid_LTON()
    # multiple_bid_BNB()
    multiple_bid_LTON()
