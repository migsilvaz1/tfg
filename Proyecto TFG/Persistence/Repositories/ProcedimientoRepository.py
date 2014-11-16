from Persistence.DBCon.connection import *
from Persistence.Domain.Procedimiento import *
from Persistence.Domain.Material import *
from Persistence.Domain.Complicacion import *
from Persistence.Domain.Episodio import *


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos")
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento, idtipop, id_evolucion) in cursor:
        result.append(Procedimiento(id_procedimiento, idtipop, id_evolucion))
    return result


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos WHERE id_procedimiento = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Procedimiento(row[0], row[1], row[2])


def create(procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO procedimientos VALUES(NULL,'%d','%d')" % (procedimiento.idtipop, procedimiento.idevolucion))
    cursor.execute(query)
    cnx.commit()
    query = ("SELECT @@identity AS id")
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return row[0]


def update(procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE procedimientos SET id_tipop = '%d', id_evolucion = '%s' WHERE id_procedimiento = '%d'"
             % (procedimiento.idtipop, procedimiento.idevolucion, procedimiento.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM procedimientos WHERE id_procedimiento = '%d'" % procedimiento.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM procedimientos WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento, idtipop, id_evolucion) in cursor:
        result.append(Procedimiento(id_procedimiento, idtipop, id_evolucion))
    return result


def get_imagenes(procedimiento):
    return


def get_documentos(procedimiento):
    return


def get_materiales(procedimiento):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT materiales.id_material, materiales.nombre FROM relprocedimientomaterial INNER JOIN materiales ON relprocedimientomaterial.id_material = materiales.id_material WHERE relprocedimientomaterial.id_procedimiento = '%d'" % procedimiento.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_material, nombre) in cursor:
        result.append(Material(id_material, nombre))
    return result


def get_complicaciones(procedimiento):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT complicaciones.id_complicacion, complicaciones.nombre, complicaciones.mortalidadTemprana, complicaciones.mortalidadTardia FROM relcomplicacionprocedimiento INNER JOIN complicaciones ON relcomplicacionprocedimiento.id_complicacion = complicaciones.id_complicacion WHERE relcomplicacionprocedimiento.id_procedimiento = '%d'" % procedimiento.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_complicacion, nombre, mortalidadtemprana, mortalidadtardia) in cursor:
        result.append(Complicacion(id_complicacion, nombre, mortalidadtemprana, mortalidadtardia))
    return result


def get_episodios(procedimiento):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT episodios.id_episodio, episodios.nombre, episodios.fecha, episodios.id_paciente, episodios.id_servicio, episodios.id_centro, episodios.id_patologia FROM relepisodioprocedimiento INNER JOIN episodios ON relepisodioprocedimiento.id_episodio = episodios.id_episodio WHERE relepisodioprocedimiento.id_procedimiento = '%d'" % procedimiento.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia))
    return result