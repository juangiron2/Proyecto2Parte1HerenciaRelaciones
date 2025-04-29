import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from Modelo.Producto import Productos


class TestProducto(unittest.TestCase):
    def test_crear_producto_valido(self):
        producto = Productos("Fertilizante", 20000)
        self.assertEqual(producto.nombre, "Fertilizante")
        self.assertEqual(producto.precio, 20000)

    def test_nombre_invalido(self):
        with self.assertRaises(ValueError):
            Productos("", 20000)

    def test_precio_invalido(self):
        with self.assertRaises(ValueError):
            Productos("Fertilizante", -100)

if __name__ == "__main__":
    unittest.main()
