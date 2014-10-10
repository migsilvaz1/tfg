class PruebaDiagnostica():
    def __init__(self, ide, n, idr):
        self.id = ide
        self.nombre = n
        self.idradiologo = idr

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " idradiologo: " + str(self.idradiologo)