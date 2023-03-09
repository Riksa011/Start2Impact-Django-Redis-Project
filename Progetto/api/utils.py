from web3 import Web3


# function to write an ethereum goerli transaction with provided message as input
def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/3c5cff57c7b54c488d4cb47ddc140c5f'))
    address = '0xBDd1Ef0041d2110Dd3F08b22A9ed5A895A474783'
    privateKey = '0x9844b8f22fd4a001c0eb10a2f0c05996b511eaeafff989e3cb5c754f504bcb1b'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
