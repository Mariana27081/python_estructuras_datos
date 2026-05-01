# 1. Definir tiendas como sets de productos
tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor"}
tienda_norte = {"Mouse", "Teclado", "Impresora", "Tablet"}
tienda_sur = {"Laptop", "Tablet", "Auriculares", "Mouse"}

# 2. Calcular catálogo completo y productos comunes
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

print("Catálogo completo:", catalogo_completo)
print("Productos comunes en todas las tiendas:", productos_comunes)

# 3. Exclusivos de cada tienda
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur = tienda_sur.difference(tienda_centro.union(tienda_norte))

print("\nExclusivos tienda centro:", exclusivos_centro)
print("Exclusivos tienda norte:", exclusivos_norte)
print("Exclusivos tienda sur:", exclusivos_sur)

# Verificar solapamientos
print("\nCentro y Norte sin productos en común?:", tienda_centro.isdisjoint(tienda_norte))
print("Centro y Sur sin productos en común?:", tienda_centro.isdisjoint(tienda_sur))
print("Norte y Sur sin productos en común?:", tienda_norte.isdisjoint(tienda_sur))

# 4. Definir usuarios como sets de géneros cinematográficos
usuario1 = {"Acción", "Drama", "Ciencia Ficción", "Comedia"}
usuario2 = {"Drama", "Terror", "Comedia", "Romance"}
usuario3 = {"Acción", "Drama"}

# 5. Operaciones con sets
comunes = usuario1 & usuario2
universo = usuario1 | usuario2 | usuario3
exclusivos = usuario1 - usuario2
diferencias_simetrica = usuario1 ^ usuario2

print("\nGéneros comunes entre usuario1 y usuario2:", comunes)
print("Universo de géneros:", universo)
print("Exclusivos de usuario1:", exclusivos)
print("Diferencias simétricas usuario1 vs usuario2:", diferencias_simetrica)

# 6. Verificar subconjunto
es_subconjunto = usuario3 <= usuario1
print("\n¿usuario3 es subconjunto de usuario1?:", es_subconjunto)

# Resumen final integrado
print("\n===== RESUMEN FINAL =====")
print("Total productos en catálogo:", len(catalogo_completo))
print("Productos compartidos por todas las tiendas:", productos_comunes)
print("Preferencias de usuarios analizadas correctamente")