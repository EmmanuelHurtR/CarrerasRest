from pymongo import MongoClient
from bson import ObjectId

class Conexion():
    def __init__(self):
        self.cliente=MongoClient()
        self.bd=self.cliente.ModuloCarreras
        self.col=self.bd.carreras
        self.col2=self.bd.planesEstudio

    #FUNCIONES DEL MODULO CARRERAS

    def consultarCarreras(self):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vCarreras.find({})
        lista = []
        for s in res:
            lista.append(s)
        if len(lista) > 0:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Lista de Carreras"
            resp["carreras"] = lista
        else:
            resp["estatus"] = "OK"
            resp["mensaje"] = "No hay carreras registradas"
        return resp

    def insertar_carrera(self, carrera):
        respuesta = {"Estatus": "", "Mensaje": ""}
        carrera["estatus"] = "A"
        self.col.insert_one(carrera)
        respuesta["Estatus"] = "OK"
        respuesta["Mensaje"] = "Carrera agregada correctamente"
        return respuesta

    def modificarCarrera(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        res = self.bd.carreras.find_one({"_id": data["_id"]})
        print(res)
        if res:
            self.bd.carreras.update_one({"_id": data["_id"]}, {"$set": data})
            resp["estatus:"] = "OK"
            resp["mensaje:"] = "Se actualizo la carrera correctamente"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "La carrera no existe"
        return resp

    def eliminarCarrera(self, id):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.carreras.delete_one({"_id": id})
        print(res)
        if res.deleted_count > 0:
            resp["estatus"] = "OK"
            resp["mensaje"] = "La carrera se elimino con exito"
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "La carrera no existe o no se encuentra en estatus de Inactiva"
        return resp



    # FUNCIONES DEL MODULO PLANES DE ESTUDIO
    def insertar_planEstudio(self, planesEstudio):
        respuesta = {"Estatus": "", "Mensaje": ""}
        planesEstudio["estatus"] = "A"
        self.col2.insert_one(planesEstudio)
        respuesta["Estatus"] = "OK"
        respuesta["Mensaje"] = "Plan de Estudio agregado correctamente"
        return respuesta

    def consultarPlanesEstudio(self):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vPlanesEstudio.find({})
        lista = []
        for s in res:
            lista.append(s)
        if len(lista) > 0:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Lista de Planes De Estudio"
            resp["carreras"] = lista
        else:
            resp["estatus"] = "OK"
            resp["mensaje"] = "No hay Planes De Estudio Registrados"
        return resp



    # FUNCIONES DEL MODULO ESPECIALIDADES



    # FUNCIONES DEL MODULO ASIGNATURAS


    #FUNCIONES APARTE
    def validarCredenciales(self, usuario, password):
        user = self.bd.usuarios.find_one({"email": usuario, "password": password, "estatus": "A"})
        if user:
            return user
        else:
            return None