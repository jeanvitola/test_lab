import pandas as pd 
from logg import log

conjunto=[]


def extract_museo():
  data=pd.read_csv('museos/2022-julio/museos-24-07-2022.csv')
  df_transform=pd.DataFrame()
  df_transform.insert(0, 'cod_localidad', data['Cod_Loc'].astype(str))
  df_transform.insert(1, 'id_provincia', data['IdProvincia'])
  df_transform.insert(2, 'id_departamento', data['IdDepartamento'])
  df_transform.insert(3, 'categoria', data['categoria'])
  df_transform.insert(4, 'provincia', data['provincia'])
  df_transform.insert(5, 'localidad', data['localidad'])
  df_transform.insert(6, 'nombre', data['nombre'])
  df_transform.insert(7, 'domicilio', data['direccion'])
  df_transform.insert(8, 'codigo_postal', data['CP'])
  df_transform.insert(9,'numero_telefono', data['telefono'])
  df_transform.insert(10,'mail', data['Mail'])
  df_transform.insert(11, 'web', data['Web'])
  conjunto.append(df_transform)

def extract_cine():
  data = pd.read_csv('cines/2022-julio/cines-24-07-2022.csv')
  df_transform=pd.DataFrame()
  df_transform.insert(0, 'cod_localidad', data['Cod_Loc'].astype(str))
  df_transform.insert(1, 'id_provincia', data['IdProvincia'])
  df_transform.insert(2, 'id_departamento', data['IdDepartamento'])
  df_transform.insert(3, 'categoria', data['Categoría'])
  df_transform.insert(4, 'provincia', data['Provincia'])
  df_transform.insert(5, 'localidad', data['Localidad'])
  df_transform.insert(6, 'nombre', data['Nombre'])
  df_transform.insert(7, 'domicilio', data['Dirección'])
  df_transform.insert(8, 'codigo_postal', data['CP'])
  df_transform.insert(9,'numero_telefono', data['Teléfono'])
  df_transform.insert(10,'mail', data['Mail'])
  df_transform.insert(11, 'web', data['Web'])
  conjunto.append(df_transform)

def extract_bibliotecas():
  data = pd.read_csv('bibliotecas/2022-julio/bibliotecas-24-07-2022.csv')
  df_transform=pd.DataFrame()
  df_transform.insert(0, 'cod_localidad', data['Cod_Loc'].astype(str))
  df_transform.insert(1, 'id_provincia', data['IdProvincia'])
  df_transform.insert(2, 'id_departamento', data['IdDepartamento'])
  df_transform.insert(3, 'categoria', data['Categoría'])
  df_transform.insert(4, 'provincia', data['Provincia'])
  df_transform.insert(5, 'localidad', data['Localidad'])
  df_transform.insert(6, 'nombre', data['Nombre'])
  df_transform.insert(7, 'domicilio', data['Domicilio'])
  df_transform.insert(8, 'codigo_postal', data['CP'])
  df_transform.insert(9,'numero_telefono', data['Teléfono'])
  df_transform.insert(10,'mail', data['Mail'])
  df_transform.insert(11, 'web', data['Web'])
  conjunto.append(df_transform)
 
def  concat_data():
    tabla_principal=pd.concat(conjunto)
    try:
        tabla_principal.to_csv("tabla_principal2.csv", index=False)
    except:
        print("El archivo ya existe")

extract_museo()
extract_cine()
extract_bibliotecas()
concat_data()
