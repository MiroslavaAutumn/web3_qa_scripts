import Lottery.preset
from Lottery.preset import web3_init


def get_factory_ref_code():
    web3 = web3_init()

    address = Lottery.preset.USER
    nonce = web3.eth.getTransactionCount(address)

    amount = 0.00888

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.FACTORY,
        'value': web3.toWei(amount, 'ether'),
        'gas': 1000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, Lottery.preset.USER_PRIV)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('FACTORY Ref code', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def get_lottery_ref_code():
    web3 = web3_init()

    address = Lottery.preset.USER
    nonce = web3.eth.getTransactionCount(address)

    amount = 0.00888

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.LOTTERY,
        'value': web3.toWei(amount, 'ether'),
        'gas': 1000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, Lottery.preset.USER_PRIV)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('LOTTERY Ref code', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    #get_factory_ref_code()
    #get_lottery_ref_code()
