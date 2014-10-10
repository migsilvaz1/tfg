from Persistence.DBCon.connection import *
from Persistence.Domain.Procedimiento import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento, nombre, id_evolucion) in cursor:
        result.append(Procedimiento(id_procedimiento, nombre, id_evolucion))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos WHERE id_procedimiento = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Procedimiento(row[0], row[1], row[2])


def create(procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO procedimientos VALUES(NULL,'%s','%d')" % (procedimiento.nombre, procedimiento.idevolucion))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE procedimientos SET nombre = '%s', id_evolucion = '%s' WHERE id_procedimiento = '%d'"
             % (procedimiento.nombre, procedimiento.idevolucion, procedimiento.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM procedimientos WHERE id_procedimiento = '%d'" % procedimiento.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento, nombre, id_evolucion) in cursor:
        result.append(Procedimiento(id_procedimiento, nombre, id_evolucion))
    return result