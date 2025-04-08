from modelo.Producto import Productos
from datetime import datetime

class ControlFertilizantes(Productos):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, ultima_aplicacion):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.set_frecuencia_aplicacion(frecuencia_aplicacion)
        self.set_ultima_aplicacion(ultima_aplicacion)

    def set_frecuencia_aplicacion(self, frecuencia):
        if isinstance(frecuencia, int) and frecuencia > 0:
            self.frecuencia_aplicacion = frecuencia
        else:
            raise ValueError("La frecuencia de aplicación debe ser un número entero positivo de días")

    def set_ultima_aplicacion(self, fecha):
        try:
            self.ultima_aplicacion = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("La fecha debe estar en formato YYYY-MM-DD")

    def dias_desde_ultima_aplicacion(self):
        return (datetime.now().date() - self.ultima_aplicacion).days

    def __str__(self):
        return f"Control Fertilizantes: {self.nombre}, Precio: ${self.precio}, Registro ICA: {self.registro_ica}, " \
               f"Frecuencia: cada {self.frecuencia_aplicacion} días, Última Aplicación: {self.ultima_aplicacion}"
