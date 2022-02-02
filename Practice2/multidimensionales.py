import numpy as np
import os

compras = []
pagos = []
uni  = []
num = []
nam = []
cost = []
puni = []
pnum = []
mult = []
x = 1
y = 1

def menu():
    os.system('clear')
    print("\t1. comprar items")
    print("\t2. pagar items")
    print("\t3. ver recibo de compra")
    print("\t4. ver recibo de pagos")
    print("\t5. calcular el saldo pendiente")
    print("\t6. precio promedio por producto")
    print("\t7. precio del producto mas caro")
    print("\t8. recibo de compra con pagos ingresados")
    print("\t9. eliminar pagos")

def regresoMenu():
    input("pulsa enter para regresar al menu principal\n")

def Promedio(cuenta):
    return np.sum(cuenta) / cuenta.size

while True:
    menu()
    opcion = int(input("\ningrese una opcion del menu: "))

    if(opcion == 1):
        os.system('clear')
        print("CATALOGO: \n")
        productos = np.array(['naranja', 'fresas', 'uvas', 'moras', 'sandia', 'papaya'])
        codigo = np.array([123, 234, 345, 456, 567, 678])
        precio = np.array([2.25, 5.99, 12.35, 8.45, 18.25, 10.5])

        catalogo  = np.array([productos, codigo, precio])

        for i in catalogo:
            for j in i:
                print(j, end = "\t|")
            print()


        print("\nCOMPRAR ITEMS\n")
        cant = int(input("ingrese la cantidad de productos que desea comprar, minimo 10.\n"))
        
        if(cant < 10):
            cant = int(input("ingrese un valor minimo de 10: \n"))

        while(x <= cant):
            com = int(input(f"ingrese el codigo del producto {x}: "))
            uni.append(com)
            find = np.where(codigo == com)
            value = productos[(find)]
            nam.append(value)
            costo = precio[(find)]
            cost.append(costo)
            amount = int(input(f"ingrese la cantidad que desea comprar: "))
            num.append(amount)
            tiplica = costo * amount
            mult.append(tiplica)
            compras = [nam, mult]
            x += amount
        
        nam = np.array(nam)
        cost = np.array(cost)
        compras = np.array(compras)
        mult = np.array(mult)
        print("Su compra ha sido registrada!\n")
        regresoMenu()

    elif(opcion == 2):
        os.system('clear')
        print("PAGOS DE ITEMS\n")
        cant = int(input("ingrese la cantidad de pagos que desea realizar, minimo 5.\n"))
        
        if(cant < 5):
            cant = int(input("ingrese un valor minimo de 5: \n"))

        while(y <= cant):
            pag = float(input(f"ingrese la cantidad del pago {y}: "))
            puni.append(pag)
            metodo = input("ingrese el metodo de pago: ")
            pnum.append(metodo)
            pagos  = [puni, pnum]
            y += 1
        
        puni = np.array(puni)
        pnum = np.array(pnum)
        pagos = np.array(pagos)
        print("Los pagos han sido registrados!\n")
        regresoMenu()

    elif(opcion == 3):
        os.system('clear')
        print("SUMA DE COMPRAS")
        print(f"\nLa suma total de la compra es: {np.sum(mult)}\n")
        regresoMenu()

    elif(opcion == 4):
        os.system('clear')
        print("SUMA DE PAGOS")
        print(f"\nLa suma total de pagos es: {np.sum(puni)}\n")
        regresoMenu()

    elif(opcion == 5):
        os.system('clear')
        saldo = np.sum(mult) - np.sum(puni)
        print("SALDO POR PAGAR\n")
        print(f"El saldo a pagar es: {round(saldo,2)}\n")
        regresoMenu()

    elif(opcion == 6):
        os.system('clear')
        print("PROMEDIO DE PRECIOS COMPRADOS\n")
        promedio =  Promedio(cost)
        print(f"El promedio de precios por productos comprados es: {round(promedio,2)}\n")
        regresoMenu()

    elif(opcion == 7):
        os.system('clear')
        print("PRODUCTO MAS CARO COMPRADO\n")
        mayor = np.max(cost)
        ver = np.where(cost == mayor)
        val = nam[(ver)]
        for i in range(val.size):
            print(f"El producto mas caro es grande es: {val[i]} \ntiene un precio de: {np.max(cost)}\n\n")
        regresoMenu()

    elif(opcion == 8):
        os.system('clear')
        print("RECIBO DE COMPRA\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("compras:\n")
        for i in compras:
            for j in i:
                print(j, end = "\t")
            print()
        print(f"\t\ttotal: {np.sum(mult)}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("pagos:\n")
        for i in pagos:
            for j in i:
                print(j, end = "\t")
            print()
        print(f"\t\ttotal: {np.sum(puni)}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        regresoMenu()

    elif(opcion == 9):
        os.system('clear')
        print("\tPAGOS")
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(puni.size):
            print(f"\t{puni[j]}")

        print("\nSE ELIMINA EL PAGO\n")
        salir = 's'

        while (salir == 's'):
    
            borrar = float(input("elimine el pago 2 o el pago 4, presionando el monto: "))
            puni = np.delete(puni, np.where(puni == borrar))

            print("----------------------------------------")
            print("Total Compras: ")
            print(f"{np.sum(mult)}\n")
            print("Total Pagos: ")
            print(f"{np.sum(puni)}\n")
            print("Saldo: ")
            saldo = np.sum(mult) - np.sum(puni)
            print(f"{round(saldo,2)}\n")
            print("Promedio Precio Productos: ")
            promedio =  Promedio(cost)
            print(f"{round(promedio,2)}\n")
            print("Producto mas caro\n")
            mayor = np.max(cost)
            ver = np.where(cost == mayor)
            val = nam[(ver)]
            for i in range(val.size):
                print(f"El producto mas caro es grande es: {val[i]} \ntiene un precio de: {np.max(cost)}\n\n")
            print("Estado de Cuenta:\n")
            print("\tCompras")
            print("~~~~~~~~~~~~~~~~~~~~~")
            for i in range(mult.size):
                print(f"\t{mult[i]}\n")
            print("\n\tPagos")
            print("~~~~~~~~~~~~~~~~~~~~~")
            for j in range(puni.size):
                print(f"\t{puni[j]}\n")

            print("----------------------------------------")

            salir = input("si desea continuar eliminando presione 's'\nsi ya no desea eliminar otro credito, presione 'n'\n")

        regresoMenu()