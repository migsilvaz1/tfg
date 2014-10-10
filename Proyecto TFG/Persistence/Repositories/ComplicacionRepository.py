from Persistence.DBCon.connection import *
from Persistence.Domain.Complicacion import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM complicaciones")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_complicacion, nombre, mortalidadTemprana, mortalidadTardia) in cursor:
        result.append(Complicacion(id_complicacion, nombre, mortalidadTemprana, mortalidadTardia))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM complicaciones WHERE id_complicacion = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Complicacion(row[0], row[1], row[2], row[3])


def create(complicacion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO complicaciones VALUES(NULL,'%s','%c','%c')" % (complicacion.nombre,
                                                                         complicacion.mortalidadTemprana,
                                                                         complicacion.mortalidadTardia))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(complicacion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE complicaciones SET nombre = '%s', mortalidadTemprana = '%c', mortalidadTardia = '%c'"
             " WHERE id_complicacion = '%d'" % (complicacion.nombre, complicacion.mortalidadTemprana,
                                                complicacion.mortalidadTardia, complicacion.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(complicacion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM complicaciones WHERE id_complicacion = '%d'" % complicacion.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM complicaciones WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_complicacion, nombre, mortalidadTemprana, mortalidadTardia) in cursor:
        result.append(Complicacion(id_complicacion, nombre, mortalidadTemprana, mortalidadTardia))
    return result