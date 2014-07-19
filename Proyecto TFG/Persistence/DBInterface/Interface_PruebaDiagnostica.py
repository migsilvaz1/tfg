from Persistence.DBCon.connection import *
from Persistence.Domain.PruebaDiagnostica import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pruebasDiagnosticas")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_pdiagnostica, nombre, id_patologia, id_radiologo) in cursor:
        result.append(PruebaDiagnostica(id_pdiagnostica, nombre, id_patologia, id_radiologo))
    return result


def get_by_id(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pruebasDiagnosticas WHERE id_pdiagnostica = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return PruebaDiagnostica(row[0], row[1], row[2], row[3])


def create(nombre, patologia, radiologo):
    id_patologia = patologia.id
    id_radiologo = radiologo.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO pruebasDiagnosticas VALUES(NULL,'%s','%d','%d')" % (nombre, id_patologia, id_radiologo))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(identificator, nombre, patologia, radiologo):
    id_patologia = patologia.id
    id_radiologo = radiologo.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE pruebasDiagnosticas SET nombre = '%s', id_patologia = '%d', id_radiologo = '%d' "
             "WHERE id_pdiagnostica = '%d'" % (nombre, id_patologia, id_radiologo, identificator))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM pruebasDiagnosticas WHERE id_pdiagnostica = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)

