from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario ISBN -> Libro
        self.libros_disponibles = {}

        # Diccionario ID -> Usuario
        self.usuarios = {}

        # Set de IDs únicos
        self.ids_usuarios = set()

    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros_disponibles:
            print("El libro ya existe en el sistema.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros_disponibles[isbn] = libro

        print("Libro agregado correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El ID de usuario ya está registrado.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe.")
            return

        if isbn not in self.libros_disponibles:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros_disponibles.pop(isbn)

        usuario.prestar_libro(libro)

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe.")
            return

        usuario = self.usuarios[id_usuario]

        libro = usuario.devolver_libro(isbn)

        if libro:
            self.libros_disponibles[isbn] = libro
            print("Libro devuelto correctamente.")
        else:
            print("El usuario no tenía ese libro.")

    def buscar_por_titulo(self, titulo):

        encontrados = False

        for libro in self.libros_disponibles.values():

            if libro.titulo.lower() == titulo.lower():
                print(libro)
                encontrados = True

        if not encontrados:
            print("No se encontraron libros con ese título.")

    def buscar_por_autor(self, autor):

        encontrados = False

        for libro in self.libros_disponibles.values():

            if libro.autor.lower() == autor.lower():
                print(libro)
                encontrados = True

        if not encontrados:
            print("No se encontraron libros de ese autor.")

    def buscar_por_categoria(self, categoria):

        encontrados = False

        for libro in self.libros_disponibles.values():

            if libro.categoria.lower() == categoria.lower():
                print(libro)
                encontrados = True

        if not encontrados:
            print("No se encontraron libros de esa categoría.")

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no existe.")
            return

        usuario = self.usuarios[id_usuario]

        if not usuario.libros_prestados:
            print("El usuario no tiene libros prestados.")
            return

        print("Libros prestados:")

        for libro in usuario.libros_prestados:
            print(libro)