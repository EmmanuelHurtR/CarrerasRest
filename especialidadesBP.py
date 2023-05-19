from flask import Blueprint, request
from model import Conexion
from flask_httpauth import HTTPBasicAuth

especialidadBP=Blueprint("especialidadBP", __name__)

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

@especialidadBP.route('/Carreras/especialidad', methods=['POST'])
@auth.login_required(role=['A', 'E', 'D'])
def agregarEspecialidad():
    cn=Conexion()
    datos=request.get_json()
    return cn.insertar_planEstudio(datos)

@especialidadBP.route('/Carreras/especialidad', methods=['GET'])
@auth.login_required(role=['A'])
def ConsultaEspecialidad():
    cn=Conexion()
    return cn.consultarPlanesEstudio()

@especialidadBP.route('/Carreras/especialidad', methods=['PUT'])
@auth.login_required(role='A')
def modificarEspecialidad():
    cn=Conexion()
    datos=request.get_json()
    return cn.modificarEspecialidades()

@especialidadBP.route('/Carreras/especialidad<int:id>', methods=['DELETE'])
@auth.login_required(role='A')
def eliminarEspecialidad(id):
    cn=Conexion()
    return cn.eliminarEspecialidad(id)