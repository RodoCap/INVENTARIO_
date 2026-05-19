class Producto:
    def __init__(self, nombre, precio, stock, categoria, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        return f"[{self.nombre} - ${self.precio} | Stock: {self.stock} | Categoria: {self.categoria} ]"