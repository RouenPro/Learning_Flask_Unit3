from flask import Flask, jsonify, request

app = Flask(__name__)

# Create Store
stores = [
    {
        'name': 'my wonderful store',
        'items': [
            {
            'name': 'my item',
            'price': 15.9
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass

@app.route('/store')
def create_iteam_in_store():
    return jsonify(stores)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item', methods=['GET'])
def get_iteam_in_store(name):
    pass

app.run(port=5000)