from data.inventario_db import InventarioDB
from Vista.inventario_view import InventarioView

class InventarioController:
    def __init__(self):
        self.db = InventarioDB()
        self.view = InventarioView()

        self.db.conectar()
        self.db.crear_tabla()

    def registrar_producto(self):
        producto = self.view.pedir_datos_producto()
        self.db.agregar_producto(producto)
        self.view.mostrar_mensaje("Producto registrado")

    def mostrar_productos(self):
        productos = self.db.listar_productos()
        self.view.mostrar_productos(productos)

    def cambiar_stock(self):
        id_producto = self.view.pedir_id_producto()
        nuevo_stock = self.view.pedir_stock()

        self.db.actualizar_stock(id_producto, nuevo_stock)
        self.view.mostrar_mensaje("Stock actualizado")

    def eliminar_producto(self):
        id_producto = self.view.pedir_id_producto()

        self.db.eliminar_producto(id_producto)
        self.view.mostrar_mensaje("Producto eliminado")

    def filtrar_por_categoria(self):
        categoria = self.view.pedir_categoria()
        productos = self.db.buscar_por_categoria(categoria)

        self.view.mostrar_productos(productos)

    def mostrar_bajo_stock(self):
        limite = self.view.pedir_limite_stock()
        productos = self.db.productos_bajo_stock(limite)

        self.view.mostrar_productos(productos)

    def iniciar(self):
        while True:
            opcion = self.view.mostrar_menu()

            if opcion == "1":
                self.registrar_producto()

            elif opcion == "2":
                self.mostrar_productos()

            elif opcion == "3":
                self.cambiar_stock()

            elif opcion == "4":
                self.eliminar_producto()

            elif opcion == "5":
                self.filtrar_por_categoria()

            elif opcion == "6":
                self.mostrar_bajo_stock()

            elif opcion == "7":
                self.db.cerrar()
                print("Sistema finalizado")
                break

            else:
                print("Opcion incorrecta")