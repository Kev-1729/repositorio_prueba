# Yo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self) -> str:
        return f"La altura {self.altura} y la base {self.base}."
    
    def __repr__(self) -> str:
        return self.__str__()
    
figura = Rectangulo(4, 5)
print(figura)

# IA

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self) -> str:
        return f"Rectángulo con altura {self.altura} y base {self.base}."

    def __repr__(self) -> str:
        return f"Rectangulo(base={self.base}, altura={self.altura})"

# Crear una instancia de Rectangulo
figura = Rectangulo(4, 5)

# Imprimir la representación en cadena del objeto
print(figura)  # Esto llamará a __str__

# Imprimir la representación oficial del objeto
print(repr(figura))  # Esto llamará a __repr__