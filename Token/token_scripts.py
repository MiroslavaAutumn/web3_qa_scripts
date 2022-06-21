import Token.preset
from Token.preset import sign_send_tx, web3_init, get_contract_abi


def token_init():
    web3 = web3_init()
    token_abi = get_contract_abi(Token.preset.TOKEN_ADDRESS)
    token = web3.eth.contract(address=web3.toChecksumAddress(
        Token.preset.TOKEN_ADDRESS),
        abi=token_abi)
    return token, web3


def token_info():
    token, web3 = token_init()

    name = token.functions.name().call()
    symbol = token.functions.symbol().call()
    decimals = token.functions.decimals().call()
    total_supply = token.functions.totalSupply().call()

    print('name - ', name, '\nsymbol - ', symbol, '\ndecimals - ', decimals, '\ntotal supply - ', total_supply)

    user_address = Token.preset.USER
    balance_of = token.functions.balanceOf(
        user_address
    ).call()
    print('user balance - ', balance_of)

    allowance_owner_address = Token.preset.USER
    allowance_spender_address = Token.preset.OWNER  # usually a smart contract address

    allowance = token.functions.allowance(
        allowance_owner_address,
        allowance_spender_address
    ).call()
    print('allowance -', allowance)

def approve():
    token, web3 = token_init()

    amount = 1000 * 10 ** 18
    approve = token.functions.approve(
        Token.preset.TOKEN_ADDRESS,
        amount
    )
    tx_hash = sign_send_tx(web3, approve, Token.preset.USER,
                           Token.preset.USER_PRIV)
    print('Approve', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def burn():
    token, web3 = token_init()

    amount = 100 * 10 ** 18
    burn = token.functions.burn(
        amount
    )
    tx_hash = sign_send_tx(web3, burn, Token.preset.USER,
                           Token.preset.USER_PRIV)
    print('Burn', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def decreaseAllowance():
    token, web3 = token_init()

    subtracted_value = 100 * 10 ** 18
    decrease_allowance = token.functions.decreaseAllowance(
        Token.preset.USER,
        subtracted_value
    )
    tx_hash = sign_send_tx(web3, decrease_allowance, Token.preset.USER,
                           Token.preset.USER_PRIV)
    print('Decrease allowance', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def increaseAllowance():
    token, web3 = token_init()
    added_value = 100 * 10 ** 18
    increase_allowance = token.functions.increaseAllowance(
        Token.preset.USER,
        added_value
    )
    tx_hash = sign_send_tx(web3, increase_allowance, Token.preset.USER,
                           Token.preset.USER_PRIV)
    print('Increase allowance', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def mint():  # only owner
    token, web3 = token_init()
    amount = 100 * 10 ** 18
    mint = token.functions.mint(
        #Token.preset.USER,  # comment out this line if the method only accepts an amount
        amount
    )
    tx_hash = sign_send_tx(web3, mint, Token.preset.OWNER,
                           Token.preset.OWNER_PRIV)
    print('Mint', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def pause():  # only owner
    token, web3 = token_init()

    pause = token.functions.pause()
    tx_hash = sign_send_tx(web3, pause, Token.preset.OWNER,
                           Token.preset.OWNER_PRIV)
    print('Pause', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def renounceOwnership():  # only owner
    token, web3 = token_init()

    renounce_ownership = token.functions.renounceOwnership()
    tx_hash = sign_send_tx(web3, renounce_ownership, Token.preset.OWNER,
                           Token.preset.OWNER_PRIV)
    print('Renounce ownership', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def transfer():
    token, web3 = token_init()

    amount = 100 * 10 ** 18
    transfer = token.functions.transfer(
        Token.preset.USER_2,
        amount
    )
    tx_hash = sign_send_tx(web3, transfer, Token.preset.USER,
                           Token.preset.USER_PRIV)
    print('Transfer', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def transferFrom():  # Don't forget to make an approve from user2 to user1
    token, web3 = token_init()

    amount = 100 * 10 ** 18
    transfer_from = token.functions.transferFrom(
        Token.preset.USER_2,  # from
        Token.preset.USER,  # to
        amount
    )
    tx_hash = sign_send_tx(web3, transfer_from, Token.preset.USER,
                           Token.preset.USER_PRIV)
    print('Transfer from', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def transferOwnership():  # only owner
    token, web3 = token_init()

    new_owner_address = Token.preset.USER
    transfer_ownership = token.functions.transferOwnership(
        new_owner_address
    )
    tx_hash = sign_send_tx(web3, transfer_ownership, Token.preset.OWNER,
                           Token.preset.OWNER_PRIV)
    print('Transfer ownership', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


def unpause():  # only owner
    token, web3 = token_init()

    unpause = token.functions.unpause()
    tx_hash = sign_send_tx(web3, unpause, Token.preset.OWNER,
                           Token.preset.OWNER_PRIV)
    print('Unpause', 'https://testnet.bscscan.com/tx/' + tx_hash.hex())


if __name__ == '__main__':
    token_info()