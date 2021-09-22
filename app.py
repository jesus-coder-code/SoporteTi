from flask import Flask, request, jsonify
from flask_cors import CORS
from database.db import connection
from database.getData import getReport
from database.postData import createReport
from database.updateData import updateReport
import os
app = Flask(__name__)
CORS(app)

@app.route("/get", methods=['GET'])
def get():
    report = getReport()
    try:
        if report:
            return jsonify(report)
        else:
            return {'mensaje':'no hay datos'}
    except:
        return {'mensaje':'arregla esa monda'}

@app.route("/create", methods=["POST"])
def create():
    try:
        add = request.json
        tipo = add['tipo']
        fallo = add['fallo']
        descripcion = add['descripcion']

        if createReport(tipo, fallo, descripcion):
            return jsonify({'mensaje':'reporte creado'})
        else:
            return jsonify({'mensaje':'error'})
        
    except Exception as error:
        print(error);
        return {'mensaje':'arregla esa monda'}

@app.route("/update/<id>", methods=["PUT"])
def update(id):
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


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
    #app.run(debug = True)