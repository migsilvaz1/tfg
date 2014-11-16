from Persistence.DBCon.connection import *
from Persistence.Domain.Factor import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM factoresDeRiesgo")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_factor, nombre) in cursor:
        result.append(Factor(id_factor, nombre))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM factoresDeRiesgo WHERE id_factor = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Factor(row[0], row[1])


def create(factor):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO factoresDeRiesgo VALUES(NULL,'%s')" % factor.nombre)
    cursor.execute(query)
    cnx.commit()
    query = ("SELECT @@identity AS id")
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return row[0]


def update(factor):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE factoresDeRiesgo SET nombre = '%s' WHERE id_factor = '%d'" % (factor.nombre, factor.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(factor):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM factoresDeRiesgo WHERE id_factor = '%d'" % factor.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM factoresDeRiesgo WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_factor, nombre) in cursor:
        result.append(Factor(id_factor, nombre))
    return result