class Usuario:
    def __init__(self, id_usuario, nombre, apellido, cargo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido} {self.cargo}"

    def __str__(self):
        return f"ID: {self.id_usuario}, Nombre: {self.obtener_nombre_completo()}"


class Tarea:
    def __init__(self, id_tarea, descripcion, nombre_usuario_asignado, fecha_entrega, id_usuario_asignado=None, estado="pendiente"):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.nombre_usuario_asignado = nombre_usuario_asignado
        self.fecha_entrega = fecha_entrega
        self.id_usuario_asignado = id_usuario_asignado
        self.estado = estado

    def marcar_completada(self):
        self.estado = "completada"
        print(f"Tarea '{self.descripcion}' (ID: {self.id_tarea}) marcada como completada.")

    def asignar_usuario(self, id_usuario):
        self.id_usuario_asignado = id_usuario
        print(f"Tarea '{self.descripcion}' (ID: {self.id_tarea}) asignada al Usuario ID: {id_usuario}.")

    def __str__(self):
        asignado_str = f"Asignado a ID: {self.id_usuario_asignado}" if self.id_usuario_asignado else "Sin asignar"
        return f"ID Tarea: {self.id_tarea}, Descripción: '{self.descripcion}', Estado: {self.estado}, {asignado_str}"


class UsuarioRegular(Usuario):
    def __init__(self, id_usuario, nombre, apellido, cargo):
        super().__init__(id_usuario, nombre, apellido, cargo)

    def ver_info(self):
        print(f"[Usuario Regular] {self.nombre} {self.apellido} - Cargo: {self.cargo}")


class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, apellido, cargo):
        super().__init__(id_usuario, nombre, apellido, cargo)

    def ver_info(self):
        print(f"[Administrador] {self.nombre} {self.apellido} - Cargo: {self.cargo}")