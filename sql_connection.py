import mysql.connector

def get_sql_connection():
    connection = mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database_name'
    )
    return connection
