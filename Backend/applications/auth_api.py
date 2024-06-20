from applications.user_datastore import user_datastore
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_security import utils, auth_token_required


class Login(Resource):
    def post(self):
        recieved_data = request.get_json()

        email = recieved_data.get('email')
        password = recieved_data.get('password')

        if not email or not password:
            return make_response(jsonify({'message':'Email and Password are required'}),400)
        
        user = user_datastore.find_user(email=email)
        if not user:
            return make_response(jsonify({'message':'Invalid Credentials - User doesn\'t exists '}),401)
        
        if not utils.verify_password(password, user.password):
            return make_response(jsonify({'message':'Invalid Credentials - Invalid Password'}),401)

        utils.login_user(user)
        auth_token = user.get_auth_token()

        response = {
            'message':'Login Successful',
            'user':{
                'username':user.username,
                'email':user.email,
                'address' : user.address,
                'roles': [role.name for role in user.roles],
                'auth_token':auth_token
            }
        } 
        return make_response(jsonify(response),200) 
    