import mariadb

config ={
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'sesiones',
}

DB = mariadb.connect(**config)
DB.autocommit= True