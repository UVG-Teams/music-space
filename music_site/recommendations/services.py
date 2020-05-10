from pymongo import MongoClient
from datetime import datetime

from db_connections.services import get_sales_on

# client = MongoClient('localhost', 27017)
now = datetime.utcnow()
client = MongoClient()
db = client.music_space
# Clientes con todas las compras ocurridas en una fecha dada
compras_clientes = db.compras_clientes
# Analizar los tracks mas recientes registrados en la DB 
# y generar un listado con 10 clientes 
# y nuevos tracks que pueden ser de su interes
recommendations = db.recommendations

def print_collection(collection):
	for x in db[collection].find():
		print(x)

print_collection('compras_clientes')
print_collection('recommendations')

def sales_on(date):
    sales = get_sales_on(date)
    print(sales)
