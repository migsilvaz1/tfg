from Persistence.DBCon.connection import *
from Persistence.Domain.PruebaDiagnostica import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pruebasDiagnosticas")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_pdiagnostica, nombre, id_radiologo) in cursor:
        result.append(PruebaDiagnostica(id_pdiagnostica, nombre, id_radiologo))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pruebasDiagnosticas WHERE id_pdiagnostica = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return PruebaDiagnostica(row[0], row[1], row[2])


def create(prueba):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO pruebasDiagnosticas VALUES(NULL,'%s','%d')" % (prueba.nombre, prueba.idradiologo))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(prueba):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE pruebasDiagnosticas SET nombre = '%s', id_radiologo = '%d' WHERE id_pdiagnostica = '%d'"
             % (prueba.nombre, prueba.idradiologo, prueba.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(prueba):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM pruebasDiagnosticas WHERE id_pdiagnostica = '%d'" % prueba.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pruebasDiagnosticas WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_pdiagnostica, nombre, id_radiologo) in cursor:
        result.append(PruebaDiagnostica(id_pdiagnostica, nombre, id_radiologo))
    return result