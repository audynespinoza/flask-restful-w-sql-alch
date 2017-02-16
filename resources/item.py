from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,
		help="This field cannot be left blank, and has to have a float!"
	)
	parser.add_argument('store_id',
		type=float,
		required=True,
		help="Every item needs a store id."
	)
	@jwt_required()
	#the 'name' argument is directly tied to the '<string:name>' in the api.add_resource
	#it's the name that is included in the url string
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {'message': 'item not found'}, 404

	@jwt_required()
	def post(self, name):
		if ItemModel.find_by_name(name):
			return {'message':"item '{}' already exists".format(name)},400
		post_data=Item.parser.parse_args()

		item = ItemModel(name,**post_data)

		try:
			item.save_to_db()
		except:
			return {'message':'An error occured while inserting item'},500
		
		return item.json(), 201

	@jwt_required()
	def delete(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()

		return {'message':'Item deleted'}

	@jwt_required()
	def put(self, name):
		post_data=Item.parser.parse_args()
		item = ItemModel.find_by_name(name)

		if item is None:
			item = ItemModel(name, **post_data)
		else:
			item.price = post_data['price']
			item.store_id = post_data['store_id']

		item.save_to_db()

		return item.json(), 200


#gets lists of items
class ItemList(Resource):
	@jwt_required()
	def get(self):
		return {'items': [item.json() for item in ItemModel.query.all()]}

