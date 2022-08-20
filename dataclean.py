import pandas as pd
from logg import log


datalake = []
datacine=[]


class data_clean:

    """Esta clase contiene las funciones donde se extraerán las categorías de interés de los tres principales archivos """

    def extract_museo():
        log.info('Extrayendo categorías de  Museo')
        data = pd.read_csv('museos/2022-julio/museos-24-07-2022.csv')
        df_transform = pd.DataFrame()
        df_transform.insert(0, 'cod_localidad', data['Cod_Loc'].astype(str))
        df_transform.insert(1, 'id_provincia', data['IdProvincia'])
        df_transform.insert(2, 'id_departamento', data['IdDepartamento'])
        df_transform.insert(3, 'categoria', data['categoria'])
        df_transform.insert(4, 'provincia', data['provincia'])
        df_transform.insert(5, 'localidad', data['localidad'])
        df_transform.insert(6, 'nombre', data['nombre'])
        df_transform.insert(7, 'domicilio', data['direccion'])
        df_transform.insert(8, 'codigo_postal', data['CP'])
        df_transform.insert(9, 'numero_telefono', data['telefono'])
        df_transform.insert(10, 'mail', data['Mail'])
        df_transform.insert(11, 'web', data['Web'])
        datalake.append(df_transform)

    def extract_cine():
        log.info('Extrayendo categorías de  Cine')
        data = pd.read_csv('cines/2022-julio/cines-24-07-2022.csv')
        cine = data
        df_transform = pd.DataFrame()
        df_transform.insert(0, 'cod_localidad', data['Cod_Loc'].astype(str))
        df_transform.insert(1, 'id_provincia', data['IdProvincia'])
        df_transform.insert(2, 'id_departamento', data['IdDepartamento'])
        df_transform.insert(3, 'categoria', data['Categoría'])
        df_transform.insert(4, 'provincia', data['Provincia'])
        df_transform.insert(5, 'localidad', data['Localidad'])
        df_transform.insert(6, 'nombre', data['Nombre'])
        df_transform.insert(7, 'domicilio', data['Dirección'])
        df_transform.insert(8, 'codigo_postal', data['CP'])
        df_transform.insert(9, 'numero_telefono', data['Teléfono'])
        df_transform.insert(10, 'mail', data['Mail'])
        df_transform.insert(11, 'web', data['Web'])
        datalake.append(df_transform)
        datacine.append(data)

    def extract_bibliotecas():
        log.info('Extrayendo categorías de bibliotecas')
        data = pd.read_csv('bibliotecas/2022-julio/bibliotecas-24-07-2022.csv')
        df_transform = pd.DataFrame()
        df_transform.insert(0, 'cod_localidad', data['Cod_Loc'].astype(str))
        df_transform.insert(1, 'id_provincia', data['IdProvincia'])
        df_transform.insert(2, 'id_departamento', data['IdDepartamento'])
        df_transform.insert(3, 'categoria', data['Categoría'])
        df_transform.insert(4, 'provincia', data['Provincia'])
        df_transform.insert(5, 'localidad', data['Localidad'])
        df_transform.insert(6, 'nombre', data['Nombre'])
        df_transform.insert(7, 'domicilio', data['Domicilio'])
        df_transform.insert(8, 'codigo_postal', data['CP'])
        df_transform.insert(9, 'numero_telefono', data['Teléfono'])
        df_transform.insert(10, 'mail', data['Mail'])
        df_transform.insert(11, 'web', data['Web'])
        datalake.append(df_transform)

    def concat_data():
        tabla_principal = pd.concat(datalake)
        try:
            tabla_principal.to_csv("tabla_principal.csv", index=False)
        except:
            log.info('El archivo de tabla_principal ya existe')


log.info('Transformación de datos en proceso')
dc = data_clean
dc.extract_museo()
dc.extract_cine()
dc.extract_bibliotecas()
dc.concat_data()
log.info('Extración y limpieza de datos terminada')