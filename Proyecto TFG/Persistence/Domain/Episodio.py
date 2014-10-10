class Episodio():
    def __init__(self, ide, n, nh, ids, idc, idp):
        self.id = ide
        self.nombre = n
        self.idpaciente = nh
        self.idservicio = ids
        self.idcentro = idc
        self.idpatologia = idp

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " idpaciente: " + str(self.idpaciente) \
               + " idservicio: " + str(self.idservicio) + " idcentro: " + str(self.idcentro)  + " idpatologia: " + \
               str(self.idpatologia)