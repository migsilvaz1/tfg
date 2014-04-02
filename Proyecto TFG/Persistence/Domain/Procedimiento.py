class Procedimiento():
    def __init__(self, ide, n, idev):
        self.id = ide
        self.nombre = n
        self.idevolucion = idev

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " idevolucion: " + str(self.idevolucion)