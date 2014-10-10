class Paciente():
    def __init__(self, ide, nh, n, fn, s, enc, e, ec):
        self.id = ide
        self.numerohistorial = nh
        self.nombre = n
        self.fechanacimiento = fn
        self.sexo = s
        self.enfermedadesconocidas = enc
        self.edad = e
        self.edadconsulta = ec

    def __repr__(self):
        return "id: " + str(self.id) + " numero historial: " + str(self.numerohistorial) + " nombre: " + self.nombre + " fecha nacimiento: " +\
               str(self.fechanacimiento) + " sexo: " + self.sexo +" enfermedades conocidas: " +\
               self.enfermedadesconocidas + " edad: " + str(self.edad) + " edad consulta: " + str(self.edadconsulta)