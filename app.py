from flask import Flask, render_template
from web3 import Web3
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()  # take environment variables from .env.
ALCHEMY_API_URL = os.getenv("ALCHEMY_API_URL")
w3 = Web3(Web3.HTTPProvider(ALCHEMY_API_URL))  # Connect to your Ethereum node

# Replace these with your contract's address and ABI
contract_address = '0x37d9979D81cC68C2F0E286EC6fDD3E13e8399b3f'
# JSONファイルからABIを読み込む
with open('contract_abi.json', 'r') as f:
    contract_abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/')
def home():
    return 'Hello, Blockchain!'

@app.route('/balance/<address>')
def balance(address):
    # balanceOf を balances に変更します。
    balance = contract.functions.balances(address).call()
    return f'The balance of {address} is {balance}'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
