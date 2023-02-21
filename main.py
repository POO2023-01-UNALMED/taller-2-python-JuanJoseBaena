class Auto:
    cantidadCreados = 0
    def __innit__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

        def cantidadAsientos(self, cantidadAsientos):
            numeroAsientos = 0
            for asiento in self.asientos:
                if isinstance(asiento, asientos):
                    numeroAsientos += 1
            return cantidadAsientos

        def verificarIdentidad(self):
            for asiento in self.asientos:
                if asiento != None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"

            if self.motor.registro != self.registro:
                return "Las piezas no son originales"
            
            return "Auto original"

class Asiento:
    def __innit__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color
        return cambiarColor

class Motor:
    def __innit__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

        def cambiarRegistro (self, registro):
            self.registro = registro

        def asignarTipo (self, tipo):
            tipos = ["electrico", "gasolina"]
            if tipo in tipos:
                self.tipos = tipo

