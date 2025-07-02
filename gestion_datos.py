from clases import Usuario, Tarea, Administrador, UsuarioRegular

lista_usuarios = []
lista_tareas = []
registro_tareas_por_usuario = {} #dicci




def registrar_usuario(nombre, apellido, cargo):
    id_nuevo = generar_id_usuario()

    if cargo.lower() == "administrador":
        nuevo_usuario = Administrador(id_nuevo, nombre, apellido, cargo)
    else:
        nuevo_usuario = UsuarioRegular(id_nuevo, nombre, apellido, cargo)

    lista_usuarios.append(nuevo_usuario)
    print(f"Usuario '{nuevo_usuario.obtener_nombre_completo()}' registrado con ID: {id_nuevo}.")
    return nuevo_usuario

def generar_id_usuario():
    if not lista_usuarios:
        return 7777
    return max(usuario.id_usuario for usuario in lista_usuarios) + 1


def mostrar_usuarios():
    if not lista_usuarios:
        print("\n--- No hay usuarios registrados aún. ---")
        return

    print("\n--- Listado de Usuarios ---")
    for usuario in lista_usuarios:
        print(f"- {usuario}")

def buscar_usuario_por_id(id_usuario):
    for usuario in lista_usuarios:
        if usuario.id_usuario == id_usuario:
            return usuario
    return None

def generar_id_tarea():
    if not lista_tareas:
        return 101
    return max(tarea.id_tarea for tarea in lista_tareas) + 1

def registrar_tarea(descripcion, id_usuario_asignado, fecha_entrega): #modi para dicci
    usuario = buscar_usuario_por_id(id_usuario_asignado)
    if usuario:
        id_nueva_tarea = generar_id_tarea()
        nueva_tarea = Tarea(id_nueva_tarea, descripcion, usuario.nombre, fecha_entrega, id_usuario_asignado=usuario.id_usuario)
        lista_tareas.append(nueva_tarea)
        
        if usuario.nombre not in registro_tareas_por_usuario:  #acá va guardar dicci
            registro_tareas_por_usuario[usuario.nombre] = []
        registro_tareas_por_usuario[usuario.nombre].append(descripcion)

        print(f"Tarea '{descripcion}' registrada con ID: {id_nueva_tarea}, asignada a {usuario.nombre}.")
        return nueva_tarea
    else:
        print(f"No se encontró un usuario con ID {id_usuario_asignado}.")
        return None

#LA RECURSIVIDAAAAAAD!!!!!!
def mostrar_tareas(mostrar_completadas=True, indice=0):
    if indice >= len(lista_tareas):
        return

    tarea = lista_tareas[indice]

    if not mostrar_completadas and tarea.estado == "completada":
        mostrar_tareas(mostrar_completadas, indice + 1)
        return

    info_usuario = ""
    if tarea.id_usuario_asignado:
        usuario = buscar_usuario_por_id(tarea.id_usuario_asignado)
        if usuario:
            info_usuario = f" (Asignada a: {usuario.obtener_nombre_completo()})"
        else:
            info_usuario = " (Usuario asignado no encontrado)"

    if indice == 0:
        print("\n---  Listado de Tareas  ---") #1 vez y muestra en recursivo demás


    print(f"- ID Tarea: {tarea.id_tarea}, Descripción: '{tarea.descripcion}', Estado: {tarea.estado}{info_usuario}")

    mostrar_tareas(mostrar_completadas, indice + 1)


def buscar_tarea_por_id(id_tarea):
    for tarea in lista_tareas:
        if tarea.id_tarea == id_tarea:
            return tarea
    return None

def actualizar_tarea(id_tarea, nueva_descripcion=None, nuevo_id_usuario_asignado=None, nuevo_estado=None):
    tarea = buscar_tarea_por_id(id_tarea)
    if not tarea:
        print(f"Error: Tarea con ID {id_tarea} no encontrada para actualizar.")
        return False

    actualizado = False

    if nueva_descripcion is not None:
        tarea.descripcion = nueva_descripcion
        print(f"Descripción de la tarea {id_tarea} actualizada.")
        actualizado = True
    
    if nuevo_id_usuario_asignado is not None:
        if buscar_usuario_por_id(nuevo_id_usuario_asignado):
            tarea.id_usuario_asignado = nuevo_id_usuario_asignado
            print(f"Usuario asignado a la tarea {id_tarea} actualizado a ID {nuevo_id_usuario_asignado}.")
            actualizado = True
        else:
            print(f"Error: No se pudo asignar. Usuario con ID {nuevo_id_usuario_asignado} no existe.")
    
    if nuevo_estado is not None:
        if nuevo_estado in ["pendiente", "completada"]:
            tarea.estado = nuevo_estado
            print(f"Estado de la tarea {id_tarea} actualizado a '{nuevo_estado}'.")
            actualizado = True
        else:
            print(f"Error: Estado '{nuevo_estado}' no válido. Debe ser 'pendiente' o 'completada'.")
    
    if actualizado:
        print(f"Tarea {id_tarea} actualizada exitosamente.")
    else:
        print(f"No se realizaron cambios en la tarea {id_tarea}.")
    return actualizado

def eliminar_tarea(id_tarea):
    tarea_a_eliminar = None
    for tarea in lista_tareas:
        if tarea.id_tarea == id_tarea:
            tarea_a_eliminar = tarea
            break

    if tarea_a_eliminar:
        lista_tareas.remove(tarea_a_eliminar)
        print(f"Tarea '{tarea_a_eliminar.descripcion}' (ID: {id_tarea}) eliminada exitosamente.")
        return True
    else:
        print(f"Error: Tarea con ID {id_tarea} no encontrada para eliminar.")
        return False
    
#para mostar dicci
def mostrar_diccionario_usuarios_y_tareas():
    print("\n--- Registro de Tareas por Usuario  ---")
    for nombre, tareas in registro_tareas_por_usuario.items():
        print(f"{nombre}:")
        for t in tareas:
            print(f"  - {t}") 