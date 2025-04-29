import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from Modelo.Control_de_plagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):
    def test_crear_control_plagas(self):
        producto = ControlPlagas("Insecticida", 10000, "ICA123", 15, 7)
        self.assertEqual(producto.nombre, "Insecticida")
        self.assertEqual(producto.registro_ica, "ICA123")
        self.assertEqual(producto.frecuencia_aplicacion, 15)

    def test_frecuencia_invalida(self):
        with self.assertRaises(ValueError):
            ControlPlagas("Insecticida", 10000, "ICA123", -5, 7)

if __name__ == "__main__":
    unittest.main()
