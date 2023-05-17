from flask import Flask
from carrerasBP import carreraBP
from planesEstudiosBP import planeEstudioBP

app=Flask(__name__)
app.register_blueprint(carreraBP) #Cargar la funcionalidad inclueda en el componente solicitudBPV2
app.register_blueprint(planeEstudioBP)

@app.route('/',methods=['GET'])
def init():
    return {"mensaje":"Escuchando el Servicio REST de Carreras"}

#Manipulaciones de errores
@app.errorhandler(404)
def errorinterno(e):
    respuesta={"estatus":"Error","mensaje":"Recurso no disponible, contacta al administrador del servicio"}
    return respuesta

if __name__=='__main__':
    init
    app.run(debug=True)