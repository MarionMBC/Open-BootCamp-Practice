class Operaciones:
    def suma (self, a, b):
        """Suma dos valores: a + b"""
        return a+b

    def resta (self, a, b):
        """Resta dos valores: a + b"""
        return a-b

    def multiplicación (self, a, b):
        """Multiplica dos valores: a + b"""
        return a*b

    def division (self, a, b):
        """Divide dos valores: a + b"""
        return "Syntax Error" if (b == 0) else a/b
