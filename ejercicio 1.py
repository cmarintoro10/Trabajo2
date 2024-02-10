# Crear una lista vacía para almacenar las tareas
tareas = []

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = input("Ingrese la tarea que desea agregar: ")
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

# Función para editar una tarea en la lista
def editar_tarea():
    tarea = input("Ingrese la tarea que desea editar: ")
    if tarea in tareas:
        nueva_tarea = input("Ingrese la nueva tarea: ")
        indice = tareas.index(tarea)
        tareas[indice] = nueva_tarea
        print("Tarea editada con éxito.")
    else:
        print("La tarea no se encontró en la lista.")

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    tarea = input("Ingrese la tarea que desea eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada con éxito.")
    else:
        print("La tarea no se encontró en la lista.")

# Función para mostrar todas las tareas en la lista
def mostrar_tareas():
    print("Lista de tareas:")
    for tarea in tareas:
        print("- " + tarea)

# Función para agregar la fecha de vencimiento a una tarea
def agregar_fecha_vencimiento():
    tarea = input("Ingrese la tarea a la que desea agregar la fecha de vencimiento: ")
    if tarea in tareas:
        fecha = input("Ingrese la fecha de vencimiento (en formato dd/mm/aaaa): ")
        indice = tareas.index(tarea)
        tareas[indice] += " - Fecha de vencimiento: " + fecha
        print("Fecha de vencimiento agregada con éxito.")
    else:
        print("La tarea no se encontró en la lista.")

# Función para agregar la prioridad a una tarea
def agregar_prioridad():
    tarea = input("Ingrese la tarea a la que desea agregar la prioridad: ")
    if tarea in tareas:
        prioridad = input("Ingrese la prioridad (alta, media o baja): ")
        indice = tareas.index(tarea)
        tareas[indice] += " - Prioridad: " + prioridad
        print("Prioridad agregada con éxito.")
    else:
        print("La tarea no se encontró en la lista.")

# Menú principal
while True:
    print("\nBienvenido al Gestor de Tareas (To-Do List)")
    print("1. Agregar tarea")
    print("2. Editar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar tareas")
    print("5. Agregar fecha de vencimiento")
    print("6. Agregar prioridad")
    print("7. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        editar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        mostrar_tareas()
    elif opcion == "5":
        agregar_fecha_vencimiento()
    elif opcion == "6":
        agregar_prioridad()
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
