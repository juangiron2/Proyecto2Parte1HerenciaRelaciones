import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from Modelo.Producto import Productos
from CRUD.crud_Producto import productos, crear_producto, Listar_productos, actualizar_producto, eliminar_producto

class TestCrudProducto(unittest.TestCase):
    def setUp(self):
        productos.clear()
        self.producto = Productos("Laptop", 1000.0)
        productos.append(self.producto)

    @patch('builtins.input', side_effect=["Tablet", "300.0"])
    def test_crear_producto(self, mock_input):
        crear_producto()
        self.assertEqual(len(productos), 2)
        self.assertEqual(productos[1].nombre, "Tablet")

    def test_listar_productos(self):
        with patch('sys.stdout') as fake_stdout:
            Listar_productos()
            self.assertIn("Laptop", fake_stdout.getvalue())

    @patch('builtins.input', side_effect=["Laptop", "PC de escritorio", "1200.0"])
    def test_actualizar_producto(self, mock_input):
        actualizar_producto()
        self.assertEqual(productos[0].nombre, "PC de escritorio")
        self.assertEqual(productos[0].precio, 1200.0)

    @patch('builtins.input', side_effect=["Laptop"])
    def test_eliminar_producto(self, mock_input):
        eliminar_producto()
        self.assertEqual(len(productos), 0)

#ejecuta esta prueba usando el comando "python -m unittest discover"

