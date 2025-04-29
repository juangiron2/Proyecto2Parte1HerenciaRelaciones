import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Modelo.Producto import Productos

class Antibiotico(Productos):
    def __init__(self, nombre, precio, dosis, tipo_animal):
        super().__init__(nombre, precio)
        self.set_dosis(dosis)
        self.set_tipo_animal(tipo_animal)

    def set_dosis(self, dosis):
        if 400 <= dosis <= 600:
            self.dosis = dosis
        else:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg")

    def set_tipo_animal(self, tipo_animal):
        tipos_validos = ["Bovino", "Caprino", "Porcino"]
        if tipo_animal in tipos_validos:
            self.tipo_animal = tipo_animal
        else:
            raise ValueError(f"Tipo de animal no válido. Debe ser uno de: {', '.join(tipos_validos)}")

    def __str__(self):
        return f"Antibiótico: {self.nombre}, Precio: ${self.precio}, Dosis: {self.dosis}Kg, Animal: {self.tipo_animal}"
