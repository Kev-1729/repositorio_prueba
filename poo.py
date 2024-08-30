class Programador:
    def __init__(self, nombre, apellido, lenguaje, sistema):
        self.nombre = nombre
        self.apellido = apellido
        self.lenguaje = lenguaje
        self.sistema = sistema

    def descripción(self):
        return f" Nombre: {self.nombre}\n Apellido: {self.apellido}\n Lenguaje: {self.lenguaje}\n Sistema: {self.sistema}"

programador1 = Programador("Kevin", "Tupac", "python", "linux")

print(programador1.descripción())