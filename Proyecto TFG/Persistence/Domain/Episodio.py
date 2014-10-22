class Episodio():
    def __init__(self, ide, n, f, nh, ids, idc, idp):
        self.id = ide
        self.nombre = n
        self.fecha = f
        self.idpaciente = nh
        self.idservicio = ids
        self.idcentro = idc
        self.idpatologia = idp

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre +" fecha: " + str(self.fecha) + " idpaciente: " + str(self.idpaciente) \
               + " idservicio: " + str(self.idservicio) + " idcentro: " + str(self.idcentro)  + " idpatologia: " + \
               str(self.idpatologia)