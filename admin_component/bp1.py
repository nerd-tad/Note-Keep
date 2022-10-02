from flask import Blueprint, render_template, Response, request
import pymongo
from bson.objectid import ObjectId  #this lets us covert strings to objectids, mongo uses object ids so it goes well with mongo
import json

bp_1 = Blueprint('bp1', __name__, static_folder='static', template_folder='templates')

'''try:
	mongo = pymongo.MongoClient(
		host='localhost',
		port=27017,
		serverSelectionTimeoutMS = 1000
	)
	db = mongo.tad_db1
	mongo.server_info()  #this is the line that triggers exception.
except:
	print('Cannot connect to db!!')'''
try:
	mongo = pymongo.MongoClient(
		host='mongodb+srv://<mongo_cloud_username>:<mongo_cloud_password>your_domain_.mongodb.net/?retryWrites=true&w=majority',
		serverSelectionTimeoutMS = 1000
	)
	db = mongo.test_db1.test_collection1
	mongo.server_info()  #this is the line that triggers exception.
except:
	print('Cannot connect to db!!')
print(db)



@bp_1.route('/')
@bp_1.route('/home')
def home():
	return render_template('Home.html')

@bp_1.route('/test')
def test():
	return '<h1>This is test inside blueprint.</h1>'

@bp_1.route('/create_user', methods=['POST', 'GET'])
def create_user():
	try:
		#user = {'name':'rim', 'alter_ego':'lazy_nerd'}
		user = {'name':request.form['name'], 'alter_ego':request.form['alter_ego']}  #request.form data will be came using postman or html form
		#wow, we saw how we can submit form data in html with flask, without creating a form, we can do the same with postman... see above line
		#we created form-data in postman and gave names to form fields(name, alter_ego) and values to it.
		dbResponse = db.users.insert_one(user)
		print(dir(dbResponse))
		print('inserted successfully!!')
		print(dbResponse.inserted_id) #that inserted_id was found using dir(dbResponse)
		return Response(
			response=json.dumps({'msg':'user_created', 'id':f'{dbResponse.inserted_id}'}),
			status=200,
			mimetype = 'application/json'
		)
	except Exception as e:
		print(e)					#POINT TO NOTE -> THE ENTIRE DATABASE PATH WILL BE /test_db1.test_collection1.users (/<major_db>.<collection_name>.<minor_db_set>)  collection and minor_db_set will be auto created. Not to worry....


@bp_1.route('/get_users', methods=['POST', 'GET'])
def get_all_users():
	try:
		data = list(db.users.find()) #you have to convert the data comming from query ot a list
		for ele in data:
			ele["_id"] = str(ele["_id"])  #ele["_id"] is something cannot jsonified, to do it we have to convert id to a string
		return Response(
			response=json.dumps(data),
			status=200,
			mimetype = 'application/json'
		)
	except Exception as e:
		return Response(
			response=json.dumps({'msg':'failed retrieving!!'}),
			status=500,
			mimetype = 'application/json'
		)


@bp_1.route('/update/<m_id>', methods=['PATCH'])
def update(m_id):
	try:
		#search the user and update and do it in one line
		dbResponse = db.users.update_one(
			{'_id':ObjectId(m_id)}, #we are copying and adding id to the url route, it should be convereted to and object id or it wont work.
			{'$set':{"name":request.form['name']}}  #the thing inside $set is json, remember, or you get fucked
		)
		if dbResponse.modified_count == 1: #then only an update has occured
			return Response(
				response=json.dumps({'msg':'updated successfully!!!'}),
				status=200,
				mimetype = 'application/json'
			)
		return Response(
			response=json.dumps({'msg':'nothing to update, maybe you tried with the same value existed!!!'}),
			status=200,
			mimetype = 'application/json'
		)


	except Exception as e:
		print('*******************************')
		print(e)
		print('*******************************')
		return Response(
			response=json.dumps({'msg':'sorry!,cannot update!!!'}),
			status=500,
			mimetype = 'application/json'
		)

@bp_1.route('/delete/<m_id>', methods=['DELETE'])
def delete(m_id):
	try:
		#search the user and update and do it in one line
		dbResponse = db.users.delete_one({'_id':ObjectId(m_id)})
		if dbResponse.deleted_count == 1: #then only an update has occured
			return Response(
				response=json.dumps({'msg':'deleted successfully!!!'}),
				status=200,
				mimetype = 'application/json'
			)
		return Response(
			response=json.dumps({'msg':'nothing to delete, maybe you tried with a nonexisting id same as in mongo format!!!'}),
			status=200,
			mimetype = 'application/json'
		)


	except Exception as e:
		print('*******************************')
		print(e)
		print('*******************************')
		return Response(
			response=json.dumps({'msg':'sorry!,cannot delete!!!'}),
			status=500,
			mimetype = 'application/json'
		)
