# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd 
import psycopg2
from dataclean import datalake
import datetime


# DEFINE THE DATABASE CREDENTIALS


user = 'ukpkzzxlojkufjupphf4'
password = '3szfJwiWmZ2rmHmxbxxq'
host = 'bkoipdkx2waraakv4cc1-postgresql.services.clever-cloud.com'
port = 5432
database = 'bkoipdkx2waraakv4cc1'
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

    #----------> TABLA DE CATEGORÍA Y CANTIDAD<------------------------ 

    categ_cant= tabla.groupby('categoria', as_index=False).size()
    categ_cant=categ_cant.rename(columns={'size':'cantidad'})
    categ_cant["date"]=datetime.date.today().strftime("%Y-%m-%d")
    categ_cant
    try:
        categ_cant.to_sql('tablaCategoria', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")


    #---------> TABLA DE CANTIDAD POR FUENTES <---------------------------
 
    fuente=list()
    for name, df in tabla.items():
        fuente.append({'fuente':name,'cantidad':df.size,})

    tabla_fuente=pd.DataFrame(fuente)
    tabla_fuente["date"]=datetime.date.today().strftime("%Y-%m-%d")
    tabla_fuente

    try:
        tabla_fuente.to_sql('tablaCategoria', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")

  #Tabla de cantidad, proviencia y fuente
  
    provi_cant=tabla.groupby(['categoria','provincia'], as_index=False).size()
    provi_cant=provi_cant.rename(columns={'size':'cantidad'})
    provi_cant["date"]=datetime.date.today().strftime("%Y-%m-%d")
    provi_cant

    try:
        provi_cant.to_sql('tablaCategoria', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")


   


get_connection()
tablaPrincipal()
    