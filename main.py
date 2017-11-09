from app import app
import whitelist
import block_num

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)