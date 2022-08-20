# Importamos SQALCHEMY LIBRARY para  crear el Metodo ENGINE
from sqlalchemy import create_engine
import pandas as pd 
import psycopg2
from dataclean import datalake
import datetime
from logg import log


    
class dataPostgresql:

    def get_connection():

        user = 'uqmaap1pj5xxhla3libh'
        password = 'fwdCjWHIuTEsPOxTVe5z'
        host = 'bueqgc81zoandrbcwv7p-postgresql.services.clever-cloud.com'
        port = 5432
        database = 'bueqgc81zoandrbcwv7p'
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
        
        try: 
            url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
            conn = psycopg2.connect(url)
            conn.autocommit = True
            log.info(f"La conexión a la Base de datos ha sido Exitosa.")
        except Exception as ex:
            log.info("La conexión ha presentado un error, por favor verificar ")
    
    def tablasNormalizadas():
        tabla=pd.concat(datalake)
        tabla_principal=tabla
        tabla_principal["id"]=tabla_principal.index 
        tabla_principal.reset_index(drop=True, inplace=True)
        tabla_principal.set_index("id", inplace=True)
        tabla_principal["date"]=datetime.date.today().strftime("%Y-%m-%d")

        try:
            tabla_principal.to_sql('principal', url, if_exists='replace')
        except:
            log.info("no se subió a la BBDD")


if __name__ == "__main__":
    dp=dataPostgresql
    dp.get_connection()
    dp.tablasNormalizadas()
    