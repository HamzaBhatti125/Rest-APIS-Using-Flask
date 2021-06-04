from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'Flowers store',
        'items': [
            {
                'name': 'Roses',
                'price': 100
            }, 
            {
                'name': 'Lillies',
                'price': 200
            }
        ]
    },
    {
        'name': 'Book store',
        'items': [
            {
                'name': 'History Books',
                'price': 100
            },
            {
                'name': 'Geography Books',
                'price': 500
            },
        ]
    }
]


@app.route('/')
def home():
    return "Restful APIS using Flask"

#Get All Stores
@app.route('/stores')
def get_all_store_name():
    return jsonify({'stores': stores})

#Create Store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#Get Single Store
@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'store not found'}), 404

#Add items to Store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

#Show items of Specific Store
@app.route('/store/<string:name>/items')
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run(debug=True)