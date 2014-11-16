class Evolucion:
    def __init__(self, ide, r, n):
        self.id = ide
        self.resultado = r
        self.notas = n

    def __repr__(self):
        return "id: " + str(self.id) + " resultado: " + self.resultado + " notas: " + self.notas