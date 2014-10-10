from Persistence.DBCon.connection import *
from Persistence.Domain.Episodio import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_patologia, nombre, id_paciente, id_servicio, id_centro, id_patologia))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios WHERE id_episodio = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Episodio(row[0], row[1], row[2], row[3], row[4], row[5])


def create(episodio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO episodios VALUES(NULL,'%s','%d','%d','%d','%d')" % (episodio.nombre, episodio.idpaciente
                                                                               , episodio.idservicio,
                                                                               episodio.idcentro, episodio.idpatologia))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(episodio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE episodios SET nombre = '%s', id_paciente = '%d', id_servicio = '%d', id_centro = '%d', id_patologia = '%d' "
             "WHERE id_episodio = '%d'" % (episodio.nombre, episodio.idpaciente, episodio.idservicio, episodio.idcentro, episodio.idpatologia, episodio.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(episodio):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM episodios WHERE id_episodio = '%d'" % episodio.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia, nombre, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_patologia, nombre, id_paciente, id_servicio, id_centro, id_patologia))
    return result