from pymongo import MongoClient
from bson import ObjectId

class Conexion():
    def __init__(self):
        self.cliente=MongoClient()
        self.bd=self.cliente.ModuloCarreras
        self.col=self.bd.carreras

    def insertar_carrera(self, carrera):
        respuesta = {"Estatus": "", "Mensaje": ""}
        carrera["estatus"] = "A"
        self.col.insert_one(carrera)
        respuesta["Estatus"] = "OK"
        respuesta["Mensaje"] = "Carrera agregada correctamente"
        return respuesta

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

    def modificarCarrera(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        res = self.bd.carreras.find_one({"_id": data["_id"]})
        if res:
            self.bd.carreras.update_one({"_id": data["_id"]}, {"$set": res})
            resp["estatus:"] = "OK"
            resp["mensaje:"] = "Se actualizo la carrera correctamente"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "La carrera no existe"
        return resp

    def eliminarCarrera(self, id):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.carreras.delete_one({"_id": ObjectId(id), "estatus": "I"})
        if res.delete_count > 0:
            resp["estatus"] = "OK"
            resp["mensaje"] = "La carrera se elimino con exito"
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "La carrera no existe o no se encuentra en estatus de Inactiva"
        return resp
