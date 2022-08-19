# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd 
import psycopg2

# DEFINE THE DATABASE CREDENTIALS


user = 'uqmaap1pj5xxhla3libh'
password = 'fwdCjWHIuTEsPOxTVe5z'
host = 'bueqgc81zoandrbcwv7p-postgresql.services.clever-cloud.com'
port = 5432
database = 'bueqgc81zoandrbcwv7p'
url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)

def get_connection():
    try: 
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
        conn = psycopg2.connect(url)
        conn.autocommit = True
        print(f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


def TablaPrincipal():
   






if __name__ == '__main__':
    get_connection()
  
    


        





        
   
  
    
  
    