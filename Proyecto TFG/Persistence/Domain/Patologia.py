class Patologia():
    def __init__(self, ide, n, nh, ids, idc):
        self.id = ide
        self.nombre = n
        self.numerohistorial = nh
        self.idservicio = ids
        self.idcentro = idc

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " numero historial: " + str(self.numerohistorial) \
               + " idservicio: " + str(self.idservicio) + " idcentro: " + str(self.idcentro)