class Producto():
    def __init__(self,nombre,precio,stock):
        self.nombre =nombre
        self.precio_base=precio 
        self.stock=stock
        
    def aplicar_descuento(self,porcentaje):
        self.precio_base*=(1-porcentaje)
        print(f"El nuebo precio es {self.precio_base}")
        
    def actualizar_stock(self,cantidad):
    
        if (self.stock<cantidad) < 0:
            print("no puedes tener stock negatibo")
        else:
              self.stock += cantidad
              print(f"la nueba cantidad es {self.stock}")
              
            
class Categoria():
    def __init__(self,nombrecategoria):
        self.nombre_categoria=nombrecategoria
        self.lista_productos = []
        
    def agregar_producto(self,producto):
        self.lista_productos.append(producto)
        print(f"el producto {producto} se agrego a la lista")
        
    def balor_total_categoria(self):
        total = 0
        for producto in self.lista_productos:
            total += producto.precio_base*producto.stock
        return total
    

class Pedido():
    def __init__(self,cliente):
        self.cliente=cliente
        self.productos_comprados=[]
        self.estado = "Pendiente"
        
    def agregar_producto(self,producto):
        self.productos_comprados.append(producto)
        