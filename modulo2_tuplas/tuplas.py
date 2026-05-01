# 1. Definir catalogo como tupla de subtuplas (titulo, director, año, puntuacion)
catalogo = (
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Interstellar", "Christopher Nolan", 2014, 8.6),
    ("Parasite", "Bong Joon-ho", 2019, 8.5),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.2)
)

# 2. Recorrer catalogo con for desempaquetando los cuatro campos
print("Catálogo de películas:")
for titulo, director, año, puntuacion in catalogo:
    print(f"Título: {titulo}, Director: {director}, Año: {año}, Puntuación: {puntuacion}")

# 3. Usar operador * para separar primera pelicula del resto
primera, *resto = catalogo
print("\nPrimera película:")
print(primera)

print("\nResto de películas:")
for peli in resto:
    print(peli)

# 4. Definir buscar_por_director(director)
def buscar_por_director(director):
    coincidencias = tuple(peli for peli in catalogo if peli[1] == director)
    return coincidencias

# 5. Definir obtener_estadisticas(peliculas)
def obtener_estadisticas(peliculas):
    puntuaciones = [peli[3] for peli in peliculas]
    minimo = min(puntuaciones)
    maximo = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    return (minimo, maximo, promedio)

# 6. Llamar a buscar_por_director e imprimir coincidencias
resultado = buscar_por_director("Christopher Nolan")
print("\nPelículas de Christopher Nolan:")
for peli in resultado:
    print(peli)

# 7. Desempaquetar retorno de obtener_estadisticas
min_punt, max_punt, prom_punt = obtener_estadisticas(catalogo)

# 8. Imprimir mínima, máxima y promedio
print("\nEstadísticas de puntuación:")
print(f"Mínima: {min_punt}")
print(f"Máxima: {max_punt}")
print(f"Promedio: {prom_punt:.2f}")