from Persistence.DBCon.connection import *
from Persistence.Domain.Material import *
from Persistence.dbmethods.relationMethods import *


def readallmateriales():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM materiales")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_material, nombre) in cursor:
        result.append(Material(id_material, nombre))
    return result


def readmaterialbyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM materiales WHERE id_material = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Material(row[0], row[1])


def creatematerial(nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO materiales VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updatematerial(identificator, nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE materiales SET nombre = '%s' WHERE id_material = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deletematerial(identificator):
    #borrar las relaciones en las que aparece el material
    material = readmaterialbyid(identificator)
    deleterelprocmat_bymat(material)
    #borrar el material
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM materiales WHERE id_material = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)