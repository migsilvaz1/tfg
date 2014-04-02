from Persistence.DBCon import connection
from Persistence.Domain.Centro import *


def readallcentros():
    cnx = connection.dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros")
    cursor.execute(query)
    connection.dbdisconect(cnx)
    for (id_centro, nombre) in cursor:
        result.append(Centro(id_centro, nombre))
    return result


def readcentrobyid(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM centros WHERE id_centro = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return Centro(row[0], row[1])


def createcentro(nombre):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO centros VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def updatecentro(identificator, nombre):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE centros SET nombre = '%s' WHERE id_centro = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def deletecentro(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE patologias SET id_centro = 0, WHERE id_centro = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    query = ("DELETE FROM centros WHERE id_centro = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)