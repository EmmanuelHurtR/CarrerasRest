from flask import Blueprint, request
from model import Conexion

planeEstudioBP=Blueprint("planeEstudioBP", __name__)

@planeEstudioBP.route('/Carreras/planEstudio', methods=['POST'])
def agregarPlanEstudio():
    cn=Conexion()
    datos=request.get_json()
    return cn.insertar_planEstudio(datos)

@planeEstudioBP.route('/Carreras/planEstudio', methods=['GET'])
def ConsultaPlanesEstudio():
    cn=Conexion()
    return cn.consultarPlanesEstudio()