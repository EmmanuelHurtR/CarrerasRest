from flask import Blueprint, request
from model import Conexion

carreraBP=Blueprint("carreraBP", __name__)

@carreraBP.route('/Carreras',methods=['POST'])
def agregarCarrera():
    cn=Conexion()
    datos=request.get_json()
    return cn.insertar_carrera(datos)

@carreraBP.route('/Carreras',methods=['GET'])
def ConsultaCarreras():
    cn=Conexion()
    return cn.consultarCarreras()

@carreraBP.route("/Carreras", methods=['PUT'])
def modificarCarrera():
    cn = Conexion()
    datos = request.get_json()
    return cn.modificarCarrera(datos)

@carreraBP.route('/Carreras/<string:id>', methods=['DELETE'])
def eliminarCarrera(id):
    cn=Conexion()
    return cn.eliminarCarrera(id)
