class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # Se guarda titulo y autor como tupla (inmutable)
        self._datos = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    @property
    def titulo(self):
        return self._datos[0]

    @property
    def autor(self):
        return self._datos[1]

    @property
    def categoria(self):
        return self._categoria

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self.titulo} - {self.autor} | Categoria: {self.categoria} | ISBN: {self.isbn}"