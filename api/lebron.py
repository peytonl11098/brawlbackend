import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.lebrons import LebronStatsPredict

lebron_api = Blueprint('lebron_api', __name__,
                   url_prefix='/api/lebrons')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(lebron_api)

class LebronAPI:        
    class _CRUD(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def post(self): # Create method
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate Abbreviation
            opp = body.get('Abbreviation')
            if opp is None or len(opp) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 400
            uo = LebronStatsPredict(opp=opp)
            
    # building RESTapi endpoint
    api.add_resource(_CRUD, '/')