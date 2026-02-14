# servicios/inventario.py

from modelos.producto import Producto

class Inventario:
    """
    Clase encargada de gestionar los productos.
    """

    def __init__(self):
        self.productos = []  # Lista principal de almacenamiento

    def añadir_producto(self, producto):
        # Validar que el ID no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
            return

        for p in self.productos:
            print(p)
