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
    print("\n" + "=" * 40)
    print("      GESTOR DE TAREAS v1.0")
    print("=" * 40)

    print("1. 📋 Ver tareas")
    print("2. ➕ Agregar tarea")
    print("3. ✅ Marcar tarea")
    print("4. 🗑️ Eliminar tarea")
    print("5. 🚪 Salir")

    print("=" * 40)
    
def guardar_tareas():
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")


    
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
        if len(tareas) == 0:
            print("\n" + "=" * 40)
            print("           MIS TAREAS")
            print("=" * 40)
            print("No hay tareas registradas.")
            print("=" * 40)
        else:
            print("\n" + "=" * 40)
            print("           MIS TAREAS")
            print("=" * 40)

            for numero, tarea in enumerate(tareas, 1):
                print(f"{numero}. {tarea}")

            print("=" * 40)

    # ===== AGREGAR TAREA =====
    elif opcion == "2":
        nueva_tarea = input("Ingrese la nueva tarea: ")

        if nueva_tarea.strip() == "":
            print("❌ La tarea no puede estar vacía.")
        else:
            tareas.append("[ ] " + nueva_tarea)
            guardar_tareas()
            print(f"✅ '{nueva_tarea}' agregada correctamente.")

        # ===== MARCAR TAREA =====
    elif opcion == "3":
        print("\n" + "=" * 40)
        print("           MARCAR TAREA")
        print("=" * 40)

        if len(tareas) == 0:
            print("No hay tareas registradas.")
            print("=" * 40)
            continue

        for numero, tarea in enumerate(tareas, 1):
            print(f"{numero}. {tarea}")

        print("=" * 40)

        numero = input("Ingrese el número de la tarea completada: ")

        if not numero.isdigit():
            print("❌ Debe ingresar un número.")
            continue

        completada = int(numero)

        if completada < 1 or completada > len(tareas):
            print("❌ Esa tarea no existe.")
            continue

        tarea = tareas[completada - 1]

        if tarea.startswith("[x]"):
            print("⚠️ Esa tarea ya está completada.")
        else:
            tareas[completada - 1] = tarea.replace("[ ]", "[x]", 1)
            guardar_tareas()
            print("✅ Tarea marcada como completada.")
            
    # ===== ELIMINAR TAREA =====
    elif opcion == "4":

        if len(tareas) == 0:
            print("No hay tareas registradas.")
            continue

        print("\n" + "=" * 40)
        print("          ELIMINAR TAREA")
        print("=" * 40)

        for numero, tarea in enumerate(tareas, 1):
            print(f"{numero}. {tarea}")

        numero = input("Ingrese el número de la tarea que desea eliminar: ")

        if not numero.isdigit():
            print("❌ Debe ingresar un número.")
            continue

        numero = int(numero)

        if numero < 1 or numero > len(tareas):
            print("❌ Esa tarea no existe.")
            continue

        tarea_eliminada = tareas.pop(numero - 1)
        guardar_tareas()

        print(f"✅ '{tarea_eliminada}' eliminada correctamente.")   

    # ===== SALIR Y GUARDAR =====
    elif opcion == "5":
        print("\n" + "=" * 40)
        print(" Gracias por usar Gestor de Tareas")
        print("          Versión 1.0")
        print("=" * 40)
        break
    else:
        print("Esta opción aún no esta disponible")