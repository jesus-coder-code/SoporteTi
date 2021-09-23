from flask import Flask, request, jsonify
from flask_cors import CORS
from database.db import connection
from database.getData import getReport
from database.postData import createReport
from database.updateData import updateReport
import os
app = Flask(__name__)
#usamos CORS para que nuestra api se conecte a nuestro frontend
CORS(app)

#endpoint del metodo get para obtener los datos
@app.route("/get", methods=['GET'])
def get():
    #usamos la funcion getReport del archivo getData.py para generar nuestro json con los datos
    report = getReport()
    try:
        if report:
            #si hay datos, convierte esto en json y los muestra, sino, nos enviara un mensaje diciendo que no hay datos
            return jsonify(report)
        else:
            return {'mensaje':'no hay datos'}
    except:
        return {'mensaje':'arregla esa monda'}

#endpoint del metodo post para crear registros
@app.route("/create", methods=["POST"])
def create():
    try:
        add = request.json
        tipo = add['tipo']
        fallo = add['fallo']
        descripcion = add['descripcion']

        #pasaremos los datos ingresados por parametros, usando la funcion createReport del archivo postData.py
        if createReport(tipo, fallo, descripcion):
            return jsonify({'mensaje':'reporte creado'})
        else:
            return jsonify({'mensaje':'error'})
        
    except Exception as error:
        print(error);
        return {'mensaje':'arregla esa monda'}

@app.route("/update/<id>", methods=["PUT"])
def update(id):
    #endpoint con el metodo put, para actualizar los registros, pasamos por parametros usando la funcion updateReport del archivo updateData.py
    try:
        add = request.json
        tipo = add['tipo']
        fallo = add['fallo']
        descripcion = add['descripcion']

        if updateReport(id, tipo, fallo, descripcion):
            return jsonify({'mensaje':'reporte actualizado'})
        else:
            return jsonify({'mensaje':'error al actualizar el reporte'})
    except:
        return jsonify({'mensaje':'hubo un error inesperado'})

#configuracion para hacer deploy en heroku
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
    #app.run(debug = True)