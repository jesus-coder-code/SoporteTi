from flask import Flask, request, jsonify
from database.db import connection
from database.getData import getReport
from database.postData import createReport
import os
app = Flask(__name__)

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

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
    #app.run(debug = True)