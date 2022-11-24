class animal:
    _edad = 25

    def modEdad(self, edad):
        self._edad = edad

    def printEdad(self):
        print(self._edad)


animal1 = animal()
animal1.modEdad(30)
animal1.printEdad()


class perro():
    raza = "PitBull"

    def perro(raza):
        perro.raza = raza

    def perroPrint():
        print(perro.raza)


perro.perro("Rot")
perro.perroPrint()


class persona:
    nombre = '',
    apellido = '',

    def printNombre(self):
        print(f'Su nombre es: {self.nombre} {self.apellido}')


class empleado(persona):
    codEmpleado = 0

    def __init__(self):
        persona.__init__(self)
        print("Estoy en la clase hija")


empleado1 = empleado()

empleado1.nombre = "Marion"
empleado1.apellido = "Bustamante"
empleado1.codEmpleado = "dev87"
empleado1.printNombre()


class destructor():
    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre
        print("Hola, soy el constructor: ", self.nombre)

    def __del__(self):
        print("Hola, soy el destructor: ", self.nombre)


_encendido = False


def enciende():
    print("Hola")
    global _encendido
    _encendido = True


def apaga():
    global _encendido
    _encendido = False


def isEncendido():
    return _encendido


diccionario = {
    '_encendido': False,
    'enciende': enciende,
    'apaga': apaga
}

apaga()
diccionario['enciende']()


# Clases compuestas >>Has A<<

class Puerta:
    cantidadPuertas = 5


class Cuarto:
    ventanas = 0
    focos = 0
    Muebles = ''  # Incluye adornos


class Dormitorio (Cuarto):
    nombre = "Habitación"
    cantCamas = 0



class Casa:
    puertas = Puerta()
    Dormitorios = Dormitorio()


casa1 = Casa()
casa1.Dormitorios.Muebles = ["2 lámparas", "1 Cama", "1 closet"]
casa1.Dormitorios.nombre = "Cuarto de invitados"

print(casa1.Dormitorios.Muebles)
print(casa1.Dormitorios.nombre)


