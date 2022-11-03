# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada
# Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos
# para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = ""
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def isApproved(self):
        return "aprobó" if self.nota>=7 else"reprobó"

    def __str__(self):
        print(f'El alumno: {self.nombre} {self.isApproved()} la clase con una calificación de {self.nota}.')


Alumno1 = Alumno("Marion Bustamante", 7)

Alumno1.__str__()