from database.db import connection

def getReport():
    lista = []
    connect = connection()
    cur = connect.cursor()
    cur.execute("SELECT * FROM reporte") #con esta consulta obtenemos los datos 
    query = cur.fetchall()
    #hacemos un ciclo for para obtener nuestros reportes en un diccionario y luego agregarlos a una lista
    for x in query:
        data = {
        "ID":x[0], 
        "tipo":x[1],
        "fallo":x[2],
        "descripcion":x[3],
        }
        lista.append(data)
    return lista