class Cine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos_disponibles = [[True] * columnas for _ in range(filas)]

    def mostrar_disponibilidad(self):
        print("Disponibilidad de asientos:")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.asientos_disponibles[i][j]:
                    print("O", end=" ")
                else:
                    print("X", end=" ")
            print()

    def seleccionar_asiento(self, fila, columna):
        if 1 <= fila <= self.filas and 1 <= columna <= self.columnas:
            if self.asientos_disponibles[fila - 1][columna - 1]:
                print(f"El asiento {fila}{columna} ha sido reservado.")
                self.asientos_disponibles[fila - 1][columna - 1] = False
            else:
                print("Lo siento, ese asiento ya está reservado.")
        else:
            print("Asiento fuera de rango. Por favor, seleccione un asiento válido.")

def main():
    cine = Cine(filas=5, columnas=10)

    while True:
        print("\nSeleccione una opción:")
        print("1. Mostrar disponibilidad de asientos")
        print("2. Reservar asiento")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            cine.mostrar_disponibilidad()
        elif opcion == "2":
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))
            cine.seleccionar_asiento(fila, columna)
        elif opcion == "3":
            print("¡Gracias por usar el sistema de reservas de cine!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
