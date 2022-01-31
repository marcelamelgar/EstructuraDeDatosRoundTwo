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
    return np.sum(cuenta) / cuenta.size

while True:
    menu()

    opcion = int(input("\ningrese una opcion del menu: "))

    if(opcion == 1):
        os.system('clear')
        print("INGRESO DE DEBITOS\n")
        cant = int(input("ingrese la cantidad de debitos que desea registrar, minimo 10.\n"))
        
        if(cant < 10):
            cant = int(input("ingrese un valor minimo de 10: \n"))

        while(x <= cant):
            deb = float(input(f"ingrese el debito {x}: "))
            debitos.append(deb)
            x += 1
        
        debitos = np.array(debitos)
        print("Los debitos han sido registrados!\n")

        regresoMenu()

    elif(opcion == 2):
        os.system('clear')
        print("INGRESO DE CREDITOS\n")
        cant = int(input("ingrese la cantidad de creditos que desea registrar, minimo 5.\n"))
        
        if(cant < 5):
            cant = int(input("ingrese un valor minimo de 5: \n"))

        while(y <= cant):
            cred = float(input(f"ingrese el credito {y}: "))
            creditos.append(cred)
            y += 1
        
        creditos = np.array(creditos)
        print("Los creditos han sido registrados!\n")
        regresoMenu()

    elif(opcion == 3):
        os.system('clear')
        print("SUMA DE DEBITOS")
        print(f"\nLa suma total de debitos es: {np.sum(debitos)}\n")
        regresoMenu()

    elif(opcion == 4):
        os.system('clear')
        print("SUMA DE CREDITOS")
        print(f"\nLa suma total de creditos es: {np.sum(creditos)}\n")
        regresoMenu()

    elif(opcion == 5):
        os.system('clear')
        saldo = np.sum(creditos) - np.sum(debitos)
        print("SALDO\n")
        print(f"El saldo es: {saldo}\n")
        regresoMenu()

    elif(opcion == 6):
        os.system('clear')
        print("PROMEDIO DE DEBITOS\n")
        promedio =  Promedio(debitos)
        print(f"El promedio de los debitos es: {round(promedio,2)}\n")
        regresoMenu()

    elif(opcion == 7):
        os.system('clear')
        print("MONTO MAYOR DE DEBITOS\n")
        print(f"El monto en debitos mas grande es: {np.max(debitos)}\n")
        regresoMenu()

    elif(opcion == 8):
        os.system('clear')
        print("OPERACIONES REALIZADAS\n")
        print(f"debitos: {debitos.size}")
        print(f"creditos: {creditos.size}\n")
        regresoMenu()

    elif(opcion == 9):
        os.system('clear')
        print("ESTADO DE CUENTA\n")
        print("\tDebitos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for i in range(debitos.size):
            print(f"\t{debitos[i]}\n")
        print("\n\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(creditos.size):
            print(f"\t{creditos[j]}\n")
        regresoMenu()

    elif(opcion == 10):
        os.system('clear')
        print("\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(creditos.size):
            print(f"\t{creditos[j]}")

        print("\nSE ELIMINA CREDITO\n")
    
        borrar = float(input("ingrese el monto del credito que quiere eliminar: "))
        creditos = np.delete(creditos, np.where(creditos == borrar))

        print("----------------------------------------")
        print("Total Debitos: ")
        print(f"{np.sum(debitos)}\n")
        print("Total Creditos: ")
        print(f"{np.sum(creditos)}\n")
        print("Saldo: ")
        saldo = np.sum(creditos) - np.sum(debitos)
        print(f"{saldo}\n")
        print("Promedio Debitos: ")
        promedio =  Promedio(debitos)
        print(f"{round(promedio,2)}\n")
        print("Debito Mayor\n")
        print(f"{np.max(debitos)}\n")
        print("Estado de Cuenta:\n")
        print("\tDebitos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for i in range(debitos.size):
            print(f"\t{debitos[i]}\n")
        print("\n\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(creditos.size):
            print(f"\t{creditos[j]}\n")

        print("----------------------------------------")

        regresoMenu()