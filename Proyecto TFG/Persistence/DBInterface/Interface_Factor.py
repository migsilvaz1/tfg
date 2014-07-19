from Persistence.DBCon import connection
from Persistence.Domain.Factor import *


def get_all():
    cnx = connection.dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM factoresDeRiesgo")
    cursor.execute(query)
    connection.dbdisconect(cnx)
    for (id_factor, nombre) in cursor:
        result.append(Factor(id_factor, nombre))
    return result


def get_by_id(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM factoresDeRiesgo WHERE id_factor = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return Factor(row[0], row[1])


def create(nombre):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO factoresDeRiesgo VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def update(identificator, nombre):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE factoresDeRiesgo SET nombre = '%s' WHERE id_factor = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def delete(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM factoresDeRiesgo WHERE id_factor = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)

