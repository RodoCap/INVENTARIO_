import flet as ft
from Modelo.producto import Producto

class InventarioView:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Sistema de Inventario"
        self.page.window_width = 500
        self.page.window_height = 700

        # Campos
        self.txt_nombre = ft.TextField(label="Nombre")
        self.txt_precio = ft.TextField(label="Precio")
        self.txt_stock = ft.TextField(label="Stock")
        self.txt_categoria = ft.TextField(label="Categoría")

        self.txt_id = ft.TextField(label="ID")
        self.txt_nuevo_stock = ft.TextField(label="Nuevo Stock")
        self.txt_limite = ft.TextField(label="Límite de Stock")

        # Área de salida
        self.salida = ft.Column()

    def mostrar_menu(self):

        self.page.add(
            ft.Text(
                "Sistema de Inventario",
                size=25,
                weight="bold"
            ),

            self.txt_nombre,
            self.txt_precio,
            self.txt_stock,
            self.txt_categoria,

            ft.Row([
                ft.ElevatedButton("1. Registrar producto"),
                ft.ElevatedButton("2. Mostrar producto"),
            ]),

            self.txt_id,
            self.txt_nuevo_stock,

            ft.Row([
                ft.ElevatedButton("3. Actualizar stock"),
                ft.ElevatedButton("4. Eliminar producto"),
            ]),

            ft.Row([
                ft.ElevatedButton("5. Buscar categoría"),
                ft.ElevatedButton("6. Bajo stock"),
            ]),

            self.txt_limite,

            ft.ElevatedButton("7. Salir"),

            ft.Divider(),

            self.salida
        )

    def pedir_datos_producto(self):

        nombre = self.txt_nombre.value
        precio = float(self.txt_precio.value)
        stock = int(self.txt_stock.value)
        categoria = self.txt_categoria.value

        return Producto(nombre, precio, stock, categoria)

    def pedir_id_producto(self):

        return int(self.txt_id.value)

    def pedir_stock(self):

        return int(self.txt_nuevo_stock.value)

    def pedir_categoria(self):

        return self.txt_categoria.value

    def pedir_limite_stock(self):

        return int(self.txt_limite.value)

    def mostrar_productos(self, productos):

        self.salida.controls.clear()

        if productos:

            for producto in productos:
                self.salida.controls.append(
                    ft.Text(str(producto))
                )

        else:
            self.salida.controls.append(
                ft.Text("No hay productos")
            )

        self.page.update()

    def mostrar_mensaje(self, mensaje):

        self.salida.controls.append(
            ft.Text(mensaje)
        )

        self.page.update()