import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    passwd = os.getenv("DB_PASS")
)

# preparing cursor object
cursor = db.cursor()

# creating db
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')};")

print("DB created!")