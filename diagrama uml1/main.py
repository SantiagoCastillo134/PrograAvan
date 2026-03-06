from models import *

print("--- REGISTRO MANUAL DE INVENTARIO (10 OBJETOS) ---")

p1 = Producto(11, "Palomitas Medianas", 70.0, "Snacks")
p2 = Producto(12, "Refresco Grande", 55.0, "Bebidas")
p3 = Producto(13, "Hamburguesa Clásica", 95.0, "Comida")
p4 = Producto(14, "Papas a la Francesa", 65.0, "Snacks")
p5 = Producto(15, "Gomitas Dulces", 30.0, "Dulces")
p6 = Producto(16, "Té Helado", 40.0, "Bebidas")
p7 = Producto(17, "Combo Familiar", 320.0, "Combos")
p8 = Producto(18, "Entrada IMAX Adulto", 120.0, "Boletos")
p9 = Producto(19, "Entrada 2D Niño", 60.0, "Boletos")
p10 = Producto(20, "Combo Palomitas + Refresco", 140.0, "Promos")

print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())

print("\n-VALIDACION DE DATOS FINALIZADA-")
print("Sistema de Cine")

peliculas = [
    Pelicula("Interstellar", 169, "B", "Ciencia Ficcion"),
    Pelicula("Jurassic World", 124, "B", "Accion"),
    Pelicula("El Rey Leon", 118, "A", "Animacion"),
    Pelicula("Doctor Strange", 115, "B", "Accion"),
    Pelicula("Inception", 148, "B", "Ciencia Ficcion"),
    Pelicula("Kung Fu Panda", 92, "A", "Animacion"),
    Pelicula("El Conjuro", 112, "C", "Terror"),
    Pelicula("Deadpool", 108, "C", "Accion"),
    Pelicula("Up", 96, "A", "Animacion"),
    Pelicula("Guardianes de la Galaxia", 121, "B", "Accion")
]

for p in peliculas:
    p.obtener_detalles()


salas = [
    Sala(1, "Sala Premium", "Piso 1", "IMAX", 40),
    Sala(2, "Sala Platino", "Piso 1", "2D", 35),
    Sala(3, "Sala Familiar", "Piso 2", "2D", 28),
    Sala(4, "Sala Kids", "Piso 2", "3D", 20),
    Sala(5, "Sala VIP 1", "Piso 3", "IMAX", 18),
    Sala(6, "Sala VIP 2", "Piso 3", "3D", 16),
    Sala(7, "Sala Classic", "Piso 4", "2D", 24),
    Sala(8, "Sala Max", "Piso 4", "IMAX", 30),
    Sala(9, "Sala Digital", "Piso 5", "3D", 22),
    Sala(10, "Sala Estándar", "Piso 5", "2D", 26)
]

for s in salas:
    s.calcular_asientos_libres()


funciones = []

for i in range(10):
    funcion = Funcion(i+1, peliculas[i], salas[i], "18:00", 80)
    funciones.append(funcion)

for f in funciones:
    f.obtener_detalles_funcion()


usuarios = [
    Usuario(1, "Miguel", "miguel@mail.com", "111"),
    Usuario(2, "Valeria", "valeria@mail.com", "222"),
    Usuario(3, "Andres", "andres@mail.com", "333"),
    Usuario(4, "Fernanda", "fernanda@mail.com", "444"),
    Usuario(5, "Ricardo", "ricardo@mail.com", "555"),
    Usuario(6, "Daniela", "daniela@mail.com", "666"),
    Usuario(7, "Sebastian", "sebastian@mail.com", "777"),
    Usuario(8, "Paula", "paula@mail.com", "888"),
    Usuario(9, "Alejandro", "alejandro@mail.com", "999"),
    Usuario(10, "Camila", "camila@mail.com", "000")
]

for u in usuarios:
    u.login()


empleados = [
    Empleado(11, "Admin1", "admin1@mail.com", "101", "EMP01", "ADMIN"),
    Empleado(12, "Taquilla1", "taquilla@mail.com", "102", "EMP02", "TAQUILLERO"),
    Empleado(13, "Limpieza1", "clean@mail.com", "103", "EMP03", "LIMPIEZA")
]

for e in empleados:
    e.marcar_entrada()
    e.gestionar_funciones()


promociones = [
    Promocion("DESC10", "10% descuento", 0.10),
    Promocion("DESC20", "20% descuento", 0.20),
    Promocion("DESC5", "5% descuento", 0.05),
    Promocion("DESC15", "15% descuento", 0.15),
    Promocion("DESC25", "25% descuento", 0.25)
]


reserva1 = Reserva(1, usuarios[0], funciones[0], ["A1", "A2", "A3"])
reserva1.calcular_total()
reserva1.monto_total = promociones[0].aplicar_descuento(reserva1.monto_total)
reserva1.confirmar_pago()

reserva2 = Reserva(2, usuarios[1], funciones[0], ["A1"])
reserva2.calcular_total()
reserva2.confirmar_pago()

reserva3 = Reserva(3, usuarios[2], funciones[1], ["B1", "B2"])
reserva3.calcular_total()
reserva3.confirmar_pago()

salas[0].calcular_asientos_libres()
salas[1].calcular_asientos_libres()