import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK = False
    # REGISTERED_USERS = {
    #     'masonbercier@yahoo.com':{
    #     'name': 'mason',
    #     'password': 'password'
    #     }
    # }