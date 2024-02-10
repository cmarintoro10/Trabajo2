import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "computadora", "algoritmo", "inteligencia"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def ahorcado():
    palabra_a_adivinar = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra:")
    print(mostrar_tablero(palabra_a_adivinar, letras_adivinadas))

    while True:
        if intentos == 0:
            print("¡Perdiste! La palabra era:", palabra_a_adivinar)
            break

        if "_" not in mostrar_tablero(palabra_a_adivinar, letras_adivinadas):
            print("¡Felicidades! ¡Ganaste!")
            break

        letra = input("Ingresa una letra: ").lower()

        if letra in palabra_a_adivinar:
            if letra not in letras_adivinadas:
                letras_adivinadas.append(letra)
                print("¡Letra correcta!")
            else:
                print("Ya has ingresado esa letra.")
        else:
            print("Letra incorrecta. Pierdes un intento.")
            intentos -= 1

        print("Intentos restantes:", intentos)
        print(mostrar_tablero(palabra_a_adivinar, letras_adivinadas))

if __name__ == "__main__":
    ahorcado()
