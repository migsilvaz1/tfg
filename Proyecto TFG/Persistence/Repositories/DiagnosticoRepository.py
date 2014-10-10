from Persistence.DBCon.connection import *
from Persistence.Domain.Diagnostico import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM diagnosticos")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_diagnostico, nombre, id_patologia) in cursor:
        result.append(Diagnostico(id_diagnostico, nombre, id_patologia))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM diagnosticos WHERE id_diagnostico = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Diagnostico(row[0], row[1], row[2])


def create(diagnostico):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO diagnosticos VALUES(NULL,'%s','%d')" % (diagnostico.nombre, diagnostico.idepisodio))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(diagnostico):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE diagnosticos SET nombre = '%s', id_patologia = '%d' WHERE id_diagnostico = '%d'"
             % (diagnostico.nombre, diagnostico.idepisodio, diagnostico.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(diagnostico):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM diagnosticos WHERE id_diagnostico = '%d'" % diagnostico.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM diagnosticos WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_diagnostico, nombre, id_patologia) in cursor:
        result.append(Diagnostico(id_diagnostico, nombre, id_patologia))
    return result