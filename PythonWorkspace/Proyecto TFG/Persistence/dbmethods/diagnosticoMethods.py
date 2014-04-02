from Persistence.DBCon.connection import *
from Persistence.Domain.Diagnostico import *


def readalldiagnosticos():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM diagnosticos")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_diagnostico, nombre, id_patologia) in cursor:
        result.append(Diagnostico(id_diagnostico, nombre, id_patologia))
    return result


def readdiagnosticobyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM diagnosticos WHERE id_diagnostico = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Diagnostico(row[0], row[1], row[2])


def creatediagnostico(nombre, patologia):
    id_patologia = patologia.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO diagnosticos VALUES(NULL,'%s','%d')" % (nombre, id_patologia))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updatediagnostico(identificator, nombre, patologia):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE diagnosticos SET nombre = '%s', id_patologia = '%d' WHERE id_diagnostico = '%d'"
             % (nombre, patologia, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deletediagnostico(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM diagnosticos WHERE id_diagnostico = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)
