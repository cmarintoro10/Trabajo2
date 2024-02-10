class RegistroGastos:
    def __init__(self):
        self.gastos = {}

    def agregar_gasto(self, categoria, monto):
        if categoria in self.gastos:
            self.gastos[categoria] += monto
        else:
            self.gastos[categoria] = monto

    def calcular_total(self):
        return sum(self.gastos.values())

    def generar_informe(self):
        print("Informe de gastos:")
        for categoria, monto in self.gastos.items():
            print(f"{categoria}: ${monto}")

    def establecer_presupuesto(self, categoria, presupuesto):
        if categoria in self.gastos:
            if presupuesto >= self.gastos[categoria]:
                print("Presupuesto establecido correctamente.")
            else:
                print("El presupuesto es menor que el gasto actual.")
        else:
            print("La categoría no tiene gastos registrados.")

def main():
    registro = RegistroGastos()

    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar gasto")
        print("2. Calcular total de gastos")
        print("3. Generar informe de gastos")
        print("4. Establecer presupuesto")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            categoria = input("Ingrese la categoría del gasto: ")
            monto = float(input("Ingrese el monto del gasto: "))
            registro.agregar_gasto(categoria, monto)
            print("Gasto agregado correctamente.")
        elif opcion == "2":
            total = registro.calcular_total()
            print(f"El total de gastos es: ${total}")
        elif opcion == "3":
            registro.generar_informe()
        elif opcion == "4":
            categoria = input("Ingrese la categoría para establecer el presupuesto: ")
            presupuesto = float(input("Ingrese el presupuesto: "))
            registro.establecer_presupuesto(categoria, presupuesto)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
