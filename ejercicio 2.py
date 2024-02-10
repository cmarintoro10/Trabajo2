def longitud():
    opcion = int(input("Selecciona la unidad de longitud a convertir:\n1. Metros\n2. Pies\n3. Pulgadas\nOpción: "))
    valor = float(input("Ingresa el valor a convertir: "))

    if opcion == 1:
        pies = valor * 3.28084
        pulgadas = valor * 39.3701
        print(f"{valor} metros equivalen a {pies} pies y {pulgadas} pulgadas.")
    elif opcion == 2:
        metros = valor * 0.3048
        pulgadas = valor * 12
        print(f"{valor} pies equivalen a {metros} metros y {pulgadas} pulgadas.")
    elif opcion == 3:
        metros = valor * 0.0254
        pies = valor * 0.0833333
        print(f"{valor} pulgadas equivalen a {metros} metros y {pies} pies.")
    else:
        print("Opción no válida.")


def masa():
    opcion = int(input("Selecciona la unidad de masa a convertir:\n1. Kilogramos\n2. Libras\n3. Onzas\nOpción: "))
    valor = float(input("Ingresa el valor a convertir: "))

    if opcion == 1:
        libras = valor * 2.20462
        onzas = valor * 35.274
        print(f"{valor} kilogramos equivalen a {libras} libras y {onzas} onzas.")
    elif opcion == 2:
        kilogramos = valor * 0.453592
        onzas = valor * 16
        print(f"{valor} libras equivalen a {kilogramos} kilogramos y {onzas} onzas.")
    elif opcion == 3:
        kilogramos = valor * 0.0283495
        libras = valor * 0.0625
        print(f"{valor} onzas equivalen a {kilogramos} kilogramos y {libras} libras.")
    else:
        print("Opción no válida.")


def temperatura():
    opcion = int(input("Selecciona la unidad de temperatura a convertir:\n1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\nOpción: "))
    valor = float(input("Ingresa el valor a convertir: "))

    if opcion == 1:
        fahrenheit = valor * 9/5 + 32
        print(f"{valor} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
    elif opcion == 2:
        celsius = (valor - 32) * 5/9
        print(f"{valor} grados Fahrenheit equivalen a {celsius} grados Celsius.")
    else:
        print("Opción no válida.")


def main():
    print("Bienvenido al Conversor de Unidades")
    while True:
        print("\nSelecciona la opción deseada:")
        print("1. Longitud")
        print("2. Masa")
        print("3. Temperatura")
        print("4. Salir")
        opcion = int(input("Opción: "))

        if opcion == 1:
            longitud()
        elif opcion == 2:
            masa()
        elif opcion == 3:
            temperatura()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
