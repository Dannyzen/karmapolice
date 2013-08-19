MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'karma'
SERVER_NAME = 'localhost:5000'

RESOURCE_METHODS = ['GET','POST']

ITEM_METHODS = ['GET','PATCH']


Karma = {
    'schema': {
        'username': {
            'type' : 'string',
            'minlength': 1,
            'maxlength': 30,
            'required': True,
        },
        'points' :{
            'type': 'integer',
            'required': True,
            }
        },
    'additional_lookup' : {
        'url':'[\w]+','field':'name'
        },
    'item_title': 'username',
}

DOMAIN ={
    ng_items(resource, documents):
    ...  print 'About to return items from "%s" ' % resourcenkarma'e Karma
