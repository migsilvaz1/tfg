from Persistence.DBCon.connection import *
from Persistence.Domain.Procedimiento import *
import complicacionMethods
import materialMethods
import relationMethods
import evolucionMethods

def readallprocedimientos():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento, nombre, id_evolucion) in cursor:
        result.append(Procedimiento(id_procedimiento, nombre, id_evolucion))
    return result


def readprocedimientobyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos WHERE id_procedimiento = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Procedimiento(row[0], row[1], row[2])


def createprocedimiento(nombre, evolucion):
    id_evolucion = evolucion.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO procedimientos VALUES(NULL,'%s','%d')" % (nombre, id_evolucion))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updateprocedimiento(identificator, nombre, evolucion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE procedimientos SET nombre = '%s', id_evolucion = '%s' WHERE id_procedimiento = '%d'"
             % (nombre, evolucion, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleteprocedimiento(identificator):
    procedimiento = readprocedimientobyid(identificator)
    #borrar los materiales
    materiales = relationMethods.readallmat_from_prod(identificator)
    for m in materiales:
        materialMethods.deletematerial(m.id)
    #Borrar la evolucion
    evolucionMethods.deleteevolucion(procedimiento.idevolucion)
    #Borrar las complicaciones
    complicaciones = relationMethods.readallcom_from_prod(identificator)
    for c in complicaciones:
        complicacionMethods.deletecomplicacion(c.id)
    #Borrar las relaciones con patologias
    relationMethods.deleterelpatprod_byprod(procedimiento)
    #Borrar el procedimiento
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM procedimientos WHERE id_procedimiento = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)