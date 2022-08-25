import pymysql
import sys

# Create a connection object
Host = "localhost" 
User = "Freezer"       
Password = "freezer"           

try:
    conn  = pymysql.connect(host=Host, user=User, password=Password)
except pymysql.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Create a cursor object
cur  = conn.cursor()
# creating database 
cur.execute("CREATE DATABASE IF NOT EXISTS FREEZER ") 
  
cur.execute("USE FREEZER")
  
for database in databaseList:
  print(database)
    
conn.close()