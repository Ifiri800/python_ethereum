from web3 import Web3
from web3.contract import parse_block_identifier_int
from web3.types import BlockData
from datetime import datetime
from time import timezone

# Link the project and connecting to Infura
eth_node = "https://mainnet.infura.io/v3/84d9e7fb419a4fd1b74b758bf07c22ba"

web3 = Web3(Web3.HTTPProvider(eth_node))
print(web3.isConnected())
print(web3.eth.blockNumber)


accounts = web3.eth.get_accounts()
test_address = "0xd757fd54b273BB1234d4d9993f27699d28d0EDD2"
balance = web3.eth.get_balance(test_address)
print("balance", web3.fromWei(balance, "ether"))

block = web3.eth.get_block('latest')
print(block)


block_data = web3.eth.get_transaction_by_block
print(block_data)

receipt = web3.eth.get_transaction_receipt
print(receipt)

transaction = web3.eth._get_transaction
print(transaction)

block_info = web3.eth.get_transaction_by_block
print(block_info)



