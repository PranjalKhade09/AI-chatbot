import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="mysql@123",
        database="college_chatbot"
    )
    return connection