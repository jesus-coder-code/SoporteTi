from database.db import connection

def getReport():
    lista = []
    connect = connection()
    cur = connect.cursor()
    cur.execute("SELECT * FROM reporte")
    query = cur.fetchall()
    for x in query:
        data = {
        "ID":x[0], 
        "tipo":x[1],
        "fallo":x[2],
        "descripcion":x[3],
        }
        lista.append(data)
    return lista