class Complicacion():
    def __init__(self, ide,  n, nmt, mt):
        self.id = ide
        self.nombre = n
        self.mortalidadtemprana = nmt
        self.mortalidadtardia = mt

    def __repr__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " Mortalidad temprana: " + self.mortalidadtemprana \
               + " Mortalidad tardia: " + self.mortalidadtardia