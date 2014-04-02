from Persistence.DBCon.connection import *
from Persistence.Domain.Complicacion import *
from Persistence.dbmethods.relationMethods import *


def readallcomplicaciones():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM complicaciones")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_complicacion, nombre, mortalidadTemprana, mortalidadTardia) in cursor:
        result.append(Complicacion(id_complicacion, nombre, mortalidadTemprana, mortalidadTardia))
    return result


def readcomplicacionbyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM complicaciones WHERE id_complicacion = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Complicacion(row[0], row[1], row[2], row[3])


def createcomplicacion(nombre, mortalidadTemprana, mortalidadTardia):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO complicaciones VALUES(NULL,'%s','%c','%c')" % (nombre, mortalidadTemprana, mortalidadTardia))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updatecomplicacion(identificator, nombre, mortalidadTemprana, mortalidadTardia):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE complicaciones SET nombre = '%s', mortalidadTemprana = '%c', mortalidadTardia = '%c'"
             " WHERE id_complicacion = '%d'" % (nombre, mortalidadTemprana, mortalidadTardia, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deletecomplicacion(identificator):
    #borrar las relaciones en las que aparece la complicacion
    complicacion = readcomplicacionbyid(identificator)
    deleterelcompro_bycom(complicacion)
    #borrar la complicacion
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM complicaciones WHERE id_complicacion = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)