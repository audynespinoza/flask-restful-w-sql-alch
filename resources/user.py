import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help="This field cannot be left blank"
	)
	parser.add_argument('password',
		type=str,
		required=True,
		help="This field cannot be left blank"
	)
	def post(self):
		post_data=UserRegister.parser.parse_args()

		if UserModel.find_by_username(post_data['username']):
			return {'message': "User '{}' has already been created".format(post_data['username'])}, 400
		
		user = UserModel(**post_data)
		try:
			user.save_to_db()
		except:
			return {'message': "An error occured while attempting to register user's information"},500
		return {'message': "Username '{}' has been registered".format(post_data['username'])}, 201




tcp.stream==1 || tcp.stream==2 || tcp.stream==3 || tcp.stream==4 || tcp.stream==5 || tcp.stream==6 || tcp.stream==7 || tcp.stream==8 