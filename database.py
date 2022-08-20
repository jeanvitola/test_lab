# Importamos SQALCHEMY LIBRARY para  crear el Metodo ENGINE
from sqlalchemy import create_engine
import pandas as pd 
import psycopg2
from dataclean import datalake
import datetime
from logg import log

#Definimos las credenciales de la Base de datos

class dataPostgresql:
    """ En esta clase definimos las credenciales para conexión a  la base de datos utilizada que en este caso es PostgreSQL,
        tambien se establece la carga de dataframe para la transformación de los mismos y luego subirlos a la base de datos de forma correcta.

    Credenciales:
    user = usuario para autenticarse en la BBDD
    password =  contraseña para autenticarse en la BDD
    host =  host de la BBDD 
    port =  Puerto (5432 por defecto)
    database = nombre de la base de datos
    """

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
            log.info(f"La conexión al {host} con usuario {user} ha sido exitosa.")
        except Exception as ex:
            log.info("La conexión ha presentado un error, por favor verificar", ex)

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

        #Tabla de categoria y cantidad
        categ_cant= tabla_principal.groupby('categoria', as_index=False).size()
        categ_cant=categ_cant.rename(columns={'size':'cantidad'})
        categ_cant["date"]=datetime.date.today().strftime("%Y-%m-%d")
        categ_cant
        try:
            categ_cant.to_sql('categoriaCantidad', url, if_exists='replace')
            log.info('La carga de la tabla principal ha sido Extiosa')

        except Exception as e:
            log.info('no se subió a la BBDD')


        # Tabla de cantidad por fuente

        fuente=list()
        for name, df in tabla.items():
            fuente.append({'fuente':name,'cantidad':df.size,})

        tabla_fuente=pd.DataFrame(fuente)
        tabla_fuente["date"]=datetime.date.today().strftime("%Y-%m-%d")
        tabla_fuente

        try:
            tabla_fuente.to_sql('CantidadFuente', url, if_exists='replace')
            log.info('La carga de tabla_fuente se ha realizado')

        except:
            print("no se subió a la BBDD")

        #Tabla de cantidad, proviencia y fuente
    
        provi_cant=tabla_principal.groupby(['categoria','provincia'], as_index=False).size()
        provi_cant=provi_cant.rename(columns={'size':'cantidad'})
        provi_cant["date"]=datetime.date.today().strftime("%Y-%m-%d")
        provi_cant

        try:
            provi_cant.to_sql('provinciFuente', url, if_exists='replace')
            log.info('La carga de provi_cant se ha realizado')

        except:
            print("no se subió a la BBDD")


if __name__ == '__main__':
    dp=dataPostgresql
    dp.get_connection()
    dp.tablaPrincipal()
    
  
    


        





        
   
  
    
  
    