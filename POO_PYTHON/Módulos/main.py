import operaciones 
import datetime
import sys
sys.path.append('C:\\Users\\MELCHISEDEC\\Desktop\\new_module')
sys.path.append('C:\\Users\\MELCHISEDEC\\Desktop\\Open Bootcamp\\Open-BootCamp-Practice\\POO_PYTHON\\Módulos\\package_p1')
import mod1
import paquetes
import package_p1.saludos as saludos
print(sys.path)

op = operaciones.Operaciones()

def hola ():
    return print(__name__)


def sortList(list):
    for i in range (len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] > list[j]:
                list[j] = list[i]
                list[i] = list[j]
    return list


if __name__ == '__main__':
    # print ("Este es el main")
    # print(op.suma(1,2))
    # print(op.resta(2,3))
    # op.como_me_llamo()
    # hola()
    # op.nombre()
    # print(op.PI)
    # print(datetime.date.today())
    # print (saludos.hola())
    # print (__name__)
    # mod1.printModule()
    list = [2,3,4,5,2,1,7]
    print(sortList(list))

    paquetes.printPaquetes()
    print (dir(paquetes.printPaquetes()))




