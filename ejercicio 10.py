class JuegoPreguntas:
    def __init__(self):
        self.preguntas = {
            "Ciencia": [
                {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "respuesta": "Júpiter"},
                {"pregunta": "¿Quién descubrió la penicilina?", "respuesta": "Alexander Fleming"},
                {"pregunta": "¿Cuál es el símbolo químico del oro?", "respuesta": "Au"}
            ],
            "Historia": [
                {"pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?", "respuesta": "1939"},
                {"pregunta": "¿Quién fue el primer presidente de Estados Unidos?", "respuesta": "George Washington"},
                {"pregunta": "¿Cuál fue el primer imperio mesopotámico?", "respuesta": "Imperio Sumerio"}
            ],
            "Geografía": [
                {"pregunta": "¿Cuál es el río más largo del mundo?", "respuesta": "Amazonas"},
                {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "París"},
                {"pregunta": "¿En qué continente se encuentra la Cordillera de los Andes?", "respuesta": "Sudamérica"}
            ]
        }

    def seleccionar_pregunta(self, categoria):
        if categoria in self.preguntas:
            return self.preguntas[categoria].pop(0)
        else:
            return None

def main():
    juego = JuegoPreguntas()

    print("Bienvenido al Juego de Preguntas y Respuestas")

    while True:
        print("\nSeleccione una categoría:")
        print("1. Ciencia")
        print("2. Historia")
        print("3. Geografía")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "4":
            print("¡Hasta luego!")
            break
        elif opcion not in ["1", "2", "3"]:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            continue

        categoria = None
        if opcion == "1":
            categoria = "Ciencia"
        elif opcion == "2":
            categoria = "Historia"
        elif opcion == "3":
            categoria = "Geografía"

        pregunta = juego.seleccionar_pregunta(categoria)
        if pregunta:
            texto_pregunta = pregunta["pregunta"]
            respuesta = pregunta["respuesta"]
            respuesta_usuario = input(f"{texto_pregunta}: ").strip()
            if respuesta_usuario.lower() == respuesta.lower():
                print("¡Respuesta correcta!")
            else:
                print(f"Respuesta incorrecta. La respuesta correcta es: {respuesta}")
        else:
            print("No hay más preguntas disponibles en esta categoría.")

if __name__ == "__main__":
    main()
