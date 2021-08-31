from re import L
from typing import List
from flask import Flask, make_response, Blueprint
from flask import request

from models.user import User
from models.utils.serializer import AlchemyEncoder
from config import db, URL_PREFIX

import os
import json


api_user = Blueprint('user-route', __name__, url_prefix=URL_PREFIX)



@api_user.route('/users', methods=['GET'])
def get_all_users():
    users: List[User] = db.session.query(User).all()
    ids = [user.id_ for user in users]
    return make_response({'users': json.dumps(dict(zip(ids, users)), cls=AlchemyEncoder)}, 200)



@api_user.route('/user', methods=['GET'])
def get_user():
    id_ = request.args.get('id')
    if not id_:
        return make_response({}, 200)
    user = db.session.query(User).filter(User.id_ == id_).first()
    return make_response(json.dumps({'user': user}, cls=AlchemyEncoder), 200)



@api_user.route('/user/new', methods=['GET'])
def create_new_random_user():
    user = User.create_random_user()
    return make_response(json.dumps({'user': user}, cls=AlchemyEncoder), 200)


@api_user.route('/user', methods=['DELETE'])
def soft_delete_user():
    id_ = request.args.get('id')
    if not id_:
        return make_response('DELETE', 404)

    user = db.session.query(User).filter(User.id_ == id_).first()
    user.inactive = False
    db.session.commit()
    return make_response('DELETE', 200)



