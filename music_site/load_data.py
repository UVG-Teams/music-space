import django
import psycopg2
import os
import credentials

print("\n"*100)
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

print('Loading data structure...')
# db = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
# db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = db.cursor()
# sqlfile = open('./music_site/database.sql', 'r', encoding='UTF-8')
# cursor.execute(sqlfile.read())
print("~ " * 75)
os.system("python manage.py makemigrations")
print("~ " * 75)
os.system("python manage.py migrate")
print("~ " * 75)
# dbDump = input("Enter the name of the dump file with extension: \n\t- ")
dbDump = "databaseInitDump.sql"
try:
  file = open(dbDump, "r")
  print("Restoring data...")
  print("\t{db} < {dump}".format(
    db = dbname,
    dump = dbDump
  ))
  os.system("psql -h {host} -U {user} -v --disable-triggers --set ON_ERROR_STOP=on {db} < {dump}".format(
    host = host,
    user = user,
    db = dbname,
    dump = dbDump
  ))
  # os.system("pg_restore -h {host} -U {user} --dbname={db} -a {dump}".format(
  #   host = host,
  #   user = user,
  #   db = dbname,
  #   dump = dbDump
  # ))
  print("~ " * 75)
  print(" - Migrations Done!")
  print("Data loaded successfully!")
except IOError:
  print("There is no file named {dump}!".format(dump = dbDump))