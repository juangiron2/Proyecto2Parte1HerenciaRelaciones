import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from Modelo.Control_de_fertilizante import ControlFertilizantes
from datetime import datetime

class TestControlFertilizantes(unittest.TestCase):
    def test_crear_control_fertilizantes_valido(self):
        control = ControlFertilizantes("Nutrientes Plus", 30000, "ICA456", 30, "2024-01-15")
        self.assertEqual(control.nombre, "Nutrientes Plus")
        self.assertEqual(control.precio, 30000)
        self.assertEqual(control.registro_ica, "ICA456")
        self.assertEqual(control.frecuencia_aplicacion, 30)
        self.assertEqual(control.ultima_aplicacion, datetime.strptime("2024-01-15", "%Y-%m-%d").date())

    def test_frecuencia_aplicacion_invalida(self):
        with self.assertRaises(ValueError):
            ControlFertilizantes("Fertilizante X", 25000, "ICA123", -10, "2024-05-20")  #Frecuencia negativa

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            ControlFertilizantes("Fertilizante Y", 28000, "ICA789", 45, "20-05-2024")  #Formato de fecha incorrecto

    def test_dias_desde_ultima_aplicacion(self):
        control = ControlFertilizantes("Fertilizante Z", 35000, "ICA101", 15, "2024-10-25")
        dias_desde = (datetime.now().date() - datetime.strptime("2024-10-25", "%Y-%m-%d").date()).days
        self.assertEqual(control.dias_desde_ultima_aplicacion(), dias_desde)

if __name__ == "__main__":
    unittest.main()
