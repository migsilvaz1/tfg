from Persistence.DBCon.connection import *
from Persistence.dbmethods import procedimientosMethods, materialMethods, patologiaMethods, complicacionMethods



#relProcedimietnoMaterial
def readallproc_from_mat(id_material):
    cnx = dbconnect()
    ids_procedimiento = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT id_procedimiento FROM relProcedimietnoMaterial WHERE id_material = '%d'" % id_material)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento) in cursor:
        ids_procedimiento.append(id_procedimiento)
    results = []
    for (ide) in ids_procedimiento:
        results.append(procedimientosMethods.readprocedimientobyid(ide))
    return results


def readallmat_from_prod(id_procedimiento):
    cnx = dbconnect()
    ids_material = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT id_material FROM relProcedimietnoMaterial WHERE id_procedimiento = '%d'" % id_procedimiento)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_material) in cursor:
        ids_material.append(id_material)
    results = []
    for (ide) in ids_material:
        results.append(materialMethods.readmaterialbyid(ide))
    return results


def createrelprocmat(procedimiento, material):
    id_procedimiento = procedimiento.id
    id_material = material.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relProcedimietnoMaterial VALUES('%d','%d')" % (id_procedimiento, id_material))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleterelprocmat_byproc(procedimiento):
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relProcedimietnoMaterial WHERE id_procedimiento = '%d'" % id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleterelprocmat_bymat(material):
    id_material = material.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relProcedimietnoMaterial WHERE id_material = '%d'" % id_material)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relPatologiaProcedimiento
def readallpat_from_prod(id_procedimiento):
    cnx = dbconnect()
    ids_patologia = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT id_patologia FROM relPatologiaProcedimiento WHERE id_procedimiento = '%d'" % id_procedimiento)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_patologia) in cursor:
        ids_patologia.append(id_patologia)
    results = []
    for (ide) in ids_patologia:
        results.append(patologiaMethods.readpatologiabyid(ide))
    return results


def readallprod_from_pat(id_patologia):
    cnx = dbconnect()
    ids_procedimiento = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT id_procedimiento FROM relPatologiaProcedimiento WHERE id_patologia = '%d'" % id_patologia)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento) in cursor:
        ids_procedimiento.append(id_procedimiento)
    results = []
    for (ide) in ids_procedimiento:
        results.append(procedimientosMethods.readprocedimientobyid(ide))
    return results


def createrelpatprod(patologia, procedimiento):
    id_patologia = patologia.id
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relPatologiaProcedimiento VALUES('%d','%d')" % (id_patologia, id_procedimiento))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleterelpatprod_bypat(patologia):
    id_patologia = patologia.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relPatologiaProcedimiento WHERE id_patologia = '%d'" % id_patologia)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleterelpatprod_byprod(procedimiento):
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relPatologiaProcedimiento WHERE id_procedimiento = '%d'" % id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


#relComplicacionProcedimiento
def readallprod_from_com(id_complicacion):
    cnx = dbconnect()
    ids_procedimiento = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT id_procedimiento FROM relComplicacionProcedimiento WHERE id_complicacion = '%d'" % id_complicacion)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_procedimiento) in cursor:
        ids_procedimiento.append(id_procedimiento)
    results = []
    for (ide) in ids_procedimiento:
        results.append(procedimientosMethods.readprocedimientobyid(ide))
    return results


def readallcom_from_prod(id_procedimiento):
    cnx = dbconnect()
    ids_complicacion = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT id_complicacion FROM relComplicacionProcedimiento WHERE id_procedimiento = '%d'" % id_procedimiento)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_complicacion) in cursor:
        ids_complicacion.append(id_complicacion)
    results = []
    for (ide) in ids_complicacion:
        results.append(complicacionMethods.readcomplicacionbyid(ide))
    return results


def createrelcompro(complicacion, procedimiento):
    id_complicacion = complicacion.id
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO relComplicacionProcedimiento VALUES('%d','%d')" % (id_procedimiento, id_complicacion))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleterelcompro_bycom(complicacion):
    id_complicacion = complicacion.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relComplicacionProcedimiento WHERE id_procedimiento = '%d'" % id_complicacion)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deleterelcompro_byprod(procedimiento):
    id_procedimiento = procedimiento.id
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM relComplicacionProcedimiento WHERE id_procedimiento = '%d'" % id_procedimiento)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)