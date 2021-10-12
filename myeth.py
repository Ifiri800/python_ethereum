from web3 import Web3

# Link the project and connecting to Infura
eth_node = ""

web3 = Web3(Web3.HTTPProvider(eth_node))
print(web3.isConnected())

def get_block():
    block = web3.eth.get_block('latest')
    return print(block)

def get_block_number():
    block_number = web3.eth.get_block_number()
    print(block_number)

get_block = web3.eth.get_block_number
if block_number != 0:
    block_info = web3.eth_get_block_number(block).get('hash').hex()
    print(block_info)



