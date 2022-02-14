from dataclasses import dataclass

@dataclass
class puntoTomado:
    x : float
    y : float
    n : int=0

def giveCuadrant(x,y):
    if (x > 0 and y > 0):
        n = 1
        return n
    elif (x < 0 and y > 0):
        n = 2
        return n
    elif (x < 0 and y < 0):
        n = 3
        return n
    elif (x > 0 and y < 0):
        n = 4
        return n
    else:
        n = 0
        return n

x = float(input("ingrese el valor de la coordenada x: "))
y = float(input("ingrese el valor de la coordenada y: "))
cuadrante = giveCuadrant(x,y)
punto = puntoTomado(x,y,cuadrante)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f'X: {punto.x}\nY: {punto.y}\nCUADRANTE: {punto.n}')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")