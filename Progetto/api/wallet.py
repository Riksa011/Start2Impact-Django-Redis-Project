from web3 import Web3

# create ethereum goerli testnet wallet
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/3c5cff57c7b54c488d4cb47ddc140c5f'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address
print(f'Your address: {address}\nYour key: {privateKey}')
