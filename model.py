from pymongo import MongoClient
from flask import session

client= MongoClient()
db = client['amazon_valley']

def check_user(username):

	query ={'username':username}
	result =db['users'].find_one(query)
	return result

def add_user_to_db(user_info):
	
	db['users'].insert_one(user_info) 


def check_product(pname):

	query ={'pname':pname}
	result =db['product'].find_one(query)
	return result

def add_product_to_db(product_info):
	
	db['product'].insert_one(product_info) 

def get_products():

	if session['c_type'] == 'buyer':
		result= db['product'].find({})
		return result


	query={"sellername":session['username']}
	result=db['product'].find(query)
	return result


def remove_product(pname):

	query = {"pname":pname}
	db['product'].remove(query)

