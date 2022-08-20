# Importamos SQALCHEMY LIBRARY para  crear el Metodo ENGINE

import psycopg2
from dataclean import datacine
import pandas as pd
import datetime 

# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd 
import psycopg2
from dataclean import datalake, datacine
import datetime


# DEFINE THE DATABASE CREDENTIALS


user = 'akatmacqmmxvep'
password = 'ae6cd4a2cede9d432cce63140dc747190612cf0f88b46daa555f2b420babf213'
host = 'ec2-44-206-137-96.compute-1.amazonaws.com'
port = 5432
database = 'd6mc73d6s2s5oc'
url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)

def get_connection():
    try: 
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
        conn = psycopg2.connect(url)
        conn.autocommit = True
        print(f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def  tablaPrincipal():
    tabla=pd.concat(datalake)
    tabla_principal=tabla
    tabla_principal["id"]=tabla_principal.index 
    tabla_principal.reset_index(drop=True, inplace=True)
    tabla_principal.set_index("id", inplace=True)
    tabla_principal["date"]=datetime.date.today().strftime("%Y-%m-%d")
    print(tabla_principal.columns)

    try:
        tabla_principal.to_sql('tabla_principal', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")


get_connection()
tablaPrincipal()



    