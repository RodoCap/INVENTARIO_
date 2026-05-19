import sqlite3
from sqlite3 import Error
from Modelo.producto import Producto

class InventarioDB:
    def __init__(self, dbName="inventario.db"):
        self.dbName = dbName
        self.connection = None
    def conectar(self):
        try:
            self.connection = sqlite3.connect(self.dbName)
            self.connection.row_factory = sqlite3.Row
            print("Conexion exitosa")
        except Error as e:
            print("Error al conectar:", e)

    def crear_tabla(self):
        sql = """
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def agregar_producto(self, producto):
        sql = """
        INSERT INTO productos(nombre, precio, stock, categoria)
        VALUES (?, ?, ?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (
            producto.nombre,
            producto.precio,
            producto.stock,
            producto.categoria
        ))
        self.connection.commit()

    def listar_productos(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()

        productos = []

        for fila in filas:
            productos.append(
                Producto(
                    fila["nombre"],
                    fila["precio"],
                    fila["stock"],
                    fila["categoria"],
                    fila["id"],
                )
            )
        return productos
    
    def actualizar_stock(self, id_producto, nuevo_stock):
        sql = "UPDATE productos SET stock=? WHERE id=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nuevo_stock, id_producto))
        self.connection.commit()

    def eliminar_producto(self, id_producto):
        sql = "DELETE FROM productos WHERE id=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_producto,))
        self.connection.commit()

    def buscar_por_categoria(self, categoria):
        sql = "SELECT * FROM productos WHERE categoria=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (categoria,))
        filas = cursor.fetchall()
        productos = []

        for fila in filas:
            productos.append(
                Producto(
                    fila["nombre"],
                    fila["precio"],
                    fila["stock"],
                    fila["categoria"],
                    fila["id"] 
                )
            )

        return productos
    
    def productos_bajo_stock(self, limite):
        sql = "SELECT * FROM productos WHERE stock < ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (limite,))
        filas = cursor.fetchall()

        productos = []

        for fila in filas:
            productos.append(
                Producto(
                    fila["nombre"],
                    fila["precio"],
                    fila["stock"],
                    fila["categoria"],
                    fila["id"],
                )
            )
        return productos
   
    def cerrar(self):
        if self.connection:
            self.connection.close()
            print("Conexion cerrada")


        