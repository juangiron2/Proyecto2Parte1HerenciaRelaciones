import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from Modelo.Factura import Factura
from Modelo.Cliente import Cliente
from Modelo.Producto import Productos

class TestFactura(unittest.TestCase):
    def test_crear_factura(self):
        cliente = Cliente("Ana García", "987654321")
        factura = Factura(cliente, "2024-10-18")
        self.assertEqual(factura.cliente.nombre, "Ana García")
        self.assertEqual(factura.fecha.strftime("%Y-%m-%d"), "2024-10-18")

    def test_agregar_producto(self):
        cliente = Cliente("Ana García", "987654321")
        factura = Factura(cliente, "2024-10-18")
        producto = Productos("Control Plagas", 15000)
        factura.agregar_producto(producto)
        self.assertEqual(factura.total, 15000)

    def test_fecha_invalida(self):
        cliente = Cliente("Ana García", "987654321")
        with self.assertRaises(ValueError):
            Factura(cliente, "18-10-2024")

if __name__ == "__main__":
    unittest.main()
