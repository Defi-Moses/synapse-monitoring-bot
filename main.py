import json
import requests
from web3 import Web3
from config import chains

def make_rpc_request(url, method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"RPC request failed with status code: {response.status_code}")

def checkGasBalances():
    #Infra so that we can notify when gas is low 
    gas_low = []
    gas_extremely_low = []
    results = []
    output = ""
    # Iterate over each chain
    for chain in chains:
        rpc_url = chains[chain]['url']
        contract_address = chains[chain]['bridge']

        try:
            response = make_rpc_request(rpc_url, "eth_getBalance", [contract_address, "latest"])
            gas_amount = round(int(response["result"], 16)/(10**18),2)
            gas_info = f"Gas amount for {chain} chain: {gas_amount}\n"
            output += gas_info  # Append the gas info to the output string

            #old logic (for debugging)
            # print(f"Gas amount for {chain} chain: {gas_amount}")
            # results.append({
            #     'chain': chain,
            #     'gas_amount': gas_amount
            # })
        except Exception as e:
            error_info = f"Error occurred for {chain} chain: {e}\n"
            output += error_info  # Append the error info to the output string

            #old logic (for debugging)
            # print(f"Error occurred for {chain} chain: {e}")

    # print(output)
    return output
    

def checkMiniChefBalances():
    #Infra so that we can notify when miniChef balances are low 
    miniChef_low = []
    miniChef_extremely_low = []
    results = []
    output = ""
    # Iterate over each chain
    for chain in chains:
        rpc_url = chains[chain]['url']
        contract_address = chains[chain]['minichef']
        syn_address = chains[chain]['syn']

        try:
            data ='0x70a08231' + contract_address[2:].zfill(64)
            response = make_rpc_request(rpc_url, "eth_call", [{"to": syn_address, "data":data}, "latest"])
            miniChef_amount = round(int(response["result"],16)/(10**18),2)
            miniChef_info = f"SYN balance for {chain} chain: {miniChef_amount} \n"
            output += miniChef_info  # Append the miniChef info to the output string

            #old logic (for debugging)
            # print(f"Gas amount for {chain} chain: {gas_amount}")
            # results.append({
            #     'chain': chain,
            #     'gas_amount': gas_amount
            # })
        except Exception as e:
            error_info = f"Error occurred for {chain} chain: {e}\n"
            output += error_info  # Append the error info to the output string

            #old logic (for debugging)
            # print(f"Error occurred for {chain} chain: {e}")

    # print(output)
    return output



