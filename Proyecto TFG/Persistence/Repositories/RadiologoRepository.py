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


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM radiologos WHERE id_radiologo = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Radiologo(row[0], row[1])


def create(radiologo):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO radiologos VALUES(NULL,'%s')" % radiologo.nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(radiologo):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE radiologos SET nombre = '%s' WHERE id_radiologo = '%d'" % (radiologo.nombre, radiologo.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(radiologo):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM radiologos WHERE id_radiologo = '%d'" % radiologo.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM radiologos WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_radiologo, nombre) in cursor:
        result.append(Radiologo(id_radiologo, nombre))
    return result