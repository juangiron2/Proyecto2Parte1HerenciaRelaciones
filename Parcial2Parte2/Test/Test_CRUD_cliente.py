import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from Modelo.Cliente import Cliente
from CRUD.crud_Cliente import clientes, crear_cliente, listar_clientes, actualizar_cliente, eliminar_cliente

class TestCrudCliente(unittest.TestCase):
    def setUp(self):
        clientes.clear()
        self.cliente = Cliente("Juan Pérez", "1234567890")
        clientes.append(self.cliente)

    @patch('builtins.input', side_effect=["María López", "0987654321"])
    def test_crear_cliente(self, mock_input):
        crear_cliente()
        self.assertEqual(len(clientes), 2)
        self.assertEqual(clientes[1].nombre, "María López")

    def test_listar_clientes(self):
        with patch('sys.stdout') as fake_stdout:
            listar_clientes()
            self.assertIn("Juan Pérez", fake_stdout.getvalue())

    @patch('builtins.input', side_effect=["1234567890", "Carlos Pérez"])
    def test_actualizar_cliente(self, mock_input):
        actualizar_cliente()
        self.assertEqual(clientes[0].nombre, "Carlos Pérez")

    @patch('builtins.input', side_effect=["1234567890"])
    def test_eliminar_cliente(self, mock_input):
        eliminar_cliente()
        self.assertEqual(len(clientes), 0)

#ejcutar esta prueba usando el comando "python -m unittest discover"
