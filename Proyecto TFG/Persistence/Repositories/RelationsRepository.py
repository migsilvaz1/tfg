from Persistence.DBCon.connection import *


#relProcedimietnoMaterial
def create_procedimiento_material(id_procedimiento, id_material):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relProcedimietnoMaterial VALUES('%d','%d')" % (id_procedimiento, id_material))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_procedimiento_mataterial(id_procedimiento, id_material):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relProcedimietnoMaterial WHERE id_procedimiento = '%d' AND id_material = '%d'" % id_procedimiento, id_material)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relEpisodioProcedimiento
def create_episodio_procedimiento(id_episodio, id_procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relEpisodioProcedimiento VALUES('%d','%d')" % (id_episodio, id_procedimiento))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_episodio_procedimiento(id_episodio, id_procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relEpisodioProcedimiento WHERE id_episodio = '%d' AND id_procedimiento = '%d'" % id_episodio, id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relComplicacionProcedimiento
def create_complicacion_procedimiento(id_complicacion, id_procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relComplicacionProcedimiento VALUES('%d','%d')" % (id_procedimiento, id_complicacion))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_complicacion_procedimiento(id_complicacion, id_procedimiento):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relComplicacionProcedimiento WHERE id_complicacion = '%d' AND id_procedimiento = '%d'" % id_complicacion, id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relEpisodioPdiagnostica
def create_episodio_pdiagnostica(id_episodio, id_pdiagnostica):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relEpisodioPdiagnostica VALUES('%d','%d')" % (id_episodio, id_pdiagnostica))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_episodio_pdiagnostica(id_episodio, id_pdiagnostica):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relEpisodioPdiagnostica WHERE id_episodio = '%d' AND id_pdiagnostica = '%d'" % id_episodio, id_pdiagnostica)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)