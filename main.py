class Auto:
    cantidadCreados = 0
    def __innit__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

        def cantidadAsientos(self):
            count=0
            for i in self.asientos:
                if i !=None:
                    count +=1
            return count
            #numeroAsientos = 0
            #for asiento in self.asientos:
                #if type (asiento)==Asiento:
                    #numeroAsientos += 1
            #return numeroAsientos

        def verificarIntegridad(self):
            if (self.registro==self.motor.registro):
                return "Las piezas no son originales"
            for i in range(len(self.asientos)):
                if self.asientos[i] !=None and self.asientos[i].registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
                #for asiento in self.asientos:
                    #if type(asiento)==Asiento:
                        #if asiento.registro !=self.registro:
                            #return "Las piezas no son originales"
                #return "Auto original"
            #else:
                #return "Las piezas no son originales"


            #for asiento in self.asientos:
                #if asiento != None:
                    #if asiento.registro != self.registro:
                    #return "Las piezas no son originales"
                        
            #if self.motor.registro != self.registro:
                #return "Las piezas no son originales"
            
            #return "Auto original"

class Asiento:
    def __innit__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        #if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            #self.color=color
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color.lower() in colores:
            self.color = color
        #if color in colores:
            #self.color = color

class Motor:
    def __innit__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

        def cambiarRegistro (self, registro):
            self.registro = registro

        def asignarTipo (self, tipo):
            #if (tipo=="electrico" or tipo=="gasolina"):
                #self.tipo=tipo
            tipos = ["electrico", "gasolina"]
            if tipo.lower() in tipos:
                self.tipos = tipo

#Version 4.5