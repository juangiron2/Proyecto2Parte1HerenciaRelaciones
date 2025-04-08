import unittest
from modelo.Producto import Producto


class TestProducto(unittest.TestCase):
    def test_crear_producto_valido(self):
        producto = Producto("Fertilizante", 20000)
        self.assertEqual(producto.nombre, "Fertilizante")
        self.assertEqual(producto.precio, 20000)

    def test_nombre_invalido(self):
        with self.assertRaises(ValueError):
            Producto("", 20000)

    def test_precio_invalido(self):
        with self.assertRaises(ValueError):
            Producto("Fertilizante", -100)

if __name__ == "__main__":
    unittest.main()
