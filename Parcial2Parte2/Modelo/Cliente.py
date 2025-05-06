# Modelo/Cliente.py

class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = []

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_facturas(self):
        return self.__facturas

    def agregar_factura(self, factura):
        self.__facturas.append(factura)

    def __str__(self):
        return f"Cliente: {self.__nombre}, Cédula: {self.__cedula}"
