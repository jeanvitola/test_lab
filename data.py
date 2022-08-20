from dataclean import datalake  
import pandas as pd  
import datetime 

tabla=pd.concat(datalake)


def tablaPrincipal():
    tabla_principal=tabla
    tabla_principal["id"]=tabla_principal.index 
    tabla_principal.reset_index(drop=True, inplace=True)
    tabla_principal.set_index("id", inplace=True)
    tabla_principal["date"]=datetime.date.today().strftime("%Y-%m-%d") 
    print(tabla_principal.columns)



tablaPrincipal()