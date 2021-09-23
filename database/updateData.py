from database.db import connection
import mysql.connector

#la funcion updateReport, recibe por parametros los datos ingresados
def updateReport(id, tipo, fallo, descripcion):
    try:
        #usamos la funcion connection del archivo db.py para conectarnos con nuestra base de datos
        connect = connection()
        mycursor = connect.cursor()
        #con esta consulta actualizamos los datos
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