import unittest
from modelo.Control_plagas import Control_plagas

class TestControlPlagas(unittest.TestCase):
    def test_crear_control_plagas(self):
        producto = Control_plagas("Insecticida", 10000, "ICA123", 15, 7)
        self.assertEqual(producto.nombre, "Insecticida")
        self.assertEqual(producto.registro_ica, "ICA123")
        self.assertEqual(producto.frecuencia_aplicacion, 15)

    def test_frecuencia_invalida(self):
        with self.assertRaises(ValueError):
            Control_plagas("Insecticida", 10000, "ICA123", -5, 7)

if __name__ == "__main__":
    unittest.main()
