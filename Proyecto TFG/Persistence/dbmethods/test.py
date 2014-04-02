import radiologoMethods
import pacienteMethods
import materialMethods
import servicioMethods
import centroMethods
import evolucionMethods
import complicacionMethods
import patologiaMethods
import diagnosticoMethods
import pruebaDiagnosticaMethods
import procedimientosMethods
import relationMethods
from datetime import datetime, date, timedelta


#RADIOLOGOS
radiologoMethods.createradiologo('Pedro Gordillo')
print(radiologoMethods.readallradiologos())
print(radiologoMethods.readradiologobyid(1))
radiologoMethods.updateradiologo(2, "Raquel")
print(radiologoMethods.readradiologobyid(2))
radiologoMethods.deleteradiologo(2)
print(radiologoMethods.readallradiologos())

#PACIENTES
#pacienteMethods.createpaciente(12, 'charlie', date(2013, 10, 1), 'H', 'S', 'Sin enfermedades conocidas', 22, 22)
print(pacienteMethods.readallpacientes())
print(pacienteMethods.readpacientebyid(1))

#MATERIALES
#materialMethods.creatematerial('Ejemplo material 2')
print(materialMethods.readallmateriales())
print(materialMethods.readmaterialbyid(1))

#SERVICIOS
#servicioMethods.createservicio("Servicio 2")
print(servicioMethods.readallservicios())
print(servicioMethods.readserviciobyid(1))

#CENTROS
#centroMethods.createcentro("Centro 2")
print(centroMethods.readallcentros())
print(centroMethods.readcentrobyid(1))

#EVOLUCIONES
#evolucionMethods.createevolucion("resultado 2", "notas 2")
print(evolucionMethods.readallevoluciones())
print(evolucionMethods.readevolucionbyid(1))

#COMPLICACIONES
#complicacionMethods.createcomplicacion("complicacion 2", "S", "N")
print(complicacionMethods.readallcomplicaciones())
print(complicacionMethods.readcomplicacionbyid(1))

#PATOLOGIAS
#patologiaMethods.createpatologia('Patologia 2', 1, 1, 1)
print(patologiaMethods.readallpatologias())
print(patologiaMethods.readpatologiabyid(1))

#DIAGNOSTICOS
#diagnosticoMethods.creatediagnostico('diagnostico 2', patologiaMethods.readpatologiabyid(1))
print(diagnosticoMethods.readalldiagnosticos())
print(diagnosticoMethods.readdiagnosticobyid(1))

#PRUEBASDIAGNOSTICAS
#pruebaDiagnosticaMethods.createpruebadiagnostica('prueba diagnostica 2', patologiaMethods.readpatologiabyid(1))
print(pruebaDiagnosticaMethods.readallpruebasdiagnosticas())
print(pruebaDiagnosticaMethods.readpruebadiagnosticabyid(1))

#PROCEDIMIENTOS
#procedimientosMethods.createprocedimiento('Procedimiento 2', evolucionMethods.readevolucionbyid(1))
print(procedimientosMethods.readallprocedimientos())
print(procedimientosMethods.readprocedimientobyid(1))

#RELACIONES
#relationMethods.createrelprocmat(procedimientosMethods.readprocedimientobyid(2), materialMethods.readmaterialbyid(1))
print(relationMethods.readallmat_from_prod(1))
print(relationMethods.readallproc_from_mat(1))