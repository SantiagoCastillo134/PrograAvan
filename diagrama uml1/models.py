class Persona:
    def __init__(self, id_persona, nombre, email, telefono):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        print(f"{self.nombre} ha iniciado sesión")

    def logout(self):
        print(f"{self.nombre} ha cerrado sesión")

    def actualizar_datos(self, email, telefono):
        self.email = email
        self.telefono = telefono
        print("datos actualizados correctamente")

class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        return f"ID: {self.id}, {self.nombre}, (${self.precio}), {self.categoria}"
    
class Usuario(Persona):
    def __init__(self, id_persona, nombre, email, telefono):
        super().__init__(id_persona, nombre, email, telefono)
        self.puntos_fidelidad = 0
        self.historial_reservas = []

    def crear_reserva(self, reserva):
        self.historial_reservas.append(reserva)
        print(f"Reserva creada para {self.nombre}")

    def cancelar_reserva(self, reserva):
        reserva.estado = "CANCELADA"
        print("Reserva cancelada.")


class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, telefono, id_empleado, rol):
        super().__init__(id_persona, nombre, email, telefono)
        self.id_empleado = id_empleado
        self.rol = rol
        self.horario = "No definido"

    def marcar_entrada(self):
        print(f"Empleado {self.nombre} marcó entrada.")

    def gestionar_funciones(self):
        if self.rol == "ADMIN":
            print("Gestionando funciones...")
        else:
            print("No tienes permisos para gestionar funciones")


class Espacio:
    def __init__(self, id_espacio, nombre, ubicacion):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def limpiar_espacio(self):
        print(f"El espacio {self.nombre} fue limpiado.")


class Sala(Espacio):
    def __init__(self, id_espacio, nombre, ubicacion, tipo, capacidad_total):
        super().__init__(id_espacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidad_total = capacidad_total
        self.asientos_ocupados = []

    def calcular_asientos_libres(self):
        libres = self.capacidad_total - len(self.asientos_ocupados)
        print(f"Asientos libres: {libres}")
        return libres

    def ocupar_asiento(self, asiento):
        if asiento in self.asientos_ocupados:
            print("El asiento ya está ocupado")
        else:
            self.asientos_ocupados.append(asiento)
            print(f"Asiento {asiento} ocupado correctamente.")


class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtener_detalles(self):
        print(f"{self.titulo} , {self.genero} , {self.duracion} min")


class Funcion:
    def __init__(self, id_funcion, pelicula, sala, horario, precio_base):
        self.id_funcion = id_funcion
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario
        self.precio_base = precio_base

    def obtener_detalles_funcion(self):
        print(f"Función de {self.pelicula.titulo} en sala {self.sala.nombre} a las {self.horario}")


class Promocion:
    def __init__(self, codigo, descripcion, porcentaje_descuento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentaje_descuento = porcentaje_descuento

    def aplicar_descuento(self, monto):
        descuento = monto * self.porcentaje_descuento
        total = monto - descuento
        print(f"Descuento aplicado. Total final: {total}")
        return total


class Reserva:
    def __init__(self, id_reserva, usuario, funcion, asientos):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.estado = "PENDIENTE"
        self.monto_total = 0

    def calcular_total(self):
        self.monto_total = len(self.asientos) * self.funcion.precio_base
        print(f"Total a pagar: {self.monto_total}")
        return self.monto_total

    def confirmar_pago(self):
        for asiento in self.asientos:
            if asiento in self.funcion.sala.asientos_ocupados:
                print(f"El asiento {asiento} ya está ocupado")
                return

        for asiento in self.asientos:
            self.funcion.sala.ocupar_asiento(asiento)

        self.estado = "PAGADA"
        print("Reserva confirmada y pagada.")


