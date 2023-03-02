import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    REGISTERED_USERS = {
        'masonbercier@yahoo.com':{
        'name': 'mason',
        'password': 'password'
        }
    }