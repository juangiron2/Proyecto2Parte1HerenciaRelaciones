import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from Modelo.Factura import Factura
from CRUD.crud_Facturas import facturas, crear_factura, listar_facturas, actualizar_factura, eliminar_factura
from Modelo.Cliente import Cliente
from Modelo.Producto import Productos

class TestCrudFacturas(unittest.TestCase):
    def setUp(self):
        Cliente.clear()
        Productos.clear()
        facturas.clear()
        self.cliente = Cliente("Ana Gómez", "0987654321")
        self.producto = Productos("Smartphone", 500.0)
        Cliente.append(self.cliente)
        Productos.append(self.producto)
        self.factura = Factura(self.cliente, "2024-10-01")
        self.factura.id_factura = "1234-abcd"
        facturas.append(self.factura)

    @patch('builtins.input', side_effect=["0987654321", "2024-11-01", "Smartphone", "fin"])
    def test_crear_factura(self, mock_input):
        crear_factura()
        self.assertEqual(len(facturas), 2)
        self.assertEqual(facturas[1].cliente.nombre, "Ana Gómez")

    def test_listar_facturas(self):
        with patch('sys.stdout') as fake_stdout:
            listar_facturas()
            self.assertIn("Ana Gómez", fake_stdout.getvalue())

    @patch('builtins.input', side_effect=["1234-abcd", "2024-12-01", "2"])
    def test_actualizar_factura(self, mock_input):
        actualizar_factura()
        self.assertEqual(facturas[0].fecha, "2024-12-01")

    @patch('builtins.input', side_effect=["1234-abcd"])
    def test_eliminar_factura(self, mock_input):
        eliminar_factura()
        self.assertEqual(len(facturas), 0)

#ejecuta esta prueba usando el comando "python -m unittest discover"
