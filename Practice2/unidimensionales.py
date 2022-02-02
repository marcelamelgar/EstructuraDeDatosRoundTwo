import os
import numpy as np
import cProfile

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

def ingresoDebitos(debitos):
    debitos = np.array(debitos)
    return(debitos)

def ingresoCreditos(creditos):
    creditos = np.array(creditos)
    return(creditos)

def sumDebitos(debitos):
    return(np.sum(debitos))

def sumCreditos(creditos):
    return(np.sum(creditos))

def getSaldo(creditos, debitos):
    return(saldo)

def getPromedio(debitos):
    return(promedio)

def getMax(debitos):
    return(np.max(debitos))

def operaciones(debitos, creditos):
    return(debitos.size, creditos.size)

def getEstado(debitos, creditos):
    for i in range(debitos.size):
        return(f"\t{debitos[i]}\n")
    for j in range(creditos.size):
        return(f"\t{creditos[j]}\n")



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
        
        ingresoDebitos(debitos)
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
        
        ingresoCreditos(creditos)
        print("Los creditos han sido registrados!\n")
        regresoMenu()

    elif(opcion == 3):
        os.system('clear')
        print("SUMA DE DEBITOS")
        print(f"\nLa suma total de debitos es: {np.sum(debitos)}\n")
        sumDebitos(ingresoDebitos(debitos))
        regresoMenu()

    elif(opcion == 4):
        os.system('clear')
        print("SUMA DE CREDITOS")
        print(f"\nLa suma total de creditos es: {np.sum(creditos)}\n")
        sumCreditos(ingresoCreditos(creditos))
        regresoMenu()

    elif(opcion == 5):
        os.system('clear')
        saldo = np.sum(creditos) - np.sum(debitos)
        print("SALDO\n")
        print(f"El saldo es: {saldo}\n")
        getSaldo(ingresoCreditos(creditos),ingresoDebitos(debitos))
        regresoMenu()

    elif(opcion == 6):
        os.system('clear')
        print("PROMEDIO DE DEBITOS\n")
        promedio =  Promedio(ingresoDebitos(debitos))
        print(f"El promedio de los debitos es: {round(promedio,2)}\n")
        getPromedio(ingresoDebitos(debitos))
        regresoMenu()

    elif(opcion == 7):
        os.system('clear')
        print("MONTO MAYOR DE DEBITOS\n")
        print(f"El monto en debitos mas grande es: {np.max(ingresoDebitos(debitos))}\n")
        getMax(ingresoDebitos(debitos))
        regresoMenu()

    elif(opcion == 8):
        os.system('clear')
        print("OPERACIONES REALIZADAS\n")
        print(f"debitos: {ingresoDebitos(debitos).size}")
        print(f"creditos: {ingresoCreditos(creditos).size}\n")
        operaciones(ingresoDebitos(debitos),ingresoCreditos(creditos))
        regresoMenu()

    elif(opcion == 9):
        os.system('clear')
        print("ESTADO DE CUENTA\n")
        print("\tDebitos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for i in range(ingresoDebitos(debitos).size):
            print(f"\t{ingresoDebitos(debitos)[i]}\n")
        print("\n\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(ingresoCreditos(creditos).size):
            print(f"\t{ingresoCreditos(creditos)[j]}\n")
        getEstado(ingresoDebitos(debitos), ingresoCreditos(creditos))
        regresoMenu()

    elif(opcion == 10):
        os.system('clear')
        print("\tCreditos")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(ingresoCreditos(creditos).size):
            print(f"\t{ingresoCreditos(creditos)[j]}")

        print("\nSE ELIMINA CREDITO\n")
        salir = 's'

        while (salir == 's'):
    
            borrar = float(input("ingrese el monto del credito que quiere eliminar: "))
            creditos = np.delete(ingresoCreditos(creditos), np.where(ingresoCreditos(creditos) == borrar))
            ingresoCreditos(creditos)

            print("----------------------------------------")
            print("Total Debitos: ")
            print(f"{np.sum(ingresoDebitos(debitos))}\n")
            print("Total Creditos: ")
            print(f"{np.sum(ingresoCreditos(creditos))}\n")
            print("Saldo: ")
            saldo = np.sum(ingresoCreditos(creditos)) - np.sum(ingresoDebitos(debitos))
            print(f"{saldo}\n")
            print("Promedio Debitos: ")
            promedio =  Promedio(ingresoDebitos(debitos))
            print(f"{round(promedio,2)}\n")
            print("Debito Mayor\n")
            print(f"{np.max(ingresoDebitos(debitos))}\n")
            print("Estado de Cuenta:\n")
            print("\tDebitos")
            print("~~~~~~~~~~~~~~~~~~~~~")
            for i in range(ingresoDebitos(debitos).size):
                print(f"\t{ingresoDebitos(debitos)[i]}\n")
            print("\n\tCreditos")
            print("~~~~~~~~~~~~~~~~~~~~~")
            for j in range(ingresoCreditos(creditos).size):
                print(f"\t{ingresoCreditos(creditos)[j]}\n")

            print("----------------------------------------")

            salir = input("si desea continuar eliminando presione 's'\nsi ya no desea eliminar otro credito, presione 'n'\n")

        regresoMenu()