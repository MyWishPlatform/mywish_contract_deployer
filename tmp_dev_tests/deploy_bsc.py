import os
from pathlib import Path
import dotenv
from mywish import BrownieDeployer

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

with open('./token.sol', 'r') as token:
    contract_code = token.read()

brownie_deployer = BrownieDeployer()
bsc_contract = brownie_deployer.deploy(
    contract_code,
    account_name='test_key',
    account_pass='test_password',
    private_key=os.environ['PRIVATE_KEY'],
    network='bsc-test',
    contract_name='MainToken',
    dev_api_token=os.environ['DEV_API_TOKEN_BSC'],
)

with open('./swap_bridge.sol', 'r') as token:
    contract_code = token.read()

print(bsc_contract)

swap_contract = brownie_deployer.deploy(
    contract_code,
    account_name='test_key',
    account_pass='test_password',
    private_key=os.environ['PRIVATE_KEY'],
    network='bsc-test',
    contract_name='SwapContract',
    dev_api_token=os.environ['DEV_API_TOKEN_BSC'],
    constructor_params=[
        f'\'{bsc_contract}\'',
        '\'0x986c3298d8a302fd854c8e40e1973fb78c7eba56\'',
        '3',
        '[1, 2]',
        '2',
        '0',
        '10000000000',
        '130000000000',
        '5'
    ]
)