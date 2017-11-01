from flask import Flask, render_template, abort, request
from bitshares import BitShares
from bitshares.asset import Asset
from bitsharesapi.bitsharesnoderpc import BitSharesNodeRPC
import json

app = Flask(__name__, template_folder="../../templates")

@app.route('/')
def index():
    return render_template('not_found.html')

@app.route('/get_asset', methods=['POST'])
def get_asset():
    """ Получить данные по активу
        bool is_testnet: флаг testnet/production
        string ticker: тикер
    """
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    ticker = request.json.get('ticker')
    # logic
    if is_testnet:
        rpc_point = "wss://node.testnet.bitshares.eu"
    else:
        rpc_point = "wss://bitshares.openledger.info/ws"
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@app.route('/add_authorities', methods=['POST'])
def add_authorities():
    """ Добавить аккауты в черный/белый список
        bool is_testnet: флаг testnet/production
        string owner_wif: owner private key эмитента
        string ticker: тикер
        string list_type: тип списка white_list/black_list
        string array authorities: массив id/name аккаунтов для занесения в черный/белый список
    """
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # logic
    if is_testnet:
        rpc_point = "wss://node.testnet.bitshares.eu"
    else:
        rpc_point = "wss://bitshares.openledger.info/ws"
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

@app.route('/add_markets', methods=['POST'])
def add_markets():
    """ Добавить тикеры в черный/белый список
        bool is_testnet: флаг testnet/production
        string owner_wif: owner private key эмитента
        string asset_name: тикер
        string list_type: тип списка white_list/black_list
        string array authorities: массив id/name тикеров для занесения в черный/белый список
    """
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # logic
    if is_testnet:
        rpc_point = "wss://node.testnet.bitshares.eu"
    else:
        rpc_point = "wss://bitshares.openledger.info/ws"
    chain = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False,
        keys=owner_wif
    )
    asset = Asset(ticker, False, False, chain)
    asset.add_markets(list_type, authorities)
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@app.route('/remove_authorities', methods=['POST'])
def remove_authorities():
    """ Удалить аккауты из черного/белого списока
        bool is_testnet: флаг testnet/production
        string owner_wif: owner private key эмитента
        string ticker: тикер
        string list_type: тип списка white_list/black_list
        string array authorities: массив id/name аккаунтов для удаления из черного/белого списока
    """
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # logic
    if is_testnet:
        rpc_point = "wss://node.testnet.bitshares.eu"
    else:
        rpc_point = "wss://bitshares.openledger.info/ws"
    chain = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False,
        keys=owner_wif
    )
    asset = Asset(ticker, False, False, chain)
    asset.remove_authorities(list_type, authorities)
    return json.dumps(BitSharesNodeRPC(rpc_point).get_asset(ticker))

@app.route('/remove_markets', methods=['POST'])
def remove_markets():
    """ Удалить тикеры из черного/белого списока
        bool is_testnet: флаг testnet/production
        string owner_wif: owner private key эмитента
        string ticker: тикер
        string list_type: тип списка white_list/black_list
        string array authorities: массив id/name тикеров для удаления из черного/белого списока
    """
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('isTestnet')
    owner_wif = request.json.get('owner_wif')
    ticker = request.json.get('ticker')
    list_type = request.json.get('list_type')
    authorities = request.json.get('authorities')
    # logic
    if is_testnet:
        rpc_point = "wss://node.testnet.bitshares.eu"
    else:
        rpc_point = "wss://bitshares.openledger.info/ws"
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
    app.run(debug = True)