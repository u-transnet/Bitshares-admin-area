from flask import Flask, render_template, abort, request
from bitshares import BitShares
from bitshares.asset import Asset
from bitsharesapi.bitsharesnoderpc import BitSharesNodeRPC
import json

PRODUCTION_RPC_POINT = "wss://bitshares.openledger.info/ws"
TESTNET_RPC_POINT = "wss://node.testnet.bitshares.eu"

application = Flask(__name__, template_folder="templates")

@application.route('/')
def index():
    return render_template('not_found.html')

@application.route('/get_asset', methods=['POST'])
def get_asset():
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('is_testnet')
    ticker = request.json.get('ticker')
    # check params
    if any(v is None for v in [is_testnet, ticker]):
        abort(500, "Enter all required parameters")
    # logic
    if is_testnet:
        rpc_point = TESTNET_RPC_POINT
    else:
        rpc_point = PRODUCTION_RPC_POINT
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@application.route('/add_authorities', methods=['POST'])
def add_authorities():
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # check params
    if any(v is None for v in [is_testnet, owner_wif, ticker, list_type, authorities]):
        abort(500, "Enter all required parameters")
    # logic
    if is_testnet:
        rpc_point = TESTNET_RPC_POINT
    else:
        rpc_point = PRODUCTION_RPC_POINT
    chain = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False,
        keys=owner_wif
    )
    asset = Asset(ticker, False, False, chain)
    asset.setoptions({"white_list": True})
    asset.add_authorities(list_type, authorities)
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@application.route('/add_markets', methods=['POST'])
def add_markets():
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # check params
    if any(v is None for v in [is_testnet, owner_wif, ticker, list_type, authorities]):
        abort(500, "Enter all required parameters")
    # logic
    if is_testnet:
        rpc_point = TESTNET_RPC_POINT
    else:
        rpc_point = PRODUCTION_RPC_POINT
    chain = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False,
        keys=owner_wif
    )
    asset = Asset(ticker, False, False, chain)
    asset.add_markets(list_type, authorities)
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@application.route('/remove_authorities', methods=['POST'])
def remove_authorities():
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # check params
    if any(v is None for v in [is_testnet, owner_wif, ticker, list_type, authorities]):
        abort(500, "Enter all required parameters")
    # logic
    if is_testnet:
        rpc_point = TESTNET_RPC_POINT
    else:
        rpc_point = PRODUCTION_RPC_POINT
    chain = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False,
        keys=owner_wif
    )
    asset = Asset(ticker, False, False, chain)
    asset.remove_authorities(list_type, authorities)
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@application.route('/remove_markets', methods=['POST'])
def remove_markets():
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # check params
    if any(v is None for v in [is_testnet, owner_wif, ticker, list_type, authorities]):
        abort(500, "Enter all required parameters")
    # logic
    if is_testnet:
        rpc_point = TESTNET_RPC_POINT
    else:
        rpc_point = PRODUCTION_RPC_POINT
    chain = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False,
        keys=owner_wif
    )
    asset = Asset(ticker, False, False, chain)
    asset.remove_markets(list_type, authorities)
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

if __name__ == '__main__':
    application.run(debug=True, host='127.0.0.1')