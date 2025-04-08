from datetime import datetime

class Factura:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.set_fecha(fecha)
        self.productos = []
        self.total = 0.0

    def set_fecha(self, fecha):
        try:
            self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("La fecha debe estar en formato YYYY-MM-DD")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def obtener_detalle_productos(self):
        return "\n".join([str(producto) for producto in self.productos])

    def obtener_total(self):
        """Método que devuelve el total de la factura."""
        return self.total

    def __str__(self):
        return f"Factura del Cliente: {self.cliente.nombre}\n" \
               f"Fecha: {self.fecha}\n" \
               f"Productos:\n{self.obtener_detalle_productos()}\n" \
               f"Total: ${self.total:.2f}"
