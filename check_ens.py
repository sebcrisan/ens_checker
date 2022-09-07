import os
from dotenv import load_dotenv
from web3 import Web3
from ens import ENS

from name_to_addr import name_to_addr
from get_balance import get_balance
from get_ens_names import get_ens_names
load_dotenv()

INFURA_API_KEY = os.getenv("INFURA_API_KEY")
INFURA_URL = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
PROVIDER = Web3.HTTPProvider(INFURA_URL)
WEB3 = Web3(PROVIDER)
NS = ENS(PROVIDER)

def main():
    # object with all ens name data
    data = []
    # ens names list from i.e. txt file
    ens_names = get_ens_names()
    # check if we can connect
    if(WEB3.isConnected()):
        print("connected")
        # loop through all ens names in the list 
        for name in ens_names:
            # get eth address
            eth_address = name_to_addr(NS, name)
            # get balance in eth
            balance = WEB3.fromWei(get_balance(WEB3, eth_address), "ether")
            # create data object and add it to the data list
            data.append({
                "name": name,
                "address": eth_address,
                "balance": balance
            })
    print(data)
    
if __name__ == '__main__':
     main()

