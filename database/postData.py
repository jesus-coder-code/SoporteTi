import mysql.connector
from database.db import connection

def createReport(tipo, fallo, descripcion):
    try:
        connect = connection();
        mycursor = connect.cursor()
        query = "INSERT INTO reporte (tipo, fallo, descripcion) VALUES (%s, %s, %s)"
        values = (tipo, fallo, descripcion)
        mycursor.execute(query, values)
        connect.commit()
        return True
    except Exception as err:
        print(err);
        return False
