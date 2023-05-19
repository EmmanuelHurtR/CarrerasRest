from flask import Blueprint, request
from model import Conexion
from flask_httpauth import HTTPBasicAuth

planeEstudioBP=Blueprint("planeEstudioBP", __name__)
auth=HTTPBasicAuth()

@auth.verify_password
def login(username, password):
    cn=Conexion()
    user=cn.validarCredenciales(username, password)
    if user!=None:
        return user
    else:
        return False

@auth.get_user_roles
def get_user_roles(user):
    return user["tipo"]

@auth.error_handler
def error_handler():
    return {"estatus":"Error", "mensaje":"Autorizacion denegana, usted no cuenta con los permisos necesarios para realizar esta accion"}

@planeEstudioBP.route('/PlanesEstudio', methods=['GET'])
@auth.login_required(role=['A', 'E', 'D'])
def ConsultaPlanesEstudio():
    cn=Conexion()
    return cn.consultarPlanesEstudio()

@planeEstudioBP.route('/PlanesEstudio', methods=['POST'])
@auth.login_required(role='A')
def agregarPlanEstudio():
    cn=Conexion()
    datos=request.get_json()
    return cn.insertar_planEstudio(datos)

@planeEstudioBP.route("/PlanesEstudio", methods=['PUT'])
@auth.login_required(role='A')
def modificarCarrera():
    cn = Conexion()
    datos = request.get_json()
    return cn.modificarPlanesEstudio(datos)

@planeEstudioBP.route('/PlanesEstudio/<int:id>', methods=['DELETE'])
@auth.login_required(role='A')
def eliminarPlanEstudio(id):
    cn=Conexion()
    return cn.eliminarPlanEstudio(id)
