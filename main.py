class Auto:
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
            for Asiento in self.asientos:
                if isinstance(Asiento, asientos):
                    numeroAsientos += 1
            return(cantidadAsientos)

        def verificarIdentidad(self,):
            if self.motor != self.registro:
                return "Las piezas no son originales"
            elif self.asientos != self.registro:
                return "Las piezas no son originales"
            else:
                return "Auto original"
            return verificarIdentidad

class Asiento:
    def __innit__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

        def cambiarColor(self, colores):
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
            self.tipo = tipo
            if tipo == "electrico" or "combustible":
                asignarTipo
