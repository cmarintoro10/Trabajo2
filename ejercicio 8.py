import random

def obtener_datos_simulados():
    temperatura = round(random.uniform(10, 30), 2)  # Temperatura en grados Celsius
    humedad = round(random.uniform(30, 90), 2)  # Humedad relativa en porcentaje
    velocidad_viento = round(random.uniform(0, 20), 2)  # Velocidad del viento en km/h
    descripcion = random.choice(["Despejado", "Parcialmente nublado", "Nublado", "Lluvia ligera", "Lluvia intensa", "Tormenta"])  # Descripción del tiempo
    return temperatura, humedad, velocidad_viento, descripcion

def mostrar_informacion(temperatura, humedad, velocidad_viento, descripcion):
    print("Información meteorológica simulada:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Humedad: {humedad}%")
    print(f"Velocidad del viento: {velocidad_viento} km/h")
    print(f"Descripción: {descripcion}")

def main():
    print("Bienvenido al Simulador de Tiempo")
    ubicacion = input("Ingrese la ubicación para obtener información meteorológica simulada: ")

    # Obtenemos datos simulados
    temperatura, humedad, velocidad_viento, descripcion = obtener_datos_simulados()

    # Mostramos la información
    mostrar_informacion(temperatura, humedad, velocidad_viento, descripcion)

if __name__ == "__main__":
    main()
