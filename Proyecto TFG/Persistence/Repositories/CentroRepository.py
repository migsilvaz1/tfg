from Persistence.DBCon.connection import *
from Persistence.Domain.Centro import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_centro, nombre) in cursor:
        result.append(Centro(id_centro, nombre))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros WHERE id_centro = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Centro(row[0], row[1])


def create(centro):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO centros VALUES(NULL,'%s')" % centro.nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(centro):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE centros SET nombre = '%s' WHERE id_centro = '%d'" % (centro.nombre, centro.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(centro):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM centros WHERE id_centro = '%d'" % centro.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_centro, nombre) in cursor:
        result.append(Centro(id_centro, nombre))
    return result