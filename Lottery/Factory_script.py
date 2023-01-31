import Lottery.preset
from Lottery.preset import sign_send_tx, web3_init, get_contract_abi
import Lottery.secret


def create_lottery():
    web3 = web3_init()

    factory_abi = get_contract_abi(Lottery.preset.FACTORY)
    factory_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.FACTORY_PROXY),
        abi=factory_abi)

    #  lottery params
    A = '1'  # amount of numbers
    B = '1'  # reward for the first 10 addresses
    R = '200000'  # ref code
    amount = int(A + B + R) * 10 ** 10
    print(amount)

    #  creator
    address = Lottery.secret.USER_1
    nonce = web3.eth.getTransactionCount(address)

    # build transaction
    tx = {
        'nonce': nonce,
        'to': Lottery.preset.FACTORY_PROXY,
        'value': web3.toWei(amount, 'wei'),
        'gas': 3000000,
        'gasPrice': web3.toWei('10', 'gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx, Lottery.secret.USER_1_PRIV)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('Create lottery', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())

    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    event_deployed = factory_contract.events.DeployedLottery().processReceipt(receipt)
    print('Lottery address', event_deployed[0].get('args').get('lottery'))


def calc_lotteries():
    web3 = web3_init()

    factory_abi = get_contract_abi(Lottery.preset.FACTORY)
    factory_contract = web3.eth.contract(address=web3.toChecksumAddress(
        Lottery.preset.FACTORY_PROXY),
        abi=factory_abi)

    calc_lottery = factory_contract.functions.calcLotteries(
        [Lottery.preset.LOTTERY]
    )
    tx_hash = sign_send_tx(web3, calc_lottery, Lottery.secret.USER_1,
                           Lottery.secret.USER_1_PRIV)
    print('previous day calculation', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    #create_lottery()
    calc_lotteries()
