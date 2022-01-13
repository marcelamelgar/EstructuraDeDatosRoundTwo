# Marcela Melgar
# 20200487

# Practice 1

def sumNnumbers(n):
    suma = 0

    while n > 0:
        suma = n + suma
        n = n - 1
        
    return suma

n = int(input("ingrese el valor de N: \n"))
operacion = (sumNnumbers(n))

print(f"los primeros {n} numeros, suman una cantidad de {operacion}")