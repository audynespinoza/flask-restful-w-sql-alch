from models.user import UserModel
from werkzeug.security import safe_str_cmp


#function used to authenticate a user
#given the right password, it's going to find the username and password
def authenticate(username, password):
	#if there is no username match, set to None.  This is the advantage the .get method gives us
	user = UserModel.find_by_username(username)
	#if user checks if user is not None
	if user and safe_str_cmp(user.password,password):
		return user

#this is unique to JWT
#the payload is the content of the JWT token
def identity(payload):
	user_id= payload['identity']
	return UserModel.find_by_id(user_id)
