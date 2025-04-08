class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def obtener_total_compras(self):
        return sum(pedido.obtener_total() for pedido in self.pedidos)

    def obtener_numero_pedidos(self):
        return len(self.pedidos)

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}, Número de pedidos: {self.obtener_numero_pedidos()}"
