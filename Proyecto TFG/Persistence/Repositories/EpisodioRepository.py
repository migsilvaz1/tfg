from Persistence.DBCon.connection import *
from Persistence.Domain.Episodio import *
from Persistence.Domain.PruebaDiagnostica import *
from Persistence.Domain.Diagnostico import *
from Persistence.Domain.Procedimiento import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios WHERE id_episodio = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Episodio(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


def create(episodio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO episodios VALUES(NULL,'%s','%s','%d','%d','%d','%d')" % (episodio.nombre, episodio.fecha,
                                    episodio.idpaciente, episodio.idservicio, episodio.idcentro, episodio.idpatologia))
    cursor.execute(query)
    cnx.commit()
    query = ("SELECT @@identity AS id")
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return row[0]


def update(episodio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE episodios SET nombre = '%s', fecha = '%s', id_paciente = '%d', id_servicio = '%d', id_centro = '%d', id_patologia = '%d' "
             "WHERE id_episodio = '%d'" % (episodio.nombre, episodio.fecha, episodio.idpaciente, episodio.idservicio, episodio.idcentro, episodio.idpatologia, episodio.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(episodio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM episodios WHERE id_episodio = '%d'" % episodio.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_patologia, nombre, id_paciente, id_servicio, id_centro, id_patologia))
    return result


def get_pruebas(episodio):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT pruebasdiagnosticas.id_pdiagnostica, pruebasdiagnosticas.nombre, pruebasdiagnosticas.id_radiologo FROM relepisodiopdiagnostica INNER JOIN pruebasdiagnosticas ON relepisodiopdiagnostica.id_pdiagnostica = pruebasdiagnosticas.id_pdiagnostica WHERE relepisodiopdiagnostica.id_episodio = '%d'" % episodio.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_pdiagnostica, nombre, id_radiologo) in cursor:
        result.append(PruebaDiagnostica(id_pdiagnostica, nombre, id_radiologo))
    return result


def get_diagnosticos(episodio):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM diagnosticos WHERE id_episodio = '%d'" % episodio.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_diagnostico, nombre, id_patologia) in cursor:
        result.append(Diagnostico(id_diagnostico, nombre, id_patologia))
    return result


def get_procedimientos(episodio):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT procedimientos.id_procedimiento, procedimientos.id_tipop, procedimientos.id_evolucion FROM relepisodioprocedimiento INNER JOIN procedimientos ON relepisodioprocedimiento.id_procedimiento = procedimientos.id_procedimiento WHERE relepisodioprocedimiento.id_episodio = '%d'" % episodio.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento, idtipop, id_evolucion) in cursor:
        result.append(Procedimiento(id_procedimiento, idtipop, id_evolucion))
    return result