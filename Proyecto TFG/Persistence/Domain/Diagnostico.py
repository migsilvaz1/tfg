class Diagnostico():
    def __init__(self, ide, n, idp):
        self.id = ide
        self.nombre = n
        self.idpatologia = idp

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " idpatologia: " + str(self.idpatologia)