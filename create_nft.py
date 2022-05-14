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

# Helper function that waits for a given txid to be confirmed by the network
def wait_for_confirmation(client, txid):
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation...")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    return txinfo

key, address = mnemonic.to_private_key(phrase), mnemonic.to_public_key(phrase)
def create_token(name, key, address):
    client = algod_client()

    params = client.suggested_params()
    params.fee = 1000
    params.flat_fee = True

    txn = AssetCreateTxn(address, params, 1, 0, False, manager=address, reserve=address, freeze=address, 
    clawback=address, unit_name="davidmikes", asset_name=name, url="https://storage.googleapis.com/davidmike-nft/" + name + '.json#arc3')

    stxn = txn.sign(key)

    # Send the Txn
    txid = client.send_transaction(stxn)
    return txid

print(create_token("nft1", key, address))
