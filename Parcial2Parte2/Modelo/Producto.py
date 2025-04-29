class Productos:
    def __init__(self, nombre, precio):
        self.set_nombre(nombre)
        self.set_precio(precio)

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.nombre = nombre
        else:
            raise ValueError("El nombre del producto no puede estar vacío")

    def set_precio(self, precio):
        if isinstance(precio, (int, float)) and precio > 0:
            self.precio = precio
        else:
            raise ValueError("El precio debe ser un número positivo")

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"
