import Lottery.preset
from Lottery.preset import web3_init
import Lottery.secret


def get_factory_ref_code(address=Lottery.secret.USER_1, priv=Lottery.secret.USER_1_PRIV, amount=0.00888):
    web3 = web3_init()

    nonce = web3.eth.getTransactionCount(address)

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.FACTORY_PROXY,
        'value': web3.toWei(amount, 'ether'),
        'gas': 1000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, priv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('FACTORY Ref code', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def get_lottery_ref_code(address=Lottery.secret.USER_1, priv=Lottery.secret.USER_1_PRIV, amount=0.00888):
    web3 = web3_init()
    nonce = web3.eth.getTransactionCount(address)

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.LOTTERY,
        'value': web3.toWei(amount, 'ether'),
        'gas': 1000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, priv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('LOTTERY Ref code', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def multiple_get_ref_code():
    amount = 0.00888

    users = {
        Lottery.secret.USER_1: {
            'priv': Lottery.secret.USER_1_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_2: {
            'priv': Lottery.secret.USER_2_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_3: {
            'priv': Lottery.secret.USER_3_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_4: {
            'priv': Lottery.secret.USER_4_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_5: {
            'priv': Lottery.secret.USER_5_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_6: {
            'priv': Lottery.secret.USER_6_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_7: {
            'priv': Lottery.secret.USER_7_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_8: {
            'priv': Lottery.secret.USER_8_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_9: {
            'priv': Lottery.secret.USER_9_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_10: {
            'priv': Lottery.secret.USER_10_PRIV,
            'amount': amount
        },
        Lottery.secret.USER_11: {
            'priv': Lottery.secret.USER_11_PRIV,
            'amount': amount
        }
    }

    for user, values in users.items():
        #get_lottery_ref_code(user, values.get('priv'), values.get('amount'))
        get_factory_ref_code(user, values.get('priv'), values.get('amount'))


if __name__ == '__main__':
    #get_factory_ref_code()
    #get_lottery_ref_code()
    multiple_get_ref_code()
