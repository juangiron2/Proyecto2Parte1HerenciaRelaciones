import unittest
from modelo.Cliente import Cliente
from modelo.Factura import Factura

class TestCliente(unittest.TestCase):
    def test_crear_cliente(self):
        cliente = Cliente("Juan Pérez", "123456789")
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.cedula, "123456789")

    def test_agregar_pedido(self):
        cliente = Cliente("Juan Pérez", "123456789")
        factura = Factura(cliente, "2024-10-18")
        cliente.agregar_pedido(factura)
        self.assertEqual(len(cliente.pedidos), 1)

    def test_obtener_total_compras(self):
        cliente = Cliente("Juan Pérez", "123456789")
        factura1 = Factura(cliente, "2024-10-18")
        factura2 = Factura(cliente, "2024-10-20")
        cliente.agregar_pedido(factura1)
        cliente.agregar_pedido(factura2)
        self.assertEqual(cliente.obtener_numero_pedidos(), 2)

if __name__ == "__main__":
    unittest.main()
