def agregar_registro(banco_de_datos):
    nombre = input("Ingrese el nombre del registro: ")
    edad = input("Ingrese la edad del registro: ")
    banco_de_datos[nombre] = edad
    print("Registro agregado con éxito.")


def actualizar_registro(banco_de_datos):
    nombre = input("Ingrese el nombre del registro que desea actualizar: ")
    if nombre in banco_de_datos:
        nueva_edad = input("Ingrese la nueva edad: ")
        banco_de_datos[nombre] = nueva_edad
        print("Registro actualizado con éxito.")
    else:
        print("Registro no encontrado.")


def eliminar_registro(banco_de_datos):
    nombre = input("Ingrese el nombre del registro que desea eliminar: ")
    if nombre in banco_de_datos:
        del banco_de_datos[nombre]
        print("Registro eliminado con éxito.")
    else:
        print("Registro no encontrado.")


def buscar_registro(banco_de_datos):
    nombre = input("Ingrese el nombre del registro que desea buscar: ")
    if nombre in banco_de_datos:
        print(f"Edad de {nombre}: {banco_de_datos[nombre]}")
    else:
        print("Registro no encontrado.")


def mostrar_registros(banco_de_datos):
    print("Registros en el banco de datos:")
    for nombre, edad in banco_de_datos.items():
        print(f"{nombre}: {edad}")


def main():
    banco_de_datos = {}
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar registro")
        print("2. Actualizar registro")
        print("3. Eliminar registro")
        print("4. Buscar registro")
        print("5. Mostrar registros")
        print("6. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_registro(banco_de_datos)
        elif opcion == "2":
            actualizar_registro(banco_de_datos)
        elif opcion == "3":
            eliminar_registro(banco_de_datos)
        elif opcion == "4":
            buscar_registro(banco_de_datos)
        elif opcion == "5":
            mostrar_registros(banco_de_datos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
