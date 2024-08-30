class Empleado:
    def __str__(self, salario) -> str:
        self.salario = salario

    def salario(self):
        self.salario *= 1.1

    def descripcion(self):
        return f"Salario actual {self.salario}."

class Gerente(Empleado):
    
    def salario(self):
        return super().salario(salario)
    
kevin = Gerente(100)

print(kevin.salario())