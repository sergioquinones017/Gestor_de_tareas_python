"""
=========================================
Proyecto: Gestor de Tareas

Autor: Sergio Quiñones

Descripción:
Primer proyecto desarrollado en Python.
Permite agregar, visualizar, completar,
eliminar y guardar tareas.

Versión: 1.0
=========================================
"""
tareas = []

# ===== MENÚ PRINCIPAL =====
while True:
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tareas")
    print("3. Marcar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    # ===== VER TAREAS =====
    if opcion == "1":
        print("\n ===== MIS TAREAS =====")
        if len(tareas) == 0:
            print("No hay tareas registradas.")
        else:
            for tarea in tareas:
                print(tarea)

    # ===== AGREGAR TAREA =====
    elif opcion == "2":
        tarea = input("Escriba la nueva tarea: ")
        tareas.append(tarea)
        print("Tarea agregada con exito.")
        
    # ===== MARCAR TAREA =====
    elif opcion == "3":
        print("\n===== MARCAR TAREA COMO COMPLETADA =====")

        if len(tareas) == 0:
            print("No hay tareas registradas.")

        else:
            for numero, tarea in enumerate(tareas, 1):
                print(numero, tarea)
            numero = input("Ingrese la tarea completada ")
            completada = int(numero)
            tareas[completada - 1] = "COMPLETADA " + tareas[completada - 1]
            print("Tarea marcada exitosamente. ")
 
    # ===== ELIMINAR TAREA =====   
    elif opcion =="4":
        print("Que tarea deseas eliminar")
        for numero, tarea in enumerate(tareas):
            print(numero, tarea)
        numero = input("Ingrese la tarea que desea eliminar ")
        numeros = int(numero)
        tareas.pop(numeros)
        print("Tarea eliminada con éxito")
    # ===== SALIR Y GUARDAR =====
    elif opcion == "5":
        guardar = input("¿Desea guardar las tareas antes de salir? (s/n): ")

        if guardar.lower() == "s":
            archivo = open("tareas.txt", "w")
            for tarea in tareas:
                archivo.write(tarea + "\n")
            archivo.close()

        print("Tareas guardadas correctamente.")

        print("¡Hasta luego!")
        break
    else:
        print("Esta opción aún no esta disponible")