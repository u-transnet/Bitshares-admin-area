from flask import Flask, render_template
from config import Configuration

PRODUCTION_RPC_POINT = "wss://bitshares.openledger.info/ws"
TESTNET_RPC_POINT = "wss://node.testnet.bitshares.eu"

app = Flask(__name__, template_folder="templates")
app.config.from_object(Configuration)

@app.route('/')
def index():
    return render_template('not_found.html')