# Read or write
# f = open ('texto.txt','r+')   # Read
# data = f.read()
# print(data)
# data = f.write("Este es el texto")
# print(data)
# f.close()
import pprint


def leerArchivo():
    file = open(
        'C:\\Users\\MELCHISEDEC\\Desktop\\UNAH\\III PAC - 2022\\BASE DE DATOS II\\II UNIDAD\\REPORTES\\REPORTES DE '
        'CLIENTES\\r_clientes.txt',
        'r')
    datos = file.readlines()
    info = ''
    idUsuarios = []
    for elemento in range(1, len(datos)):
        info = datos[elemento].split(',')
        idUsuarios.append(info[0])
    pprint.pprint(idUsuarios)


if __name__ == '__main__':
    leerArchivo()
