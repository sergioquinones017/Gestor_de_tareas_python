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
def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    
tareas = []

try:
    with open("tareas.txt", "r") as archivo:
        for linea in archivo:
            tareas.append(linea.strip())

except FileNotFoundError:
    pass

# ===== MENÚ PRINCIPAL =====
while True:
    mostrar_menu()

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

            numero = input("Ingrese el número de la tarea completada: ")

            if not numero.isdigit():
                print("❌ Debe ingresar un número.")
                continue

            completada = int(numero)

            if completada < 1 or completada > len(tareas):
                print("❌ Esa tarea no existe.")
                continue

            tareas[completada - 1] = "✅ COMPLETADA - " + tareas[completada - 1]

            print("✅ Tarea marcada exitosamente.")

    # ===== ELIMINAR TAREA =====
    elif opcion == "4":

        if len(tareas) == 0:
            print("No hay tareas registradas.")
            continue

        print("\n===== ELIMINAR TAREA =====")

        for numero, tarea in enumerate(tareas, 1):
            print(numero, tarea)

        numero = input("Ingrese el número de la tarea que desea eliminar: ")

        if not numero.isdigit():
            print("❌ Debe ingresar un número.")
            continue

        numero = int(numero)

        if numero < 1 or numero > len(tareas):
            print("❌ Esa tarea no existe.")
            continue

        tarea_eliminada = tareas.pop(numero - 1)

        print(f"✅ '{tarea_eliminada}' eliminada correctamente.")   

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