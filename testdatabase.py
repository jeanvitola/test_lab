# Importamos SQALCHEMY LIBRARY para  crear el Metodo ENGINE

import psycopg2
from dataclean import datacine
import pandas as pd
import datetime 

df_cines_data=pd.concat(datacine)
df_cines_data=df_cines_data[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
df_cines_data.dtypes
df_cines_data['espacio_INCAA'] = df_cines_data['espacio_INCAA'].replace('SI', 'si').replace('si', 1)
df_cines_data['espacio_INCAA'] = df_cines_data['espacio_INCAA'].fillna(0)
df_cines_data['espacio_INCAA'] = df_cines_data['espacio_INCAA'].astype("int")
tabla_provincia= df_cines_data.groupby('Provincia').sum()
tabla_provincia["date"]=datetime.date.today().strftime("%Y-%m-%d")
print(tabla_provincia.columns)
    