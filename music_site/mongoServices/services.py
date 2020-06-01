from pymongo import MongoClient

client = MongoClient()
db = client.music_space

def print_collection(collection):
    print("/" * 75)
    for x in db[collection].find():
        print(x)
    print("/" * 75)

def save_sales_on_mongo(collection, data):
    for i in range(len(data['sales'])):
        data['sales'][i]['total'] = float(data['sales'][i]['total']) 
    # db[collection].insert_one({ 'sales': data['sales'] })
    if data['sales'] != []:
        db[collection].insert_many( data['sales'] )
