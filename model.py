from pymongo import MongoClient

class Conexion():
    def __init__(self):
        self.cliente=MongoClient()
        self.bd=self.cliente.ModuloCarreras
        self.col=self.bd.carreras
        self.col2=self.bd.planesEstudio
        self.col3=self.bd.especialidades
        self.col4=self.bd.asignaturas

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

    def consultarCarreraID(self, id):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vCarreras.find_one({"id": id})
        if res:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Carrera encontrada"
            resp["carrera"] = res
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id de la carrera que buscas no existe"
        return resp

    def insertar_carrera(self, carrera):
        respuesta = {"Estatus": "", "Mensaje": ""}
        administrador = self.bd.usuarios.find_one(
            {"tipo": "A", "estatus": "A", "administrativo.estatus": "A"},
            projection={"administrativo": True, "_id": False})
        carrera_existente = self.bd.vCarreras.find_one({"id": carrera["_id"]})
        if not carrera_existente:
            if administrador:
                carrera["estatus"] = "A"
                self.col.insert_one(carrera)
                respuesta["Estatus"] = "OK"
                respuesta["Mensaje"] = "Carrera agregada correctamente"
            else:
                respuesta["Estatus"] = "Error"
                respuesta["Mensaje"] = "El usuario no existe"
        else:
            respuesta["Estatus"] = "Error"
            respuesta["Mensaje"] = "El id de la carrera ya existe en la base de datos, asegurate que sea uno no existente"
        return respuesta

    def modificarCarrera(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        existeid = self.bd.carreras.find_one(
            {"_id": data["_id"]},
            projection={"estatus": True})
        print(existeid)
        if existeid != None:
            if existeid.get("estatus") == "A" or existeid.get("estatus") == "I":
                self.bd.carreras.update_one({"_id": data["_id"]}, {"$set": data})
                print(data)
                resp["estatus:"] = "OK"
                resp["mensaje:"] = "Se actualizo la carrera correctamente"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus de la carrera no se encuentra Activa o Inactiva"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id ingresado de la carrena no existe"
        return resp

    def eliminarCarrera(self, id):
        resp = {"estatus": "", "mensaje": ""}
        existeid = self.bd.carreras.find_one(
            {"_id": id},
            projection={"estatus": True})
        print(existeid)
        if existeid:
            if existeid.get("estatus") == "I":
                res = self.bd.carreras.delete_one({"_id": id})
                if res.deleted_count > 0:
                    resp["estatus"] = "OK"
                    resp["mensaje"] = "La carrera se elimino con exito"
                else:
                    resp["estatus"] = "Error"
                    resp["mensaje"] = "No se pudo eliminar"
            else:
                resp["estatus"] = "Error"
                resp["mensaje"] = "El estatus de la carrera no se encuentra Inactiva, para elimimar la carrera debe encontrarse Inactiva"
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id ingresado de la carrena no existe"
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
            resp["estatus"] = "Error"
            resp["mensaje"] = "No hay Planes De Estudios Registrados"
        return resp

    def consultarPlanEstudioID(self, id):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vPlanesEstudio.find_one({"id": id})
        if res:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Plan de Estudio encontrado"
            resp["carrera"] = res
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id del Plan de Estudio que buscas no existe"
        return resp

    def insertar_planEstudio(self, planesEstudio):
        respuesta = {"Estatus": "", "Mensaje": ""}
        administrador = self.bd.usuarios.find_one(
            {"tipo": "A", "estatus": "A", "administrativo.estatus": "A"},
            projection={"administrativo": True, "_id": False})
        pestudio_existente = self.bd.vPlanesEstudio.find_one({"id": planesEstudio["_id"]})
        if administrador:
            if not pestudio_existente:
                planesEstudio["estatus"] = "A"
                self.col2.insert_one(planesEstudio)
                respuesta["Estatus"] = "OK"
                respuesta["Mensaje"] = "Plan de Estudio agregado correctamente"
            else:
                respuesta["Estatus"] = "Error"
                respuesta[
                    "Mensaje"] = "El id del Plan de Estudio ya existe en la base de datos, asegurate que sea uno no existente"
        else:
            respuesta["Estatus"] = "Error"
            respuesta["Mensaje"] = "El usuario no existe"
        return respuesta

    def modificarPlanesEstudio(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        existeid = self.bd.planesEstudio.find_one(
            {"_id": data["_id"]},
            projection={"estatus": True})
        print(existeid)
        if existeid != None:
            if existeid.get("estatus") == "A" or existeid.get("estatus") == "I":
                self.bd.planesEstudio.update_one({"_id": data["_id"]}, {"$set": data})
                print(data)
                resp["estatus:"] = "OK"
                resp["mensaje:"] = "Se actualizo el Plan de Estudio correctamente"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus del Plan Estudio no se encuentra Activa o Inactiva"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id ingresado del Plan de Estudio no existe"
        return resp

    def eliminarPlanEstudio(self, id):
        resp = {"estatus": "", "mensaje": ""}
        existeid = self.bd.planesEstudio.find_one(
            {"_id": id},
            projection={"estatus": True})
        print(existeid)
        if existeid:
            if existeid.get("estatus") == "I":
                res = self.bd.planesEstudio.delete_one({"_id": id})
                if res.deleted_count > 0:
                    resp["estatus"] = "OK"
                    resp["mensaje"] = "El Plan de Estudio se elimino con exito"
                else:
                    resp["estatus"] = "Error"
                    resp["mensaje"] = "No se pudo eliminar"
            else:
                resp["estatus"] = "Error"
                resp[
                    "mensaje"] = "El estatus del Plan de Estudio no se encuentra Inactiva, para elimimar el Plan de Estudio debe encontrarse Inactiva"
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id ingresado del Plan de Estudio no existe"
        return resp



    # FUNCIONES DEL MODULO ESPECIALIDADES
    def consultarEspecialidades(self):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vEspecialidades.find({})
        lista = []
        for s in res:
            lista.append(s)
        if len(lista) > 0:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Lista de Especialidades"
            resp["carreras"] = lista
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "No hay Especialidades registradas"
        return resp

    def consultarEspecialidadesID(self, id):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vEspecialidades.find_one({"id": id})
        if res:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Especialidad encontrada"
            resp["carrera"] = res
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id de la especialidad que buscas no existe"
        return resp

    def insertar_especialidad(self, especialidad):
        respuesta = {"Estatus": "", "Mensaje": ""}
        administrador = self.bd.usuarios.find_one(
            {"tipo": "A", "estatus": "A", "administrativo.estatus": "A"},
            projection={"administrativo": True, "_id": False})
        especialidad_existente = self.bd.vEspecialidades.find_one({"id": especialidad["_id"]})
        if administrador:
            if not especialidad_existente:
                especialidad["estatus"] = "A"
                self.col3.insert_one(especialidad)
                respuesta["Estatus"] = "OK"
                respuesta["Mensaje"] = "Especialidad agregada correctamente"
            else:
                respuesta["Estatus"] = "Error"
                respuesta["Mensaje"] = "El id de la especialidad ya existe en la base de datos, asegurate que sea uno no existente"
        else:
            respuesta["Estatus"] = "Error"
            respuesta["Mensaje"] = "El usuario no existe"
        return respuesta

    def modificarEspecialidad(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        existeid = self.bd.especialidades.find_one(
            {"_id": data["_id"]},
            projection={"estatus": True})
        print(existeid)
        if existeid != None:
            if existeid.get("estatus") == "A" or existeid.get("estatus") == "I":
                self.bd.especialidades.update_one({"_id": data["_id"]}, {"$set": data})
                print(data)
                resp["estatus:"] = "OK"
                resp["mensaje:"] = "Se actualizo la especialidad correctamente"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus de la especialidad no se encuentra Activa o Inactiva"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id ingresado de la especialidad no existe"
        return resp

    def eliminarEspecialidad(self, id):
        resp = {"estatus": "", "mensaje": ""}
        existeid = self.bd.especialidades.find_one(
            {"_id": id},
            projection={"estatus": True})
        print(existeid)
        if existeid:
            if existeid.get("estatus") == "I":
                res = self.bd.especialidades.delete_one({"_id": id})
                if res.deleted_count > 0:
                    resp["estatus"] = "OK"
                    resp["mensaje"] = "La especialidad se elimino con exito"
                else:
                    resp["estatus"] = "Error"
                    resp["mensaje"] = "No se pudo eliminar"
            else:
                resp["estatus"] = "Error"
                resp["mensaje"] = "El estatus de la especialidad no se encuentra Inactiva, para elimimar la carrera debe encontrarse Inactiva"
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id ingresado de la especialidad no existe"
        return resp

    # FUNCIONES DEL MODULO ASIGNATURAS
    def consultarAsignaturas(self):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vAsignaturas.find({})
        lista = []
        for s in res:
            lista.append(s)
        if len(lista) > 0:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Lista de Asignaturas"
            resp["carreras"] = lista
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "No hay Asigntauras registradas"
        return resp

    def consultarAsignaturaID(self, id):
        resp = {"estatus": "", "mensaje": ""}
        res = self.bd.vAsignaturas.find_one({"id": id})
        if res:
            resp["estatus"] = "OK"
            resp["mensaje"] = "Asignatura encontrada"
            resp["carrera"] = res
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id de la asignatura que buscas no existe"
        return resp

    def insertar_asignatura(self, asignatura):
        respuesta = {"Estatus": "", "Mensaje": ""}
        administrador = self.bd.usuarios.find_one(
            {"tipo": "A", "estatus": "A", "administrativo.estatus": "A"},
            projection={"administrativo": True, "_id": False})
        asignatura_existente = self.bd.vAsignaturas.find_one({"id": asignatura["_id"]})
        if administrador:
            if not asignatura_existente:
                asignatura["estatus"] = "A"
                self.col4.insert_one(asignatura)
                respuesta["Estatus"] = "OK"
                respuesta["Mensaje"] = "Asignatura agregada correctamente"
            else:
                respuesta["Estatus"] = "Error"
                respuesta[
                    "Mensaje"] = "El id de la asignatura ya existe en la base de datos, asegurate que sea uno no existente"
        else:
            respuesta["Estatus"] = "Error"
            respuesta["Mensaje"] = "El usuario no existe"
        return respuesta

    def modificarAsignatura(self, data):
        resp = {"estatus:": "", "mensaje:": ""}
        existeid = self.bd.asignaturas.find_one(
            {"_id": data["_id"]},
            projection={"estatus": True})
        print(existeid)
        if existeid != None:
            if existeid.get("estatus") == "A" or existeid.get("estatus") == "I":
                self.bd.asignaturas.update_one({"_id": data["_id"]}, {"$set": data})
                print(data)
                resp["estatus:"] = "OK"
                resp["mensaje:"] = "Se actualizo la asignatura correctamente"
            else:
                resp["estatus:"] = "Error"
                resp["mensaje:"] = "El estatus de la asignatura no se encuentra Activa o Inactiva"
        else:
            resp["estatus:"] = "Error"
            resp["mensaje:"] = "El id ingresado de la asignatura no existe"
        return resp

    def eliminarAsignatura(self, id):
        resp = {"estatus": "", "mensaje": ""}
        existeid = self.bd.asignaturas.find_one(
            {"_id": id},
            projection={"estatus": True})
        print(existeid)
        if existeid:
            if existeid.get("estatus") == "I":
                res = self.bd.asignaturas.delete_one({"_id": id})
                if res.deleted_count > 0:
                    resp["estatus"] = "OK"
                    resp["mensaje"] = "La asignatura se elimino con exito"
                else:
                    resp["estatus"] = "Error"
                    resp["mensaje"] = "No se pudo eliminar"
            else:
                resp["estatus"] = "Error"
                resp[
                    "mensaje"] = "El estatus de la asignatura no se encuentra Inactiva, para elimimar la asignatura debe encontrarse Inactiva"
        else:
            resp["estatus"] = "Error"
            resp["mensaje"] = "El id ingresado de la asignatura no existe"
        return resp

    #FUNCIONES APARTE
    def validarCredenciales(self, usuario, password):
        user = self.bd.usuarios.find_one({"email": usuario, "password": password, "estatus": "A"})
        if user:
            return user
        else:
            return None