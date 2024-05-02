import pprint

import pymongo
import pymongo as mongo_python

client = mongo_python.MongoClient("mongodb+srv://admpy:py220353@cluster0.xdket7h.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection

posts = db.posts

pprint.pprint(posts.count_documents({}))

pprint.pprint(posts.count_documents({"date":'2024-05-02 00:07:44.363066'}))

pprint.pprint(db.profiles.create_index([('author', pymongo.ASCENDING)], unique = True))

pprint.pprint(sorted(list(db.profiles.index_information())))

