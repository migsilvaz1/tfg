from Persistence.DBCon.connection import *
from Persistence.Domain.Servicio import *


def readallservicios():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM servicios")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_servicio, nombre) in cursor:
        result.append(Servicio(id_servicio, nombre))
    return result


def readserviciobyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM servicios WHERE id_servicio = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Servicio(row[0], row[1])


def createservicio(nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO servicios VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updateservicio(identificator, nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE servicios SET nombre = '%s' WHERE id_servicio = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleteservicio(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE patologias SET id_servicio = 0, WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    query = ("DELETE FROM servicios WHERE id_servicio = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)
