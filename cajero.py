# ==========================
# CAJERO AUTOMÁTICO
# Samuel Salcedo
# ==========================

saldo = 100000

while True:

    print("\n==========================")
    print("     CAJERO AUTOMÁTICO")
    print("==========================")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"\nSu saldo actual es: ${saldo}")

    elif opcion == "2":

        deposito = float(input("Ingrese el valor a depositar: "))

        saldo = saldo + deposito

        print(f"\nDepósito realizado correctamente.")
        print(f"Nuevo saldo: ${saldo}")

    elif opcion == "3":

        print("\nGracias por utilizar el cajero.")
        break

    else:

        print("\nOpción no válida.")