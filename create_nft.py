from algosdk.future.transaction import AssetCreateTxn
from algosdk import mnemonic
from algosdk.v2client import algod
from secrets import phrase, algod_token

# Connects to mainnet
# One can obtain a free API key from PureStake at https://developer.purestake.io/signup
def algod_client():
    algod_address = "https://mainnet-algorand.api.purestake.io/ps2"
    headers = {
       "X-API-Key": algod_token,
    }
    return algod.AlgodClient(algod_token, algod_address, headers)
    


key, address = mnemonic.to_private_key(phrase), mnemonic.to_public_key(phrase)

client = algod_client()

params = client.suggested_params()
params.fee = 1000
params.flat_fee = True

print(address)
