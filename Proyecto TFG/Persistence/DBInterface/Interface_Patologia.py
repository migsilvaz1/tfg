from Persistence.DBCon.connection import *
from Persistence.Domain.Patologia import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre, numeroHistorial, id_servicio, id_centro) in cursor:
        result.append(Patologia(id_patologia, nombre, numeroHistorial, id_servicio, id_centro))
    return result


def get_by_id(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Patologia(row[0], row[1], row[2], row[3], row[4])


def create(nombre, paciente, servicio, centro):
    numeroHistorial = paciente.numerohistorial
    id_servicio = servicio.id
    id_centro = centro.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO patologias VALUES(NULL,'%s','%d','%d','%d')" % (nombre, numeroHistorial, id_servicio,
                                                                          id_centro))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(identificator, nombre, numeroHistorial, id_servicio, id_centro):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE patologias SET nombre = '%s', numeroHistorial = '%d', id_servicio = '%d', id_centro = '%d' "
             "WHERE id_patologia = '%d'" % (nombre, numeroHistorial, id_servicio, id_centro, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM patologias WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)