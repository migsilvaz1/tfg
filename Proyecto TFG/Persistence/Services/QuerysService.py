from Persistence.Repositories import QuerysRepository
from Persistence.Domain import Patologia, Procedimiento


#QUE PORCENTAJE DE UNA PATOLOGIA A HA PRESENTADO COMPLICACIONES?
def porcentaje_complicaciones_patologia(patologia):
    if not isinstance(patologia, Patologia) or not isinstance(patologia.id, int):
        raise TypeError("El dato de entrada no es correcto")
    return QuerysRepository.porcentaje_complicaciones_patologia(patologia)


#QUE PORCENTAJE/ NUM DE PACIENTES CON UNA PATOLOGIA A PRESENTABAN FACTORES DE RIESGO?
def pacientes_factores_patologia(patologia):
    if not isinstance(patologia, Patologia) or not isinstance(patologia.id, int):
        raise TypeError("El dato de entrada no es correcto")
    return QuerysRepository.pacientes_factores_patologia(patologia)


#EDAD MEDIA DE PACIENTES CON UNA PATOLOGIA
def edad_media_pacientes_patologia(patologia):
    if not isinstance(patologia, Patologia) or not isinstance(patologia.id, int):
        raise TypeError("El dato de entrada no es correcto")
    return QuerysRepository.edad_media_pacientes_patologia(patologia)


#PORCENTAJE DE PACIENTES POR SEXO CON UNA DETERMINADA PATOLOGIA
def sexo_patologia(patologia, sexo):
    if not isinstance(patologia, Patologia) or not isinstance(patologia.id, int):
        raise TypeError("Patologia de entrada no es correcta")
    elif sexo == "H" or sexo == "M":
        return QuerysRepository.sexo_patologia(patologia, sexo)
    else:
        raise TypeError("Error en el sexo")


#CUANTOS PACIENTES CON UNA PATOLOGIA A HAN MUERTO EN UN PERIODO DE 30 DIAS?
def mortalidad_temprana_patologia(patologia):
    if not isinstance(patologia, Patologia) or not isinstance(patologia.id, int):
        raise TypeError("Patologia de entrada no es correcta")
    return QuerysRepository.mortalidad_temprana_patologia(patologia)


#CUANTOS PACIENTES CON UNA PATOLOGIA Y UN PROCEDIMIENTO CONCRETOS SE HAN CURADO?
def curacion_patologia_procedimiento(patologia, procedimiento):
    if not isinstance(patologia, Patologia) or not isinstance(patologia.id, int):
        raise TypeError("Patologia de entrada no es correcta")
    if not isinstance(procedimiento, Procedimiento) or not isinstance(procedimiento.id, int):
        raise TypeError("Procedimiento de entrada no es correcto")
    return QuerysRepository.curacion_patologia_procedimiento()