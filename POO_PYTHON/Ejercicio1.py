# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


class Vehiculo:
    color = ""
    ruedas = 0

    def __int__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = None

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__int__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def printCoche(self):
        isCilindrada = "no"
        if self.cilindrada: isCilindrada = "sí"
        print(f'El color del coche es: {super().color}, tiene {super().ruedas}. Su velocidad es de {self.velocidad} y {isCilindrada} está cilindrada.')


Coche1 = Coche("Negro", 4, 240, True)

Coche1.printCoche()
