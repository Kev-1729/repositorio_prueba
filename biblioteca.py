class Libro:

    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self) -> str:
        if self.disponible:
            return "Libro Disponible."
        else:
            return "Libro No Disponible."

class Miembro:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.libros_prestados = []

    def pedir_libro(self, obj):

        if obj.disponible:
            obj.disponible = False
            self.libros_prestados.append(obj)
        else:
            print("Libro no disponible")

    def devolver_libro(self, obj):
        if obj in obj.libros_prestados:
            obj.disponible = True
            self.libros_prestados.remove(obj)

    def __str__(self) -> str:
        return f"{self.nombre} ha prestado {[libro.titulo for libro in self.libros_prestados]}"

class Biblioteca:
    
    def __init__(self) -> None:
        self.libros = []
        self.miembros = []

    def agregar_libro(self, obj):
        self.libros.append(obj)

    def agregar_usuario(self, obj):
        self.miembros.append(obj)

    def mostar_libros(self) -> str:
        return f"Libros disponibles: {[libro for libro in self.libros]}"
    
    def mostar_usuarios(self) -> str:
        return f"Usuarios: {[usuario for usuario in self.miembros]}"
    

biblioteca = Biblioteca()

libro1 = Libro("Cien Años de Soledad", "Gabriel García Marquez")
libro2 = Libro("Marco Aurelio Denegrí", "Lexicografía")

usuario1 = Miembro("Kevin")
usuario2 = Miembro("Jose")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_usuario(usuario2)

usuario1.pedir_libro(libro1)
usuario2.pedir_libro(libro2)

print(usuario1)
print(usuario2)