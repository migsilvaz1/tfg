from Persistence.DBCon.connection import *
from Persistence.Domain.Material import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM materiales")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_material, nombre) in cursor:
        result.append(Material(id_material, nombre))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM materiales WHERE id_material = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Material(row[0], row[1])


def create(material):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO materiales VALUES(NULL,'%s')" % material.nombre)
    cursor.execute(query)
    cnx.commit()
    query = ("SELECT @@identity AS id")
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return row[0]


def update(material):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE materiales SET nombre = '%s' WHERE id_material = '%d'" % (material.nombre, material.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(material):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM materiales WHERE id_material = '%d'" % material.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM materiales WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_material, nombre) in cursor:
        result.append(Material(id_material, nombre))
    return result