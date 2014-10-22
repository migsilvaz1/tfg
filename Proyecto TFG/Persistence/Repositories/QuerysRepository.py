from Persistence.DBCon import connection


#QUE PORCENTAJE DE UNA PATOLOGIA A HA PRESENTADO COMPLICACIONES?
def porcentaje_complicaciones_patologia(patologia):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    #Calculamos primero el numero de procedimientos de una patologia
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN relepisodioprocedimiento on episodios.id_episodio = relepisodioprocedimiento.id_episodio "
             "INNER JOIN procedimientos ON relepisodioprocedimiento.id_procedimiento = procedimientos.id_procedimiento "
             "WHERE patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    total_procedimientos = row[0]
    #Numero de procediciemntos con complicaciones de una patologia
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN relepisodioprocedimiento on episodios.id_episodio = relepisodioprocedimiento.id_episodio "
             "INNER JOIN procedimientos ON relepisodioprocedimiento.id_procedimiento = procedimientos.id_procedimiento "
             "INNER JOIN relcomplicacionprocedimiento ON procedimientos.id_procedimiento = "
             "relcomplicacionprocedimiento.id_procedimiento WHERE patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    complicaciones_procedimientos = row[0]
    connection.dbdisconect(cnx)
    res = (complicaciones_procedimientos * 1.0)/(total_procedimientos * 1.0)*100
    return res


#QUE PORCENTAJE/ NUM DE PACIENTES CON UNA PATOLOGIA A PRESENTABAN FACTORES DE RIESGO?
def pacientes_factores_patologia(patologia):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    #Total de pacientes con una patologia
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN pacientes ON episodios.id_paciente = pacientes.id_paciente WHERE "
             "patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    total_pacientes = row[0]
    #Numero de pacientes con factores de riesgo de una patologia
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN pacientes ON episodios.id_paciente = pacientes.id_paciente INNER JOIN "
             "relpacientefactor ON pacientes.id_paciente = relpacientefactor.id_paciente WHERE "
             "patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    pacientes_riesgo = row[0]
    connection.dbdisconect(cnx)
    res = (pacientes_riesgo * 1.0)/(total_pacientes * 1.0)*100
    return res


#EDAD MEDIA DE PACIENTES CON UNA PATOLOGIA
def edad_media_pacientes_patologia(patologia):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT AVG(pacientes.edad) FROM patologias INNER JOIN episodios ON patologias.id_patologia = "
             "episodios.id_patologia INNER JOIN pacientes ON episodios.id_paciente = pacientes.id_paciente "
             "WHERE patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return row[0]


#PORCENTAJE DE PACIENTES POR SEXO CON UNA DETERMINADA PATOLOGIA
def sexo_patologia(patologia, sexo):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    #Total de pacientes con una patologia
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN pacientes ON episodios.id_paciente = pacientes.id_paciente WHERE "
             "patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    total_pacientes = row[0]
    #Total de pacientes con una patologia por sexo
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN pacientes ON episodios.id_paciente = pacientes.id_paciente WHERE "
             "patologias.id_patologia = '%d' AND pacientes.sexo = '%c'" % (patologia.id, sexo))
    cursor.execute(query)
    row = cursor.fetchone()
    pacientes_sexo = row[0]
    connection.dbdisconect(cnx)
    res = (pacientes_sexo * 1.0)/(total_pacientes * 1.0)*100
    return res


#CUANTOS PACIENTES CON UNA PATOLOGIA A HAN MUERTO EN UN PERIODO DE 30 DIAS?
def mortalidad_temprana_patologia(patologia):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN relepisodioprocedimiento on episodios.id_episodio = relepisodioprocedimiento.id_episodio "
             "INNER JOIN procedimientos ON relepisodioprocedimiento.id_procedimiento = procedimientos.id_procedimiento "
             "INNER JOIN relcomplicacionprocedimiento ON procedimientos.id_procedimiento = "
             "relcomplicacionprocedimiento.id_procedimiento INNER JOIN complicaciones ON "
             "relcomplicacionprocedimiento.id_complicacion = complicaciones.id_complicacion WHERE "
             "complicaciones.mortalidadTemprana = 'S' AND patologias.id_patologia = '%d'" % patologia.id)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return row[0]


#CUANTOS PACIENTES CON UNA PATOLOGIA Y UN PROCEDIMIENTO CONCRETOS SE HAN CURADO?
def curacion_patologia_procedimiento(patologia, tipop):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT count(*) FROM patologias INNER JOIN episodios ON patologias.id_patologia = episodios.id_patologia "
             "INNER JOIN relepisodioprocedimiento on episodios.id_episodio = relepisodioprocedimiento.id_episodio "
             "INNER JOIN procedimientos ON relepisodioprocedimiento.id_procedimiento = procedimientos.id_procedimiento "
             "INNER JOIN tipo_procedimiento ON procedimientos.id_tipop = tipo_procedimiento.id_tipop  INNER JOIN "
             "relcomplicacionprocedimiento ON procedimientos.id_procedimiento = "
             "relcomplicacionprocedimiento.id_procedimiento INNER JOIN complicaciones ON "
             "relcomplicacionprocedimiento.id_complicacion = complicaciones.id_complicacion WHERE "
             "complicaciones.mortalidadTemprana = 'N' AND complicaciones.mortalidadTardia = 'N' AND "
             "patologias.id_patologia = '%d' AND tipo_procedimiento.id_tipop = '%d'" % (patologia.id, tipop.id))
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return row[0]