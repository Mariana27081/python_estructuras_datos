# 1. Definir ventas con 6 productos (producto, unidades, precio, categoria)
ventas = [
    ("Laptop", 5, 800, "Tecnología"),
    ("Mouse", 20, 25, "Tecnología"),
    ("Silla", 10, 120, "Hogar"),
    ("Escritorio", 3, 300, "Hogar"),
    ("Audífonos", 15, 60, "Tecnología"),
    ("Lámpara", 8, 45, "Hogar")
]

# 2. List comp: valor_total = unidades * precio
valores_totales = [unidades * precio for _, unidades, precio, _ in ventas]

# 3. List comp con filtro: productos_destacados (valor > 1000)
productos_destacados = [
    nombre for nombre, unidades, precio, _ in ventas
    if unidades * precio > 1000
]

# 4. Dict comp: producto_info nombre → {valor, unidades}
producto_info = {
    nombre: {"valor": unidades * precio, "unidades": unidades}
    for nombre, unidades, precio, _ in ventas
}

# 5. Dict comp con filtro: ranking_premium (precio > 50) ordenado por valor desc
ranking_premium = dict(sorted(
    {
        nombre: unidades * precio
        for nombre, unidades, precio, _ in ventas
        if precio > 50
    }.items(),
    key=lambda x: x[1],
    reverse=True
))

# 6. Set comp: categorias_unicas
categorias_unicas = {categoria for _, _, _, categoria in ventas}

# 7. Set comp con filtro: productos_baratos (precio <= 50)
productos_baratos = {
    nombre for nombre, _, precio, _ in ventas if precio <= 50
}

# 8. Combinar: resumen_formateado (dict comp filtrado)
resumen_formateado = {
    nombre: f"{unidades} uds - ${precio} c/u - Total: ${unidades * precio}"
    for nombre, unidades, precio, _ in ventas
    if unidades * precio > 500
}

# 9. Calcular gran_total
gran_total = sum(unidades * precio for _, unidades, precio, _ in ventas)

# RESULTADOS
print("Valores totales:", valores_totales)
print("\nProductos destacados (>1000):", productos_destacados)
print("\nProducto info:", producto_info)
print("\nRanking premium:", ranking_premium)
print("\nCategorías únicas:", categorias_unicas)
print("\nProductos baratos:", productos_baratos)
print("\nResumen formateado:", resumen_formateado)
print("\nGran total de ventas:", gran_total)