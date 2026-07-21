# ==========================
# CAJERO AUTOMÁTICO
# Samuel Salcedo y Yimer Obando
# ==========================

saldo = 100000
historial = []

while True:

    print("\n==========================")
    print("     CAJERO AUTOMÁTICO")
    print("==========================")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        print(f"\nSu saldo actual es: ${saldo}")

    elif opcion == "2":

        deposito = float(input("Ingrese el valor a depositar: "))
        saldo += deposito

        print("\nDepósito realizado correctamente.")
        print(f"Nuevo saldo: ${saldo}")

    elif opcion == "3":

        retiro = float(input("Ingrese el valor a retirar: "))

        if retiro <= saldo:
            saldo -= retiro
            historial.append(f"Retiro: ${retiro}")
            print("Retiro realizado correctamente.")
            print(f"Saldo actual: ${saldo}")
        else:
            print("Saldo insuficiente.")

    elif opcion == "4":

        print("\n===== HISTORIAL =====")

        if len(historial) == 0:
            print("No existen movimientos.")
        else:
            for movimiento in historial:
                print(movimiento)

    elif opcion == "5":

        print("\nGracias por utilizar el cajero.")
        break

    else:

        print("\nOpción no válida.")