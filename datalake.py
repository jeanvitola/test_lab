# IMPORTAMOS EL SQALCHEMY LIBRARY's PARA CREAR EL CREATE_ENGINE
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
from dataclean import datalake, datacine
import datetime
from logg import log


user = 'akatmacqmmxvep'
password = 'ae6cd4a2cede9d432cce63140dc747190612cf0f88b46daa555f2b420babf213'
host = 'ec2-44-206-137-96.compute-1.amazonaws.com'
port = 5432
database = 'd6mc73d6s2s5oc'
url = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database)


class databasePostgresql:

    """Esta clase se encarga de  iniciar la conexión a la base de datos determinada por el usuario, luego del autenticación procede a crear y subir las tablas de acuerdo
    a los requisitos estipulados  en el archivo """

    def get_connection():
        log.info('Iniciando la conexión a la base de datos')
        try:
            url = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database)
            conn = psycopg2.connect(url)
            conn.autocommit = True
            print(f"La conexión al {host}  con el  {user}  ha iniciado.")
        except Exception as ex:
            print("La conexión a la base de datos ha presentado un error: \n", ex)

    def tablaPrincipal():
        tabla = pd.concat(datalake)
        tabla_principal = tabla
        tabla_principal["id"] = tabla_principal.index
        tabla_principal.reset_index(drop=True, inplace=True)
        tabla_principal.set_index("id", inplace=True)
        tabla_principal["date"] = datetime.date.today().strftime("%Y-%m-%d")

        try:
            tabla_principal.to_sql('tabla_principal', url, if_exists='replace')
            log.info('TablaPrincipal se ha cargado')

        except:
            print("no se subió a la BBDD")

        # ----------> TABLA DE CATEGORÍA Y CANTIDAD<------------------------

        categ_cant = tabla.groupby('categoria', as_index=False).size()
        categ_cant = categ_cant.rename(columns={'size': 'cantidad'})
        categ_cant["date"] = datetime.date.today().strftime("%Y-%m-%d")
        categ_cant
        try:
            categ_cant.to_sql('tablaCategoria', url, if_exists='replace')
            log.info('tablaCategoria se ha cargado')

        except:
            print("no se subió tablaCategoria a la BBDD")

        # ---------> TABLA DE CANTIDAD POR FUENTES <---------------------------

        fuente = list()
        for name, df in tabla.items():
            fuente.append({'fuente': name, 'cantidad': df.size, })

        tabla_fuente = pd.DataFrame(fuente)
        tabla_fuente["date"] = datetime.date.today().strftime("%Y-%m-%d")
        tabla_fuente

        try:
            tabla_fuente.to_sql('tablaFuente', url, if_exists='replace')
            log.info('TablaFuente se ha cargado')

        except:
            print("no se subió tablaFuente a la BBDD")

    # -------------------> TABLA PROVINCIA, CANTIDAD, FUENTE   <---------------------

        provi_cant = tabla.groupby(
            ['categoria', 'provincia'], as_index=False).size()
        provi_cant = provi_cant.rename(columns={'size': 'cantidad'})
        provi_cant["date"] = datetime.date.today().strftime("%Y-%m-%d")
        provi_cant

        try:
            provi_cant.to_sql('tablaProvincia', url, if_exists='replace')
            log.info('tablaProvincia se ha cargado')

        except:
            print("no se subió tablaProvincia la BBDD")

    # -------------------> TABLA CINE <-----------------------------------
        df_cines_data = pd.concat(datacine)
        df_cines_data = df_cines_data[[
            'Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
        df_cines_data.dtypes
        df_cines_data['espacio_INCAA'] = df_cines_data['espacio_INCAA'].replace(
            'SI', 'si').replace('si', 1)
        df_cines_data['espacio_INCAA'] = df_cines_data['espacio_INCAA'].fillna(
            0)
        df_cines_data['espacio_INCAA'] = df_cines_data['espacio_INCAA'].astype(
            "int")
        tabla_cine = df_cines_data.groupby('Provincia').sum()
        tabla_cine["date"] = datetime.date.today().strftime("%Y-%m-%d")
        tabla_cine
        try:
            tabla_cine.to_sql('tablaCine', url, if_exists='replace')
            log.info('TablaCine se ha cargado')

        except:
            print("no se subió TablaCine la BBDD")


dp = databasePostgresql
dp.get_connection()
dp.tablaPrincipal()
