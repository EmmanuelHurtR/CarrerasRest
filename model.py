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

    def consultarCarreraSiglas(self, siglas):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vCarreras.find_one({"siglas": siglas})
        if res:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Carrera encontrada"
            resp["carrera"] = res
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "No hay carreras registradas con esas siglas"
        return resp

    def insertar_carrera(self, carrera):
        respuesta = {"Estatus": "", "Mensaje": ""}
        administrador = self.bd.usuarios.find_one(
            {"tipo": "A", "estatus": "A", "administrativo.estatus": "A"},
            projection={"administrativo": True, "_id": False})
        if administrador:
            carrera["estatus"] = "A"
            self.col.insert_one(carrera)
            respuesta["Estatus"] = "OK"
            respuesta["Mensaje"] = "Carrera agregada correctamente"
        else:
            respuesta["Estatus"] = "Error"
            respuesta["Mensaje"] = "El usuario no existe"
        return respuesta

    def modificarCarrera(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        estatus = self.bd.carreras.find_one(
            {"_id": data["_id"]},
            projection={"estatus": True})
        print(estatus)
        if estatus != None:
            if estatus.get("estatus") == "A":
                res = self.bd.carreras.find_one({"_id": data["_id"]})
                print(res)
                if res:
                    self.bd.carreras.update_one({"_id": data["_id"]}, {"$set": data})
                    print(data)
                    resp["estatus:"] = "OK"
                    resp["mensaje:"] = "Se actualizo la carrera correctamente"
                else:
                    resp["estatus:"] = "Error"
                    resp["mensaje:"] = "La carrera esta Inactiva"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus de la carrera no se encuentra Activa"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id de la carrera no existe"
        return resp

    def eliminarCarrera(self, id):
        resp = {"estatus": "", "mensaje": ""}
        estatus = self.bd.carreras.find_one(
            {"_id": id},
            projection={"estatus": True})
        print(estatus)
        if estatus != None:
            if estatus.get("estatus") == "I":
                res = self.bd.carreras.delete_one({"_id": id})
                if res.deleted_count > 0:
                    resp["estatus"] = "OK"
                    resp["mensaje"] = "La carrera se elimino con exito"
                else:
                    resp["estatus"] = "Error"
                    resp["mensaje"] = "No se pudo eliminar"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus de la carrera no se encuentra Inactiva"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id de la carrera no existe"
        return resp



    # FUNCIONES DEL MODULO PLANES DE ESTUDIO
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

    def insertar_planEstudio(self, planesEstudio):
        respuesta = {"Estatus": "", "Mensaje": ""}
        administrador = self.bd.usuarios.find_one(
            {"tipo": "A", "estatus": "A", "administrativo.estatus": "A"},
            projection={"administrativo": True, "_id": False})
        print(administrador)
        print(planesEstudio)
        if administrador:
            planesEstudio["estatus"] = "A"
            self.col2.insert_one(planesEstudio)
            respuesta["Estatus"] = "OK"
            respuesta["Mensaje"] = "Plan de Estudio agregado correctamente"
        else:
            respuesta["Estatus"] = "Error"
            respuesta["Mensaje"] = "El usuario no existe"
        return respuesta

    def modificarPlanesEstudio(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        estatus = self.bd.planesEstudio.find_one(
            {"_id": data["_id"]},
            projection={"estatus": True})
        print(estatus)
        if estatus != None:
            if estatus.get("estatus") == "A":
                res = self.bd.planesEstudio.find_one({"_id": data["_id"]})
                print(res)
                if res:
                    self.bd.planesEstudio.update_one({"_id": data["_id"]}, {"$set": data})
                    print(data)
                    resp["estatus:"] = "OK"
                    resp["mensaje:"] = "Se actualizo el plan correctamente"
                else:
                    resp["estatus:"] = "Error"
                    resp["mensaje:"] = "El plam esta Inactiva"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus del plan no se encuentra Activa"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id del plan no existe"
        return resp

    def eliminarPlanEstudio(self, id):
        resp = {"estatus": "", "mensaje": ""}
        estatus = self.bd.planesEstudio.find_one(
            {"_id": id},
            projection={"estatus": True})
        print(estatus)
        if estatus != None:
            if estatus.get("estatus") == "I":
                res = self.bd.planesEstudio.delete_one({"_id": id})
                if res.deleted_count > 0:
                    resp["estatus"] = "OK"
                    resp["mensaje"] = "el plan se elimino con exito"
                else:
                    resp["estatus"] = "Error"
                    resp["mensaje"] = "No se ha podido eliminar"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus del plan de estudios no se encuentra Inactiva"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id del plan de estudios no existe"
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