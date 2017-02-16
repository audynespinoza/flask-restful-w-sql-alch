from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

stores=[
	{
	'name':'wonderful_store',
	'items':[
		{
		'name':'toothbrush',
		'price':15.99
		},
		{
		'name':'paste',
		'price':3.99
		},
		]
	},
	{
	'name':'coo_store',
	'items':[
		{
		'name':'hairspray',
		'price':4.99
		},
		{
		'name':'legos',
		'price':64.99
		},
		]
	},
	{
	'name':'awesome_store',
	'items':[
		{
		'name':'babyoil',
		'price':4.99
		},
		{
		'name':'diapers',
		'price':34.99
		},
		]
	}
]

@app.route('/')
def home():
	#this calls the index.html which in turn sends a GET to the specified http path
	return render_template('index.html')
#Create the 5 endpoints

#POST /store data: {name:} - THIS CREATES A NEW STORE
@app.route('/store', methods=['POST'])
def create_store():
	request_data=request.get_json()
	new_store={
		'name': request_data['name'],
		'items':[]
	}
	stores.append(new_store)
	return jsonify(new_store)

#GET /store/<string:name> !!!WORKS!!!
@app.route('/store/<string:name>') # http://127.0.0.1:5000/store/some_name
def get_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message':'there was no store found under this name'})

#GET /store !!!WORKS!!!
@app.route('/store')
def get_stores():
	return jsonify({'stores':stores})


#POST /store/<string:name>/item {name:,price:} - CREATES ITEM
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data=request.get_json()
	for store in stores:
		if store['name']==name:
			new_item={
				'name':request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message':'store not found'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({"items":store['items']})
	return jsonify({'message':'item not found'})

app.run(port=5000)




'''NOTES: to test API, get "Postman" @ getpostman.com/apps'''



