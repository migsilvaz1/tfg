from Persistence.DBCon.connection import *
from Persistence.Domain.Patologia import *
from Persistence.dbmethods.relationMethods import *
from Persistence.dbmethods.procedimientosMethods import *


def readallpatologias():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre, numeroHistorial, id_servicio, id_centro) in cursor:
        result.append(Patologia(id_patologia, nombre, numeroHistorial, id_servicio, id_centro))
    return result


def readpatologiabyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Patologia(row[0], row[1], row[2], row[3], row[4])


def createpatologia(nombre, paciente, servicio, centro):
    numeroHistorial = paciente.numerohistorial
    id_servicio = servicio.id
    id_centro = centro.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO patologias VALUES(NULL,'%s','%d','%d','%d')" % (nombre, numeroHistorial, id_servicio,
                                                                          id_centro))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updatepatologia(identificator, nombre, numeroHistorial, id_servicio, id_centro):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE patologias SET nombre = '%s', numeroHistorial = '%d', id_servicio = '%d', id_centro = '%d' "
             "WHERE id_patologia = '%d'" % (nombre, numeroHistorial, id_servicio, id_centro, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deletepatologia(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    #Borrar todos los diagnosticos asociados
    query = ("DELETE FROM diagnosticos WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    #borrar todas las pruebas diagnosticas asociadas
    query = ("DELETE FROM pruebasDiagnosticas WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    #borrar todas los procedimientos asociados
    procedimientos = readallprod_from_pat(identificator)
    patologia = readpatologiabyid(identificator)
    deleterelpatprod_bypat(patologia)
    for p in procedimientos:
        procedimientosMethods.deleteprocedimiento(p.id)

    #borrar la patologia
    query = ("DELETE FROM patologias WHERE id_patologia = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)