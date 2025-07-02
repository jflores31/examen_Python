from gestion_datos import (
    registrar_usuario, mostrar_usuarios, buscar_usuario_por_id,
    registrar_tarea, mostrar_tareas, buscar_tarea_por_id,
    actualizar_tarea, eliminar_tarea
)

def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("      BIENVENIDO AL ORGANIZADOR DE TAREAS      ")
    print("=" * 50)
    print("  1️⃣  Gestión de Usuarios")
    print("  2️⃣  Gestión de Tareas")
    print("  3️⃣  Salir del Programa")
    print("-" * 50)

def mostrar_menu_usuarios():
    print("\n" + "-" * 50)
    print("              Gestión de Usuarios             ")
    print("-" * 50)
    print("  1  📝 Registrar nuevo usuario")
    print("  2  📋 Mostrar todos los usuarios")
    print("  3  🔙 Volver al menú principal")
    print("-" * 50)

def mostrar_menu_tareas():
    print("\n" + "-" * 50)
    print("               Gestión de Tareas              ")
    print("-" * 50)
    print("  1  📝 Registrar nueva tarea")
    print("  2  📋 Mostrar todas las tareas")
    print("  3  🔍 Mostrar tareas pendientes")
    print("  4  🔄 Actualizar tarea")
    print("  5  ✅ Marcar tarea como completada")
    print("  6  ❌ Eliminar tarea")
    print("  7  🔙 Volver al menú principal")
    print("-" * 50)

def gestionar_usuarios():
    while True:
        mostrar_menu_usuarios()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n" + ("---- Registro de nuevo usuario ----").center(50))
            nombre = input("Ingrese nombre del usuario: ")
            apellido = input("Ingrese apellido del usuario: ")
            cargo = input("Ingrese el cargo del usuario: ")
            
            if nombre and apellido and cargo:
                registrar_usuario(nombre, apellido, cargo)
            else:
                print("Error: El nombre y el apellido no pueden estar vacíos.")

        elif opcion == '2':
            mostrar_usuarios()

        elif opcion == '3':
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def gestionar_tareas():   #FULL MANEJO DE ERRORES!!! PABAJO
    while True:
        mostrar_menu_tareas()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n" + ("---- Registro de nueva tarea ----").center(50))
            descripcion = input("Ingrese descripción de la tarea: ")
            fecha_tarea = input("Ingrese la fecha de entrega (ejemplo: 31/12): ")
            
            if not descripcion or not fecha_tarea:
                print("Error: La descripción de la tarea no puede estar vacía.")
                continue

            id_usuario_str = input("Ingrese ID del usuario a asignar (deje vacío si no asigna): ")
            id_usuario = None

            if id_usuario_str:
                try:
                    id_usuario = int(id_usuario_str)
                    if not buscar_usuario_por_id(id_usuario):
                        print(f"Advertencia: Usuario con ID {id_usuario} no encontrado. La tarea se registrará sin asignar.")
                        id_usuario = None
                except ValueError:
                    print("Error: El ID del usuario debe ser un número entero. Tarea registrada sin asignar.")
                    id_usuario = None

            registrar_tarea(descripcion, id_usuario, fecha_tarea)

        elif opcion == '2':
            mostrar_tareas(mostrar_completadas=True)

        elif opcion == '3':
            mostrar_tareas(mostrar_completadas=False)

        elif opcion == '4':
            print("\n" + ("---- Actualizar tarea ----").center(50))
            try: 
                id_tarea_str = input("Ingrese el ID de la tarea a actualizar: ")
                id_tarea = int(id_tarea_str)
            except ValueError:
                print("Error: El ID de la tarea debe ser un número entero.")
                continue

            tarea_encontrada = buscar_tarea_por_id(id_tarea)
            if not tarea_encontrada:
                print(f"Error: No se encontró una tarea con el ID {id_tarea}.")
                continue

            print(f"Tarea actual: {tarea_encontrada}")
            print("Deje vacío el campo que no desee actualizar.")

            nueva_descripcion = input("Nueva descripción (deje vacío para no cambiar): ")
            nuevo_id_usuario_str = input("Nuevo ID de usuario a asignar (deje vacío para no cambiar): ")
            nuevo_estado = input("Nuevo estado ('pendiente' o 'completada', deje vacío para no cambiar): ").lower()

            actualizar_params = {}

            if nueva_descripcion:
                actualizar_params["nueva_descripcion"] = nueva_descripcion
            
            if nuevo_id_usuario_str:
                try:
                    nuevo_id_usuario = int(nuevo_id_usuario_str)
                    actualizar_params["nuevo_id_usuario_asignado"] = nuevo_id_usuario
                except ValueError:
                    print("Advertencia: El ID del nuevo usuario debe ser un número entero. No se actualizará la asignación.")
            
            if nuevo_estado:
                if nuevo_estado in ["pendiente", "completada"]:
                    actualizar_params["nuevo_estado"] = nuevo_estado
                else:
                    print("Advertencia: Estado no válido. Debe ser 'pendiente' o 'completada'. No se actualizará el estado.")

            if actualizar_params:
                actualizar_tarea(id_tarea, **actualizar_params)
            else:
                print("No se proporcionaron datos para actualizar.")


        elif opcion == '5':
            print("\n" + ("---- Marcar Tarea como Completada ----").center(50))
            try:
                id_tarea_str = input("Ingrese el ID de la tarea a marcar como completada: ")
                id_tarea = int(id_tarea_str)
            except ValueError:
                print("Error: El ID de la tarea debe ser un número entero.")
                continue

            tarea = buscar_tarea_por_id(id_tarea)
            if tarea:
                tarea.marcar_completada()
            else:
                print(f"Error: Tarea con ID {id_tarea} no encontrada.")

        elif opcion == '6':
            print("\n" + ("---- Eliminar tarea ----").center(50))
            try:
                id_tarea_str = input("Ingrese el ID de la tarea a eliminar: ")
                id_tarea = int(id_tarea_str)
            except ValueError:
                print("Error: El ID de la tarea debe ser un número entero.")
                continue

            eliminar_tarea(id_tarea)

        elif opcion == '7':
            print("\n" + ("---- Volviendo al menú principal... ----").center(50))
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("👉 Elige una opción (1-3): ")

        if opcion_principal == '1':
            gestionar_usuarios()
        elif opcion_principal == '2':
            gestionar_tareas()
        elif opcion_principal == '3':
            print("\n" + ("¡Gracias por usar el Organizador de Tareas! ¡Hasta pronto!").center(50))
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()