# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd 
import psycopg2
from dataclean import conjunto 
import datetime


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

def  tablaPrincipal():
    tabla=pd.concat(conjunto)
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

    #Tabla de categoria y cantidad
    categ_cant= tabla_principal.groupby('categoria', as_index=False).size()
    categ_cant=categ_cant.rename(columns={'size':'cantidad'})
    categ_cant["date"]=datetime.date.today().strftime("%Y-%m-%d")
    categ_cant
    try:
        categ_cant.to_sql('tablaCategoria', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")


    # Tabla de cantidad por fuente
 
    fuente=list()
    for name, df in tabla.items():
        fuente.append({'fuente':name,'cantidad':df.size,})

    tabla_fuente=pd.DataFrame(fuente)
    tabla_fuente["date"]=datetime.date.today().strftime("%Y-%m-%d")
    tabla_fuente

    try:
        categ_cant.to_sql('tablaCategoria', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")

  #Tabla de cantidad, proviencia y fuente
  
    provi_cant=tabla_principal.groupby(['categoria','provincia'], as_index=False).size()
    provi_cant=provi_cant.rename(columns={'size':'cantidad'})
    provi_cant["date"]=datetime.date.today().strftime("%Y-%m-%d")
    provi_cant

    try:
        categ_cant.to_sql('tablaCategoria', url, if_exists='replace')

    except:
        print("no se subió a la BBDD")





if __name__ == '__main__':
    get_connection()
    tablaPrincipal()
    
  
    


        





        
   
  
    
  
    