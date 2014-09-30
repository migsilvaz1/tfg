from Persistence.DBCon.connection import *
from Persistence.Domain.Radiologo import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM radiologos")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_radiologo, nombre) in cursor:
        result.append(Radiologo(id_radiologo, nombre))
    return result


def get_by_id(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM radiologos WHERE id_radiologo = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Radiologo(row[0], row[1])


def create(nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO radiologos VALUES(NULL,'%s')" % nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(identificator, nombre):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE radiologos SET nombre = '%s' WHERE id_radiologo = '%d'" % (nombre, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM radiologos WHERE id_radiologo = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)