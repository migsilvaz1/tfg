from Persistence.DBCon.connection import *
from Persistence.Domain.TipoProcedimiento import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM tipo_procedimiento")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_tipop, nombre) in cursor:
        result.append(TipoProcedimiento(id_tipop, nombre))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM tipo_procedimiento WHERE id_tipop = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return TipoProcedimiento(row[0], row[1])


def create(tipop):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO tipo_procedimiento VALUES(NULL,'%s')" % tipop.nombre)
    cursor.execute(query)
    cnx.commit()
    query = ("SELECT @@identity AS id")
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return row[0]


def update(tipop):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE tipo_procedimiento SET nombre = '%s' WHERE id_tipop = '%d'" % (tipop.nombre, tipop.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(tipop):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM tipo_procedimiento WHERE id_tipop = '%d'" % tipop.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM tipo_procedimiento WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_centro, nombre) in cursor:
        result.append(TipoProcedimiento(id_centro, nombre))
    return result
