# 1. Definir inventario con tres productos [nombre, cantidad, precio]
inventario = [
    ["manzana", 50, 0.5],
    ["banana", 30, 0.3],
    ["naranja", 20, 0.4]
]

# 2. Definir actualizar_precio(producto, nuevo_precio)
def actualizar_precio(producto, nuevo_precio):
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio
            print(f"Precio de {producto} actualizado a {nuevo_precio}")
            return
    print(f"Producto {producto} no encontrado")

# 3. Definir registrar_venta(producto, cantidad)
def registrar_venta(producto, cantidad):
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta realizada: {cantidad} unidades de {producto}")
            else:
                print(f"No hay suficiente stock de {producto}")
            return
    print(f"Producto {producto} no encontrado")

# 4. Definir anadir_producto(producto, cantidad, precio)
def anadir_producto(producto, cantidad, precio):
    for item in inventario:
        if item[0] == producto:
            item[1] += cantidad
            print(f"Stock actualizado de {producto}, nueva cantidad: {item[1]}")
            return
    inventario.append([producto, cantidad, precio])
    print(f"Producto {producto} añadido al inventario")

# 5. Definir mostrar_inventario()
def mostrar_inventario():
    print("\nInventario actual:")
    for item in inventario:
        print(f"Producto: {item[0]}, Cantidad: {item[1]}, Precio: {item[2]}")

# Llamadas a funciones
actualizar_precio("banana", 0.35)     # Segundo producto
registrar_venta("manzana", 10)        # Primer producto
anadir_producto("pera", 25, 0.6)      # Producto nuevo
mostrar_inventario()