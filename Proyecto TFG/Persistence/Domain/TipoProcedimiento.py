class TipoProcedimiento:
    def __init__(self, i, n):
        self.id = i
        self.nombre = n

    def __repr__(self):
         return "id: " + str(self.id) + " nombre: " + self.nombre