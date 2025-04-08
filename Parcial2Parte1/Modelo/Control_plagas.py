from modelo.Producto import Productos

class ControlPlagas(Productos):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.set_frecuencia_aplicacion(frecuencia_aplicacion)
        self.set_periodo_carencia(periodo_carencia)

    def set_frecuencia_aplicacion(self, frecuencia):
        if isinstance(frecuencia, int) and frecuencia > 0:
            self.frecuencia_aplicacion = frecuencia
        else:
            raise ValueError("La frecuencia de aplicación debe ser un número entero positivo de días")

    def set_periodo_carencia(self, periodo):
        if isinstance(periodo, int) and periodo >= 0:
            self.periodo_carencia = periodo
        else:
            raise ValueError("El periodo de carencia debe ser un número entero no negativo de días")

    def __str__(self):
        return f"Control Plagas: {self.nombre}, Precio: ${self.precio}, Registro ICA: {self.registro_ica}, " \
               f"Frecuencia: cada {self.frecuencia_aplicacion} días, Periodo de carencia: {self.periodo_carencia} días"
