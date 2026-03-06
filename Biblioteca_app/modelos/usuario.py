class Usuario:

    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario
        # Lista para almacenar libros prestados
        self._libros_prestados = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def libros_prestados(self):
        return self._libros_prestados

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):

        for libro in self._libros_prestados:
            if libro.isbn == isbn:
                self._libros_prestados.remove(libro)
                return libro

        return None

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"