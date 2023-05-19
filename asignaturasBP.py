from flask import Blueprint, request
from model import Conexion
from flask_httpauth import HTTPBasicAuth

asignaturasBP=Blueprint("asignaturasBP", __name__)
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

@asignaturasBP.route('/asignaturas',methods=['GET'])
@auth.login_required(role=['A', 'E', 'D'])
def consultaAsignaturas():
    cn=Conexion()
    return cn.consultarAsignaturas()

@asignaturasBP.route('/asignaturas',methods=['POST'])
@auth.login_required(role='A')
def agregarAsignatura():
    cn=Conexion()
    datos=request.get_json()
    return cn.insertar_asignatura(datos)

@asignaturasBP.route("/asignaturas", methods=['PUT'])
@auth.login_required(role='A')
def modificarAsignatura():
    cn = Conexion()
    datos = request.get_json()
    return cn.modificarAsignatura(datos)

@asignaturasBP.route('/asignaturas/<int:id>', methods=['DELETE'])
@auth.login_required(role='A')
def eliminarAsignatura(id):
    cn=Conexion()
    return cn.eliminarAsignatura(id)