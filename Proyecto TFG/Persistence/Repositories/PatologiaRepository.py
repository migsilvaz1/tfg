from Persistence.DBCon.connection import *
from Persistence.Domain.Patologia import *
from Persistence.Domain.Episodio import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre) in cursor:
        result.append(Patologia(id_patologia, nombre))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias WHERE id_patologia = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Patologia(row[0], row[1])


def create(patologia):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO patologias VALUES(NULL,'%s')" % patologia.nombre)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(patologia):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE patologias SET nombre = '%s' WHERE id_patologia = '%d'" % (patologia.nombre, patologia.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(patologia):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM patologias WHERE id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM patologias WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre) in cursor:
        result.append(Patologia(id_patologia, nombre))
    return result


def get_procedimientos(patologia):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios WHERE id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia))
    return result