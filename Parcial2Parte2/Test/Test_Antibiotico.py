import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from Modelo.Antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):
    def test_crear_antibiotico_valido(self):
        antibiotico = Antibiotico("Penicilina", 50000, 500, "Bovino")
        self.assertEqual(antibiotico.nombre, "Penicilina")
        self.assertEqual(antibiotico.precio, 50000)
        self.assertEqual(antibiotico.dosis, 500)
        self.assertEqual(antibiotico.tipo_animal, "Bovino")

    def test_dosis_invalida(self):
        with self.assertRaises(ValueError):
            Antibiotico("Amoxicilina", 45000, 300, "Porcino")  #Dosis fuera del rango permitido

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            Antibiotico("Cefalexina", 60000, 450, "Gato")  #Tipo de animal no válido

if __name__ == "__main__":
    unittest.main()
