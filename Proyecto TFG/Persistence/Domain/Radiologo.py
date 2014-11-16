class Radiologo:
    def __init__(self, ide, n):
        self.id = ide
        self.nombre = n

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre