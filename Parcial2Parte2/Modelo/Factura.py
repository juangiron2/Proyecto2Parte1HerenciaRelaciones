from datetime import datetime

class Factura:
    def __init__(self, cliente, fecha):
        self._cliente = cliente  # Atributo privado
        self.set_fecha(fecha)
        self._productos = []
        self._total = 0.0
        self._id_factura = None  # Se asignará externamente con uuid

    def set_fecha(self, fecha):
        try:
            self._fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("La fecha debe estar en formato YYYY-MM-DD")

    def get_fecha(self):
        return self._fecha

    def set_id_factura(self, id_factura):
        self._id_factura = id_factura

    def get_id_factura(self):
        return self._id_factura

    def agregar_producto(self, producto):
        self._productos.append(producto)
        self._total += producto.get_precio()  # Usar método getter

    def obtener_detalle_productos(self):
        return "\n".join([str(producto) for producto in self._productos])

    def obtener_total(self):
        return self._total

    def get_cliente(self):
        return self._cliente

    def get_productos(self):
        return self._productos

    def __str__(self):
        return f"Factura ID: {self._id_factura}\n" \
               f"Cliente: {self._cliente.get_nombre()}\n" \
               f"Fecha: {self._fecha}\n" \
               f"Productos:\n{self.obtener_detalle_productos()}\n" \
               f"Total: ${self._total:.2f}"
