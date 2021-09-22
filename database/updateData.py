from database.db import connection
import mysql.connector

def updateReport(id, tipo, fallo, descripcion):
    try:
        connect = connection()
        mycursor = connect.cursor()
        query = "UPDATE reporte SET tipo = '{}', fallo = '{}', descripcion = '{}' WHERE id = '{}'".format(tipo, fallo, descripcion, id)
        q = mycursor.execute(query)
        connect.commit()

        if (q):
            print('actualizado')
        else:
            print('error')
        return True

    except Exception as err:
        print('error')
        return False