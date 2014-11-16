class Diagnostico:
    def __init__(self, ide, n, idep):
        self.id = ide
        self.nombre = n
        self.idepisodio = idep

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " idpatologia: " + str(self.idepisodio)