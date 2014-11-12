from Persistence.DBCon.connection import *
from Persistence.Domain.Paciente import *
from Persistence.Domain.Factor import *
from Persistence.Domain.Episodio import *


def get_by_id(ide):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pacientes WHERE id_paciente = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])


def get_all():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = "SELECT * FROM pacientes"
    cursor.execute(query)
    dbdisconect(cnx)
    for (idpaciente, numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta) in cursor:
        result.append(Paciente(idpaciente, numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta))
    return result


def create(paciente):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO pacientes VALUES('%d','%s','%s','%s','%c','%s','%d','%d')" % (paciente.id,
        paciente.numeroHistorial, paciente.nombre, paciente.fechaNacimiento, paciente.sexo,
        paciente.enfermedadesConocidas, paciente.edad, paciente.edadConsulta))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def update(paciente):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE pacientes SET numeroHistorial = '%s' nombre = '%s' fechaNacimiento = '%s' sexo = '%c' "
             "enfermedadesConocidas = '%s' edad = '%d' edadConsulta = '%d' WHERE id_paciente = '%d'"
             % (paciente.numeroHistorial, paciente.nombre, paciente.fechaNacimiento, paciente.sexo, paciente.enfermedadesConocidas, paciente.edad,
                paciente.edadConsulta, paciente.id))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def delete(paciente):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM pacientes WHERE id_paciente = '%d'" % paciente.id)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def get_by_name(nombre):
    text = "%"+nombre+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pacientes WHERE nombre LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (idpaciente, numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta) in cursor:
        result.append(Paciente(idpaciente, numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta))
    return result


def get_by_numeroHistorial(numeroHistorial):
    text = "%"+numeroHistorial+"%"
    result = []
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pacientes WHERE numeroHistorial LIKE '%s'" % text)
    cursor.execute(query)
    dbdisconect(cnx)
    for (idpaciente, numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta) in cursor:
        result.append(Paciente(idpaciente, numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta))
    return result


def get_factores(paciente):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT factoresderiesgo.id_factor, factoresderiesgo.nombre FROM relpacientefactor INNER JOIN factoresderiesgo ON relpacientefactor.id_factor = factoresderiesgo.id_factor WHERE relpacientefactor.id_paciente ='%d'" % paciente.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_factor, nombre) in cursor:
        result.append(Factor(id_factor, nombre))
    return result


def get_episodios(paciente):
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM episodios WHERE id_paciente = '%d'" % paciente.id)
    cursor.execute(query)
    dbdisconect(cnx)
    for (id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia) in cursor:
        result.append(Episodio(id_episodio, nombre, fecha, id_paciente, id_servicio, id_centro, id_patologia))
    return result