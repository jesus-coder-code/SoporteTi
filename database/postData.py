import mysql.connector
from database.db import connection

#igual que la funcion updateReport, recibimos los datos por parametros
def createReport(tipo, fallo, descripcion):
    try:
        connect = connection() #conectamos a la base de datos
        mycursor = connect.cursor()
        #consulta para crear el nuevo reporte en la base de datos
        query = "INSERT INTO reporte (tipo, fallo, descripcion) VALUES (%s, %s, %s)"
        values = (tipo, fallo, descripcion)
        mycursor.execute(query, values)
        connect.commit()
        return True
    except Exception as err:
        #si ocurre un error, lo imprime en consola
        print(err);
        return False
