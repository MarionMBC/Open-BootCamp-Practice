class Operaciones:
    PI = 3.14151921 
    def suma (self, a, b):
        return a+b
    def resta (self, a, b):
        return a-b
    def como_me_llamo (self):
        return print(__name__)
    def nombre (self):
        if __name__ == 'operaciones':
            return print ('Hola, soy el módulo', __name__)
            
