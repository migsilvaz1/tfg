class PruebaDiagnostica():
    def __init__(self, ide, n, idp, idr):
        self.id = ide
        self.nombre = n
        self.idpatologia = idp
        self.idradiologo = idr

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " idpatologia: " + str(self.idpatologia) + \
               " idradiologo: " + str(self.idradiologo)