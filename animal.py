class Animal:
    def __init__(self) -> None:
        pass

    def hacer_sonido(self):
        return "Sonido del animal"

class Perro(Animal):

    def hacer_sonido(self):
        return "Guau"
    
perro = Perro()

print(perro.hacer_sonido())

# IA

class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido del animal"

    def __str__(self):
        return f"Animal: {self.nombre}"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

    def __str__(self):
        return f"Perro: {self.nombre}"

# Crear una instancia de Perro
perro = Perro("Firulais")

# Llamar al método hacer_sonido
print(perro.hacer_sonido())  # Salida: Guau

# Imprimir la representación en cadena del objeto
print(perro)  # Salida: Perro: Firulais
