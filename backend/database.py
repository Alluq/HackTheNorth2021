from pymongo import MongoClient
from bson.objectid import ObjectId

class repo:
    def __init__(self, collection):
        url = "mongodb+srv://simon:simon@hackthenorth2021.kat9o.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE"
        self.db = MongoClient(url, connect=False)['hack'][collection]

    def read(self, id):
        resp = self.db.find_one({"_id": ObjectId(id)})
        return resp