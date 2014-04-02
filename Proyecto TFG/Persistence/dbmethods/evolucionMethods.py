from Persistence.DBCon.connection import *
from Persistence.Domain.Evolucion import *


def readallevoluciones():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM evoluciones")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_evolucion, resultado, notas) in cursor:
        result.append(Evolucion(id_evolucion, resultado, notas))
    return result


def readevolucionbyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM evoluciones WHERE id_evolucion = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Evolucion(row[0], row[1], row[2])


def createevolucion(resultado, notas):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO evoluciones VALUES(NULL,'%s','%s')" % (resultado, notas))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updateevolucion(identificator, nombre, notas):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE evoluciones SET nombre = '%s', notas = '%s' WHERE id_evolucion = '%d'" % (nombre, identificator,
                                                                                               notas))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleteevolucion(identificator):
    #Quitar del procedimientos esta evolucion
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE procedimientos SET id_evolucion = 0 WHERE id_evolucion = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    #eliminar la evolucion
    query = ("DELETE FROM evoluciones WHERE id_evolucion = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)