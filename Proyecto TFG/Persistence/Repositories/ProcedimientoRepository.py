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


def get_by_id(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos WHERE id_procedimiento = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Procedimiento(row[0], row[1], row[2])


def create(nombre, evolucion):
    id_evolucion = evolucion.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO procedimientos VALUES(NULL,'%s','%d')" % (nombre, id_evolucion))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(identificator, nombre, evolucion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE procedimientos SET nombre = '%s', id_evolucion = '%s' WHERE id_procedimiento = '%d'"
             % (nombre, evolucion, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM procedimientos WHERE id_procedimiento = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)