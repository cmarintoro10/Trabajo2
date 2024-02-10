def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    print("Bienvenido al Conversor de Monedas")
    moneda_origen = input("Ingrese la moneda de origen: ")
    moneda_destino = input("Ingrese la moneda de destino: ")
    monto = float(input(f"Ingrese el monto en {moneda_origen}: "))

    if moneda_origen == moneda_destino:
        print("Las monedas de origen y destino son iguales. No es necesario realizar una conversión.")
    else:
        tasa_cambio = float(input(f"Ingrese la tasa de cambio de {moneda_origen} a {moneda_destino}: "))
        monto_convertido = convertir_moneda(monto, tasa_cambio)
        print(f"{monto} {moneda_origen} equivalen a {monto_convertido} {moneda_destino}.")

if __name__ == "__main__":
    main()
