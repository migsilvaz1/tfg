from Persistence.DBCon.connection import *
from Persistence.Domain.Paciente import *


def readallpacientes():
    cnx = dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = "SELECT * FROM pacientes"
    cursor.execute(query)
    dbdisconect(cnx)
    for (numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta) in cursor:
        result.append(Paciente(numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta
    ))
    return result


def readpacientebyid(identificator):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT * FROM pacientes WHERE numeroHistorial = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    dbdisconect(cnx)
    return Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


def createpaciente(numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("INSERT INTO pacientes VALUES('%d','%s','%s','%c','%s','%d','%d')" % (numeroHistorial, nombre,
             fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def updatepaciente(numeroHistorial, nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta):
    cnx = dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("UPDATE pacientes SET nombre = '%s' fechaNacimiento = '%s' sexo = '%c' enfermedadesConocidas = '%s' "
             "edad = '%d' edadConsulta = '%d' WHERE numeroHistorial = '%d'"
             % (nombre, fechaNacimiento, sexo, enfermedadesConocidas, edad, edadConsulta, numeroHistorial))
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)


def deletepaciente(numeroHistorial):
    cnx = dbconnect()
    TODO borrar el FACTOR asociado al paciente en la tabla relPacienteFactor
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM pacientes WHERE numeroHistorial = '%d'" % numeroHistorial)
    cursor.execute(query)
    cnx.commit()
    dbdisconect(cnx)