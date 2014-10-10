from Persistence.DBCon.connection import *
from Persistence.Domain.Evolucion import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM evoluciones")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_evolucion, resultado, notas) in cursor:
        result.append(Evolucion(id_evolucion, resultado, notas))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM evoluciones WHERE id_evolucion = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Evolucion(row[0], row[1], row[2])


def create(evolucion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO evoluciones VALUES(NULL,'%s','%s')" % (evolucion.resultado, evolucion.notas))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(evolucion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE evoluciones SET nombre = '%s', notas = '%s' WHERE id_evolucion = '%d'" % (evolucion.nombre,
                                                                                               evolucion.notas, evolucion.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(evolucion):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM evoluciones WHERE id_evolucion = '%d'" % evolucion.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM evoluciones WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_evolucion, resultado, notas) in cursor:
        result.append(Evolucion(id_evolucion, resultado, notas))
    return result