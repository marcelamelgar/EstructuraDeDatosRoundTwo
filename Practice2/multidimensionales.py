import numpy as np


def reciboCompra():
    productos = ['naranja', 'fresas', 'uvas', 'moras', 'sandia', 'papaya']
    productos = np.array(productos)
    codigo = [123, 234, 345, 456, 567, 678]
    codigo = np.array(codigo)
    precio = [2.25, 5.99, 12.35, 8.45, 18.25, 10.5]
    precio = np.array(precio)

    catalogo  = [productos, codigo, precio]
    catalogo = np.array(catalogo)

    for i in catalogo:
        for j in i:
            print(j, end = "\t")
        print()


while True:
    reciboCompra()   
    input("pulsa enter para regresar al menu principal\n") 