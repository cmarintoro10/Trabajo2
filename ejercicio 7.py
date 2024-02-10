import random

# Listas de personajes, lugares y eventos
personajes = ["el héroe", "la heroína", "el mago", "el villano", "la princesa", "el dragón"]
lugares = ["el castillo", "el bosque encantado", "la montaña nevada", "la ciudad perdida", "la cueva oscura"]
eventos = ["enfrentarse a", "descubrir un tesoro en", "escapar de", "salvar a", "derrotar a"]

# Función para generar un personaje aleatorio
def generar_personaje():
    return random.choice(personajes)

# Función para generar un lugar aleatorio
def generar_lugar():
    return random.choice(lugares)

# Función para generar un evento aleatorio
def generar_evento():
    return random.choice(eventos)

# Función para generar la historia
def generar_historia(personajes, lugares, eventos):
    historia = ""
    for i in range(len(personajes)):
        personaje = random.choice(personajes)
        lugar = random.choice(lugares)
        evento = random.choice(eventos)
        
        # Añadimos objetos directos a eventos que lo requieren
        if "enfrentarse a" in evento:
            objeto_directo = random.choice(["el malvado brujo", "el monstruo de las sombras", "el ejército de esqueletos"])
        elif "descubrir un tesoro en" in evento:
            objeto_directo = random.choice(["un cofre lleno de oro", "el amuleto mágico", "la espada legendaria"])
        elif "salvar a" in evento:
            objeto_directo = random.choice(["la princesa secuestrada", "el pueblo indefenso", "el reino en peligro"])
        elif "derrotar a" in evento:
            objeto_directo = random.choice(["el dragón de fuego", "la criatura ancestral", "el tirano malvado"])
        else:
            objeto_directo = "nada"

        historia += f"{personaje} llegó a {lugar} y tuvo que {evento} {objeto_directo}.\n"
    return historia


# Función para mostrar opciones al usuario
def mostrar_opciones():
    print("**Menú Generador de Historias**")
    print("1. Generar historia aleatoria")
    print("2. Elegir personajes")
    print("3. Elegir lugares")
    print("4. Elegir eventos")
    print("5. Salir")

# Función para elegir personajes
def elegir_personajes():
    personajes_elegidos = []
    while True:
        print("¿Cuántos personajes deseas elegir? (1-6)")
        numero_personajes = int(input())
        if 1 <= numero_personajes <= 6:
            break
        else:
            print("Número inválido. Ingrese un número entre 1 y 6.")

    for i in range(numero_personajes):
        print(f"Elige el personaje {i + 1}:")
        for j, personaje in enumerate(personajes):
            print(f"{j + 1}. {personaje}")
        eleccion = int(input())
        personajes_elegidos.append(personajes[eleccion - 1])

    return personajes_elegidos

# Función para elegir lugares
def elegir_lugares():
    lugares_elegidos = []
    while True:
        print("¿Cuántos lugares deseas elegir? (1-5)")
        numero_lugares = int(input())
        if 1 <= numero_lugares <= 5:
            break
        else:
            print("Número inválido. Ingrese un número entre 1 y 5.")

    for i in range(numero_lugares):
        print(f"Elige el lugar {i + 1}:")
        for j, lugar in enumerate(lugares):
            print(f"{j + 1}. {lugar}")
        eleccion = int(input())
        lugares_elegidos.append(lugares[eleccion - 1])

    return lugares_elegidos

# Función para elegir eventos
def elegir_eventos():
    eventos_elegidos = []
    while True:
        print("¿Cuántos eventos deseas elegir? (1-5)")
        numero_eventos = int(input())
        if 1 <= numero_eventos <= 5:
            break
        else:
            print("Número inválido. Ingrese un número entre 1 y 5.")

    for i in range(numero_eventos):
        print(f"Elige el evento {i + 1}:")
        for j, evento in enumerate(eventos):
            print(f"{j + 1}. {evento}")
        eleccion = int(input())
        eventos_elegidos.append(eventos[eleccion - 1])

    return eventos_elegidos

def main():
    global personajes, lugares, eventos  # Declarar las variables como globales
    personajes = ["el héroe", "la heroína", "el mago", "el villano", "la princesa", "el dragón"]
    lugares = ["el castillo", "el bosque encantado", "la montaña nevada", "la ciudad perdida", "la cueva oscura"]
    eventos = ["enfrentarse a", "descubrir un tesoro en", "escapar de", "salvar a", "derrotar a"]

    while True:
        mostrar_opciones()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            historia = generar_historia(personajes, lugares, eventos)
            print("\nAquí está tu historia:\n")
            print(historia)
        elif opcion == 2:
            personajes = elegir_personajes()
            historia = generar_historia(personajes, lugares, eventos)
            print("\nAquí está tu historia:\n")
            print(historia)
        elif opcion == 3:
            lugares = elegir_lugares()
            historia = generar_historia(personajes, lugares, eventos)
            print("\nAquí está tu historia:\n")
            print(historia)
        elif opcion == 4:
            eventos = elegir_eventos()
            historia = generar_historia(personajes, lugares, eventos)
            print("\nAquí está tu historia:\n")
            print(historia)
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
