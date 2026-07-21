saldo = 100000
historial = []

while True:
    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1. Retirar dinero")
    print("2. Ver historial")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        retiro = float(input("Ingrese el valor a retirar: "))

        if retiro <= saldo:
            saldo -= retiro
            historial.append(f"Retiro: ${retiro}")
            print(f"Retiro exitoso. Saldo actual: ${saldo}")
        else:
            print("Saldo insuficiente.")

    elif opcion == "2":
        print("\n===== HISTORIAL =====")

        if len(historial) == 0:
            print("No existen movimientos.")
        else:
            for movimiento in historial:
                print(movimiento)

    elif opcion == "3":
        print("Gracias por utilizar el cajero.")
        break

    else:
        print("Opción inválida.")