from flask import Blueprint, request
from model import Conexion
from flask_httpauth import HTTPBasicAuth

carreraBP=Blueprint("carreraBP", __name__)
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

@carreraBP.route('/Carreras',methods=['GET'])
@auth.login_required(role=['A', 'E', 'D'])
def consultaCarreras():
    cn=Conexion()
    return cn.consultarCarreras()

@carreraBP.route('/Carreras/<int:id>',methods=['GET'])
@auth.login_required(role=['A', 'E', 'D'])
def consultarCarreraID(id):
    cn=Conexion()
    return cn.consultarCarreraID(id)

@carreraBP.route('/Carreras',methods=['POST'])
@auth.login_required(role='A')
def agregarCarrera():
    cn=Conexion()
    datos=request.get_json()
    return cn.insertar_carrera(datos)

@carreraBP.route("/Carreras", methods=['PUT'])
@auth.login_required(role='A')
def modificarCarrera():
    cn = Conexion()
    datos = request.get_json()
    return cn.modificarCarrera(datos)

@carreraBP.route('/Carreras/<int:id>', methods=['DELETE'])
@auth.login_required(role='A')
def eliminarCarrera(id):
    cn=Conexion()
    return cn.eliminarCarrera(id)


