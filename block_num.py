from bitshares.blockchain import Blockchain
from bitshares import BitShares
from application import app, TESTNET_RPC_POINT, PRODUCTION_RPC_POINT
from flask import request, abort
import json

@app.route('/get_current_block_num', methods=['POST'])
def get_current_block():
    """ Получить номер текущего блока в цепи
        bool is_testnet: флаг testnet/production
    """
    if not request.json:
        abort(400)
    # params
    is_testnet = request.json.get('is_testnet')
    # check params
    if any(v is None for v in [is_testnet]):
        abort(500, "Enter all required parameters")
    # logic
    if is_testnet:
        rpc_point = TESTNET_RPC_POINT
    else:
        rpc_point = PRODUCTION_RPC_POINT
    bitshares = BitShares(
        rpc_point,
        nobroadcast=False,
        bundle=False
    )
    chain = Blockchain(bitshares)
    current_block_num = chain.get_current_block_num()
    return json.dumps({"current_block_num": current_block_num})