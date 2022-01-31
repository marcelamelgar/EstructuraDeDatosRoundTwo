import os
import numpy as np

debitos = []
creditos = []
x = 1
y = 1

#menu
def menu():
    os.system('clear')
    print("\t1. ingresar debitos")
    print("\t2. ingresar creditos")
    print("\t3. calcular total de debitos")
    print("\t4. calcular total de creditos")
    print("\t5. calcular el saldo")
    print("\t6. calcular el promedio de debitos")
    print("\t7. mostrar el debito mas grande")
    print("\t8. conteo de operaciones")
    print("\t9. estado de cuenta")
    print("\t10. eliminar credito")

def regresoMenu():
    input("pulsa enter para regresar al menu principal\n")

def Promedio(cuenta):
    return sum(cuenta) / len(cuenta)

while True:
    menu()

    opcion = int(input("\ningrese una opcion del menu: "))

    if(opcion == 1):
        os.system('clear')
        print("INGRESO DE DEBITOS")
        cant = int(input("ingrese la cantidad de debitos que desea registrar, minimo 10.\n"))
        
        if(cant < 10):
            cant = int(input("ingrese un valor minimo de 10: "))

        while(x <= cant):
            deb = float(input(f"ingrese el debito {x}: "))
            debitos.append(deb)
            x += 1
        
        print("Los debitos han sido registrados!\n")

        regresoMenu()

    elif(opcion == 2):
        os.system('clear')
        print("INGRESO DE CREDITOS")
        cant = int(input("ingrese la cantidad de creditos que desea registrar, minimo 5.\n"))
        
        if(cant < 5):
            cant = int(input("ingrese un valor minimo de 5: "))

        while(y <= cant):
            cred = float(input(f"ingrese el credito {y}: "))
            creditos.append(cred)
            y += 1
        
        print("Los creditos han sido registrados!\n")
        regresoMenu()

    elif(opcion == 3):
        os.system('clear')
        print("SUMA DE DEBITOS")
        print(f"\nLa suma total de debitos es: {sum(debitos)}\n")
        regresoMenu()

    elif(opcion == 4):
        os.system('clear')
        print("SUMA DE CREDITOS")
        print(f"\nLa suma total de creditos es: {sum(creditos)}\n")
        regresoMenu()

    elif(opcion == 5):
        os.system('clear')
        saldo = sum(creditos) - sum(debitos)
        print("SALDO")
        print(f"El saldo es: {saldo}")
        regresoMenu()

    elif(opcion == 6):
        os.system('clear')
        print("PROMEDIO DE DEBITOS")
        promedio =  Promedio(debitos)
        print(f"El promedio de los debitos es: {round(promedio,2)}")
        regresoMenu()

    elif(opcion == 7):
        os.system('clear')
        print("MONTO MAYOR DE DEBITOS")
        print(f"El monto en debitos mas grande es: {max(debitos)}")
        regresoMenu()

    elif(opcion == 8):
        os.system('clear')
        print("OPERACIONES REALIZADAS")
        print(f"debitos: {len(debitos)}")
        print(f"creditos: {len(creditos)}")
        regresoMenu()

    elif(opcion == 9):
        os.system('clear')
        print("ESTADO DE CUENTA")
        print("\tDebitos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for i in range(len(debitos)):
            print(f"\t{debitos[i]}\n")
        print("\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(len(creditos)):
            print(f"\t{creditos[j]}\n")
        regresoMenu()

    elif(opcion == 10):
        os.system('clear')
        print("\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(len(creditos)):
            print(f"\t{creditos[j]}")

        print("SE ELIMINA CREDITO")
        borrar = float(input("ingrese el monto del credito que quiere eliminar: "))
        creditos.remove(borrar)
        
        regresoMenu()