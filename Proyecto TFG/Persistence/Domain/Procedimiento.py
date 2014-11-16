class Procedimiento:
    def __init__(self, ide, idt, idev):
        self.id = ide
        self.idtipop = idt
        self.idevolucion = idev

    def __repr__(self):
        return "id: " + str(self.id) + " idtipoprocedimiento: " + self.idtipop + " idevolucion: " + str(self.idevolucion)