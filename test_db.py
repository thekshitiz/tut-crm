import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        # Only specify database if you're sure it exists
        # database='crmdb',  # Comment this out temporarily to test connection
        user='root',
        password='admin',
        port='3306',
        auth_plugin='mysql_native_password'
    )
    
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version", db_info)
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS crmdb")
        cursor.execute("USE crmdb")
        
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database:", record[0])

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    print("If you're using MySQL 8+, try running this SQL command:")
    print("ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin';")
    print("FLUSH PRIVILEGES;")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed") 