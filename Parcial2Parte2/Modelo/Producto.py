class Productos:
    def __init__(self, nombre, precio):
        self.set_nombre(nombre)
        self.set_precio(precio)

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre  # Hacemos el nombre privado
        else:
            raise ValueError("El nombre del producto no puede estar vacío")

    def get_nombre(self):
        return self.__nombre  # Getter para acceder al nombre

    def set_precio(self, precio):
        if isinstance(precio, (int, float)) and precio > 0:
            self.__precio = precio  # Hacemos el precio privado
        else:
            raise ValueError("El precio debe ser un número positivo")

    def get_precio(self):
        return self.__precio  # Getter para acceder al precio

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio:.2f}"
