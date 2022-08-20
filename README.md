# Alkemy Reto de Data Analyst + Python  @jeanvitola

## Deploy :factory:

## ¿ Comó ejecuto el ETL? :question:

### Configurar un ambiente virtual (virtual environment)

- #### 1) instalamos, creamos y ejecutamos un virtual environment (en este caso virtualenv)

  - `[user@localhost]$ pip install virtualenv `
  - `[user@localhost]$ virtualenv data`  *En este caso data es el nombre del ambiente virtual*
  - `[user@localhost]$ source  data/bin/activate` en windows
  - `[user@localhost]$ /data/bin/activate.sh` en Linux
  

*Los siguientes comandos se ejecutan desde una terminal cmd, powershell, bash o similar.*


- #### 2)  Instalar las dependencias 

   *En el archivo requirements.txt encontramos todas las librerías utilizadas para el funcionamiento
   del proyecto*
  - `pip -r install requirements.txt`

- #### 3) Configurar conexión a la base de datos en el archivo datalake.py
 ```
-user = ''
-password = ''
-host = ''
-port = 5432
-database = ''
-url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
```
*Hay que estipular las credenciales de acceso a la base de datos de nuestra ETL que estan en nuestro archivo `datalake.py`*

- #### 4) ejecutar :snake:
 *Para correr el programa ETL, que en terminos sencillo extrae la información a tráves de una petición GET, procesa la información  hacineod una limpieza y ifltrando seguún los requerimientos y los sube a una base de datos determinadas, simplemente nos pocicionamos en la carpeta de los archivos y ejecutamos el archivo padre  `main.py`.*

- `python main.py`
- ![image](https://user-images.githubusercontent.com/75003188/185765331-c03a625d-631b-4839-bef0-9552654d0470.png)

- #### 5) Archivos :computer:
- `dataextract.py` : *Acá encontramos la extracción de datos de la página fuente y los guarda en en sistema con el nombre asignado*
- `dataclean.py` : *En este archivo se procesa la información, se cargan los csv y se sacan las categorías de interes para trabajar*
- `datalake.py` : *Se hace la conexión a la base de datos,ademas que se hacen algunas operaciones con las tablas y se suben a la misma*
- `logg.py`     : *Acá se arma el Log el cual será el archvio del sistema de eventos, para eso crea un  etl.log*


- #### 5) Imágenes :computer:
![image](https://user-images.githubusercontent.com/75003188/185765700-906d8630-9c04-41fe-8e58-ef35c01740ef.png)
![image](https://user-images.githubusercontent.com/75003188/185765715-ee3714bf-da05-4425-afd8-e6bd11ccd831.png)


