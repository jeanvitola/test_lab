import pandas as pd
import datetime
from logger_base import log
import psycopg2
from sqlalchemy import create_engine
import numpy as np


class PostgresClient:

    db_host = ""
    db_port = 5432
    db_name = ""
    db_user = ""
    db_password = ""
    conn: psycopg2

    def __init__(self, user="", passwd="", dbn="", host="", port=5458):
        self.db_host = host or config('DB_HOST', default='localhost')
        self.db_port = port or config('DB_PORT', cast=int, default=5458)
        self.db_name = dbn or config('DB_NAME')
        self.db_user = user or config('DB_USER')
        self.db_password = passwd or config('DB_PASSWORD')
        self.database_url = config('DATABASE_URL')
        self.engine = create_engine(self.database_url)

        try:
            conn_str = f"host={self.db_host} port={self.db_port} dbname={self.db_name} user={self.db_user} password={self.db_password}"
            self.conn = psycopg2.connect(conn_str)
            self.conn.autocommit = True
            log.info('Engine creado con éxito')
            log.info(f'Conectado con éxito a {self.db_name}')
        except psycopg2.Error as e:
            log.error(f'Error de conexión {e}')