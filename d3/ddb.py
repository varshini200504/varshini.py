import pymysql
def connect_db():
    try:
        connection=pymysql.Connect(host='localhost',
                                port=3306,
                                user='root',
                                password='root',
                                database='varshini_db',
                                charset='utf8')
        print("DB connnected")
        return connection
    except:
        print("db connection failed")
def disconnect_db(connection):
    try:
        connection.close()
        print("database disconnected")
    except:
        print("db dis connection failed")

def create_db():
    connection=connect_db()
    query='create database if not exists varshini_db;'
    cursor=connection.cursor()
    cursor.close()
    disconnect_db(connection)
def insert_row():
    connection=connect_db()

connection=connect_db()
if connection:
    disconnect_db(connection)
    
