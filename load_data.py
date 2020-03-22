import django
import psycopg2
import os
import credentials

input('Please disconnect server in DBeaver and then press enter... ')
print("Django Version ", django.get_version())

host = credentials.DATABASE['HOST']
dbname = credentials.DATABASE['NAME']
user = credentials.DATABASE['USER']
password = credentials.DATABASE['PASSWORD']
port = credentials.DATABASE['PORT']

conn = psycopg2.connect(host=host, dbname='connect', user=user, password=password, port=port)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS {dbname}".format(dbname=dbname))
cursor.execute("CREATE DATABASE {dbname}".format(dbname=dbname))
print('Reset database completed!')
print('Loading data...')
# db = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
# db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = db.cursor()
# sqlfile = open('./music_site/database.sql', 'r', encoding='UTF-8')
# cursor.execute(sqlfile.read())
os.system("python ./music_site/load_migrations.py")
print("Data loaded successfully!")