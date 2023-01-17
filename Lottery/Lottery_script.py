import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi


def create_lottery():
    web3 = web3_init()
    #  lottery params
    A = '1'  # amount of numbers
    B = '1'  # reward for the first 10 addresses
    R = '123456'  # ref code
    amount = int(A + B + R) * 10 ** 10

    #  creator
    address = Lottery.preset.OWNER
    nonce = web3.eth.getTransactionCount(address)

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.FACTORY,
        'value': web3.toWei(amount, 'wei'),
        'gas': 3000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, Lottery.preset.OWNER_PRIV)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('Create lottery', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def create_bid_bnb():
    web3 = web3_init()

    address = Lottery.preset.USER
    nonce = web3.eth.getTransactionCount(address)

    daily_amount = 0.001
    week_amount = 0.01
    month_amount = 0.1

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.LOTTERY,
        'value': web3.toWei(daily_amount, 'ether'),
        'gas': 30000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, Lottery.preset.USER_PRIV)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('Daily bid ', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    # create_lottery()
    # create_bid_bnb()
