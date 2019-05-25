from flask import Flask, jsonify , request, render_template

app =  Flask(__name__)

stores=[
    {



        'name':'jilbab',
        'items': [
            {
                'name':'pashmina',
                'persentease':'18%',
                'img':'url',
                'price':'Rp 10.000'
            }
        ]
    }
]
@app.route('/')
def index():
    return ('Succes')

@app.route('/store',methods=['POST'])
def create_store():
    requst_data = request.get_json()
    new_store = {
        'name': requst_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)




@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message': 'Store Not Found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores: ' : stores})


@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data= request.get_json()
    for store in stores:
        if store['name']== name:
            new_item={
                'name': request_data['name'],
                'price': request_data['price'],
                'persentase': request_data['persentase'],
                'img': request_data['img'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'Store not found'})



app.run()
