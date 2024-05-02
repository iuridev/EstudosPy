# python -m pip install "pymongo[srv]"
# pip install requests
# py -c "import requests; print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version']
import pprint
from datetime import datetime

import pymongo as mongo_python

client = mongo_python.MongoClient("mongodb+srv://admpy:py220353@cluster0.xdket7h.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection

dt = datetime.now()

post = {
    "author": "Barreto",
    "text": 'My fist project with mongoDB',
    "tags": ['mongoDB', 'database'],
    "date": f'{dt}'
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.posts.find_one())
pprint.pprint(db.posts.find_one())

# find many in bd
for gets_all in posts.find():
    pprint.pprint(gets_all)
