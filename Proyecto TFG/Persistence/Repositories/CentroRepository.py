from Persistence.DBCon import connection
from Persistence.Domain.Centro import *


def get_all():
    cnx = connection.dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros")
    cursor.execute(query)
    connection.dbdisconect(cnx)
    for (id_centro, nombre) in cursor:
        result.append(Centro(id_centro, nombre))
    return result


def get_by_id(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros WHERE id_centro = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return Centro(row[0], row[1])


def create(nombre):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO centros VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def update(identificator, nombre):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE centros SET nombre = '%s' WHERE id_centro = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def delete(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM centros WHERE id_centro = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)
