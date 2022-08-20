DROP DATABASE IF EXISTS  python_data;

CREATE DATABASE python_data;



CREATE TABLE IF NOT EXISTS tabla_principal (
   id   serial PRIMARY KEY,
   cod_localidad   VARCHAR(50),
   id_provincia   VARCHAR(10),
   id_departamento   VARCHAR(10),,
   categoria   VARCHAR(100),
   provincia   VARCHAR(100),
   localidad   VARCHAR(100),
   nombre   VARCHAR(100),
   domicilio   VARCHAR(100),
   codigo_postal   VARCHAR(100),
   numero_telefono   VARCHAR(100),
   mail   VARCHAR(100),
   web   VARCHAR(100),
   date   DATE
);




CREATE TABLE IF NOT EXISTS tablaCategoria (
   categoria   VARCHAR(20),
   cantidad   NUMERIC,
   date   DATE
);


CREATE TABLE IF NOT EXISTS tablaCine (
   Provincia   VARCHAR(100),
   Pantallas   INTEGER,
   Butacas   INTEGER,
   espacio_INCAA   INTEGER,
   date   DATE
);

CREATE TABLE IF NOT EXISTS tablaFuente (
   fuente   VARCHAR(100),
   cantidad   INTEGER,
   date   DATE
) ;


CREATE TABLE IF NOT EXISTS tablaProvincia (
   categoria   VARCHAR(100),
   provincia   VARCHAR(100),
   cantidad    INTEGER,
   date        DATE
);

