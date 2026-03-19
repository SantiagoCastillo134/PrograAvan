from cafetería import *

print("REGISTRO DE PRODUCTOS DE CAFETERIA")

b1 = Bebida(1, "Mocha", 50, "Grande", "CALIENTE")
b2 = Bebida(2, "Chocolate Caliente", 40, "Mediano", "CALIENTE")
b3 = Bebida(3, "Cafe Latte Vainilla", 48, "Grande", "CALIENTE")
b4 = Bebida(4, "Cold Brew", 45, "Grande", "FRIA")
b5 = Bebida(5, "Té Verde", 30, "Mediano", "CALIENTE")

p1 = Postre(6, "Pay de Limón", 35, False, False)
p2 = Postre(7, "Donas Glaseadas", 25, False, False)
p3 = Postre(8, "Muffin de Chocolate", 30, False, False)
p4 = Postre(9, "Pastel de Tres Leches", 55, False, False)
p5 = Postre(10, "Galleta Vegana", 28, True, False)


print(b1.nombre, "-", b1.precio_base)
print(b2.nombre, "-", b2.precio_base)
print(b3.nombre, "-", b3.precio_base)
print(b4.nombre, "-", b4.precio_base)
print(b5.nombre, "-", b5.precio_base)
print(p1.nombre, "-", p1.precio_base)
print(p2.nombre, "-", p2.precio_base)
print(p3.nombre, "-", p3.precio_base)
print(p4.nombre, "-", p4.precio_base)
print(p5.nombre, "-", p5.precio_base)

print("\nPRUEBA DE MODIFICADORES")

b1.agregar_extra("Leche deslactosada")
b1.agregar_extra("Extra chocolate")

print("Precio final cafe:", b1.calcular_precio_final())

print("\nPRUEBA DE PEDIDO")

pedido1 = Pedido(101)
pedido1.agregar_producto(b1)
pedido1.agregar_producto(p1)
pedido1.agregar_producto(p2)

print("Total del pedido:", pedido1.calcular_total())

print("\nPRUEBA DE CLIENTE")

cliente1 = Cliente(1, "Miguel", "miguel@email.com")
cliente1.realizar_pedido(pedido1)

print("Pedidos en historial:", len(cliente1.historial_pedidos))

print("\nPRUEBA DE INVENTARIO")

inventario = Inventario()
inventario.agregar_ingrediente("Cafe", 10)
inventario.agregar_ingrediente("Leche", 5)
inventario.agregar_ingrediente("Chocolate", 3)
print(inventario.ingredientes)

print("\nPRUEBA DE EMPLEADO")

empleado1 = Empleado(2, "Laura", "laura@email.com", "EMP02", "BARISTA")
empleado1.cambiar_estado_pedido(pedido1, "PREPARANDO")
print("Estado del pedido:", pedido1.estado)
