from Persistence.Repositories import QuerysRepository
from Persistence.Domain import Patologia, TipoProcedimiento


#QUE PORCENTAJE DE UNA PATOLOGIA A HA PRESENTADO COMPLICACIONES?
def porcentaje_complicaciones_patologia(patologia):
    return QuerysRepository.porcentaje_complicaciones_patologia(patologia)


#QUE PORCENTAJE/ NUM DE PACIENTES CON UNA PATOLOGIA A PRESENTABAN FACTORES DE RIESGO?
def pacientes_factores_patologia(patologia):
    return QuerysRepository.pacientes_factores_patologia(patologia)


#EDAD MEDIA DE PACIENTES CON UNA PATOLOGIA
def edad_media_pacientes_patologia(patologia):
    return QuerysRepository.edad_media_pacientes_patologia(patologia)


#PORCENTAJE DE PACIENTES POR SEXO CON UNA DETERMINADA PATOLOGIA
def sexo_patologia(patologia, sexo):
    return QuerysRepository.sexo_patologia(patologia, sexo)


#CUANTOS PACIENTES CON UNA PATOLOGIA A HAN MUERTO EN UN PERIODO DE 30 DIAS?
def mortalidad_temprana_patologia(patologia):
    return QuerysRepository.mortalidad_temprana_patologia(patologia)


#CUANTOS PACIENTES CON UNA PATOLOGIA Y UN PROCEDIMIENTO CONCRETOS SE HAN CURADO?
def curacion_patologia_procedimiento(patologia, tipoprocedimiento):
    return QuerysRepository.curacion_patologia_procedimiento(patologia, tipoprocedimiento)