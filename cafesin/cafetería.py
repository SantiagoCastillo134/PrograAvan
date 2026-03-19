class Persona:
    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
    def login(self):
        return self.nombre + " inició sesión"
    def actualizar_perfil(self, nuevo_email):
        self.email = nuevo_email

class Cliente(Persona):
    def __init__(self, id_persona, nombre, email):
        super().__init__(id_persona, nombre, email)
        self.puntos_fidelidad = 0
        self.historial_pedidos = []

    def realizar_pedido(self, pedido):
        self.historial_pedidos.append(pedido)
    def consultar_historial(self):
        return self.historial_pedidos
    def canjear_puntos(self, puntos):
        if puntos <= self.puntos_fidelidad:
            self.puntos_fidelidad -= puntos
            return True
        return False

class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, id_empleado, rol):
        super().__init__(id_persona, nombre, email)
        self.id_empleado = id_empleado
        self.rol = rol

    def actualizar_inventario(self, inventario, ingrediente, cantidad):
        inventario.reducir_stock(ingrediente, cantidad)

    def cambiar_estado_pedido(self, pedido, nuevo_estado):
        pedido.estado = nuevo_estado

class ProductoBase:
    def __init__(self, id_producto, nombre, precio_base):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_base = precio_base

class Bebida(ProductoBase):
    def __init__(self, id_producto, nombre, precio_base, tamaño, temperatura):
        super().__init__(id_producto, nombre, precio_base)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = []

    def agregar_extra(self, extra):
        self.modificadores.append(extra)
    def calcular_precio_final(self):
        extras = len(self.modificadores) * 5
        return self.precio_base + extras

class Postre(ProductoBase):
    def __init__(self, id_producto, nombre, precio_base, es_vegano, sin_gluten):
        super().__init__(id_producto, nombre, precio_base)
        self.es_vegano = es_vegano
        self.sin_gluten = sin_gluten

class Pedido:
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.productos = []
        self.estado = "PENDIENTE"
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
    def calcular_total(self):
        total = 0
        for p in self.productos:
            if isinstance(p, Bebida):
                total += p.calcular_precio_final()
            else:
                total += p.precio_base
        self.total = total
        return total
    def validar_stock(self, inventario):
        for ingrediente in inventario.ingredientes:
            if inventario.ingredientes[ingrediente] <= 0:
                return False
        return True

class Inventario:
    def __init__(self):
        self.ingredientes = {}
    def agregar_ingrediente(self, nombre, cantidad):
        self.ingredientes[nombre] = cantidad
    def reducir_stock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes:
            self.ingredientes[ingrediente] -= cantidad
            if self.ingredientes[ingrediente] < 0:
                self.notificar_faltante(ingrediente)
    def notificar_faltante(self, ingrediente):
        print("Falta ingrediente:", ingrediente)