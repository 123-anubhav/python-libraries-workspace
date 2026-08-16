import configparser
import os
from http import HTTPStatus

import mysql.connector as mysql

import user_dto

# 1. Initialize the parser
config = configparser.ConfigParser()

# 2. Get absolute path to prevent file-not-found errors
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, 'config.db')

# 3. Read the configuration file
config.read(config_path)

# 4. Extract credentials using section and keys
db_host = config.get('database', 'host')
db_user = config.get('database', 'user')
db_password = config.get('database', 'password')
db_name = config.get('database', 'database')
db_port = config.getint('database', 'port')

# Example print to verify it works
print(f"Connecting to {db_name} at {db_host}...")

def connect_to_db():
    connection = mysql.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        db=db_name
    )
    print("connected to database")
    return connection

def create_tables():
    connection = connect_to_db()
    cursor = connection.cursor()
    query = """
           CREATE TABLE IF NOT EXISTS users (
                userid INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                city VARCHAR(255),
                mobile VARCHAR(255)
         )"""

    try:
        cursor.execute(query)
        connection.commit()
        print("Tables created successfully")
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        connection.close()


def insert_user(user:user_dto.UserDto):
    connection = connect_to_db()
    cursor = connection.cursor()

    query = " INSERT INTO users (username, city) VALUES (%s, %s)"
    values=(user.username, user.city)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message":"User created successfully",
        "user":user.username,
        "success":True,
        "status_code":HTTPStatus.CREATED
    }

def get_all_users():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)  # when dictionary=True it give json data otherwise list data return
    query = " SELECT * FROM users"
    cursor.execute(query)
    get_users = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return get_users