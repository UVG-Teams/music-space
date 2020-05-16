from pymongo import MongoClient

client = MongoClient()
db = client.music_space

def print_collection(collection):
    print("/" * 75)
    for x in db[collection].find():
        print(x)
    print("/" * 75)

def save_sales_on_mongo(collection, data):
    print_collection(collection)
    print(data)
    # db[collection].insert_one({ data['date'] : data['sales'] })
    print_collection(collection)
