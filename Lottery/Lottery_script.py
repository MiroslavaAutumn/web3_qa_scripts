import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi
import Lottery.secret


def create_lottery():
    web3 = web3_init()
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


def multiple_bid():
    users = {
        Lottery.secret.OWNER: {
            'priv': Lottery.secret.OWNER_PRIV,
            'daily_amount': 0.0011
        },
        Lottery.secret.USER: {
            'priv': Lottery.secret.USER_PRIV,
            'daily_amount': 0.0012
        },
        Lottery.secret.USER_2: {
            'priv': Lottery.secret.USER_2_PRIV,
            'daily_amount': 0.0013
        }
    }

    for user, values in users.items():
        create_bid_bnb(user, values.get('priv'), values.get('daily_amount'))


def create_bid_bnb(address=Lottery.secret.USER, priv=Lottery.secret.USER_PRIV, daily_amount=0.001):
    web3 = web3_init()

    nonce = web3.eth.getTransactionCount(address)

    # daily_amount = 0.001
    week_amount = 0.01
    month_amount = 0.1

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.LOTTERY,
        'value': web3.toWei(daily_amount, 'ether'),
        'gas': 3000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, priv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('Daily bid ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())
    web3.eth.wait_for_transaction_receipt(tx_hash.hex())


def get_balance():
    web3 = web3_init()
    address = '0xAa200F0266bC546B1B660326390528e2219F439a'
    balance = web3.eth.get_balance(address)
    result = web3.fromWei(balance, 'ether')
    print(result)


if __name__ == '__main__':
    # create_lottery()
    create_bid_bnb()
    # get_balance()
    # multiple_bid()
