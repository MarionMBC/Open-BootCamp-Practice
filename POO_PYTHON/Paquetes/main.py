import P1.operaciones as op
import pprint
var1 = 3

def test():
    global var1
    var1 = 4
    perro = 3
    print(locals())



if __name__ == '__main__':
    test()
    perro = 5



def suma (a,b):
    return a+b

def resta (a,b):
    return a-b
