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


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM servicios WHERE id_servicio = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Servicio(row[0], row[1])


def create(servicio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO servicios VALUES(NULL,'%s')" % servicio.nombre)
    cursor.execute(query)
    cnx.commit()
    query = ("SELECT @@identity AS id")
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return row[0]


def update(servicio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE servicios SET nombre = '%s' WHERE id_servicio = '%d'" % (servicio.nombre, servicio.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(servicio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM servicios WHERE id_servicio = '%d'" % servicio.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM servicios WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_servicio, nombre) in cursor:
        result.append(Servicio(id_servicio, nombre))
    return result