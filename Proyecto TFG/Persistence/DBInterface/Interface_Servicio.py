from Persistence.DBCon.connection import *
from Persistence.Domain.Servicio import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM servicios")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_servicio, nombre) in cursor:
        result.append(Servicio(id_servicio, nombre))
    return result


def get_by_id(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM servicios WHERE id_servicio = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Servicio(row[0], row[1])


def create(nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO servicios VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(identificator, nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE servicios SET nombre = '%s' WHERE id_servicio = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM servicios WHERE id_servicio = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)

