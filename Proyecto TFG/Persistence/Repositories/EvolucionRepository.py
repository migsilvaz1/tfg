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


def get_by_id(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM evoluciones WHERE id_evolucion = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Evolucion(row[0], row[1], row[2])


def create(resultado, notas):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO evoluciones VALUES(NULL,'%s','%s')" % (resultado, notas))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(identificator, nombre, notas):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE evoluciones SET nombre = '%s', notas = '%s' WHERE id_evolucion = '%d'" % (nombre, identificator,
                                                                                               notas))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM evoluciones WHERE id_evolucion = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)
