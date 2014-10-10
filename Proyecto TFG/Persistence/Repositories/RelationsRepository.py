from Persistence.DBCon.connection import *


#relProcedimietnoMaterial
def create_procedimiento_material(procedimiento, material):
    id_procedimiento = procedimiento.id
    id_material = material.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relProcedimietnoMaterial VALUES('%d','%d')" % (id_procedimiento, id_material))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_procedimiento_mataterial(procedimiento, material):
    id_procedimiento = procedimiento.id
    id_material = material.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relProcedimietnoMaterial WHERE id_procedimiento = '%d' AND id_material = '%d'" % id_procedimiento, id_material)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relPatologiaProcedimiento
def create_patologia_procedimiento(patologia, procedimiento):
    id_patologia = patologia.id
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relPatologiaProcedimiento VALUES('%d','%d')" % (id_patologia, id_procedimiento))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_patologia_procedimiento(patologia, procedimiento):
    id_patologia = patologia.id
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relPatologiaProcedimiento WHERE id_patologia = '%d' AND id_procedimiento = '%d'" % id_patologia, id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relComplicacionProcedimiento
def create_complicacion_procedimiento(complicacion, procedimiento):
    id_complicacion = complicacion.id
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relComplicacionProcedimiento VALUES('%d','%d')" % (id_procedimiento, id_complicacion))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_complicacion_procedimiento(complicacion, procedimiento):
    id_complicacion = complicacion.id
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relComplicacionProcedimiento WHERE id_complicacion = '%d' AND id_procedimiento = '%d'" % id_complicacion, id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relEpisodioPdiagnostica
def create_episodio_pdiagnostica(episodio, pdiagnostica):
    id_episodio = episodio.id
    id_pdiagnostica = pdiagnostica.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relEpisodioPdiagnostica VALUES('%d','%d')" % (id_episodio, id_pdiagnostica))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete_episodio_pdiagnostica(episodio, pdiagnostica):
    id_episodio = episodio.id
    id_pdiagnostica = pdiagnostica.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relEpisodioPdiagnostica WHERE id_episodio = '%d' AND id_pdiagnostica = '%d'" % id_episodio, id_pdiagnostica)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)