import psycopg2

from config import config

#Establishing the connection

#Obtain the configuration parameters
params = config()

#Connect to the PostgreSQL database
conn = psycopg2.connect(**params)

conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database publictransport''';

#Creating a database
cursor.execute(sql)
print("Database created successfully")

#Closing the connection
conn.close()