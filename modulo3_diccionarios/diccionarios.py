# 1. Definir ventas_por_region como dict anidado
ventas_por_region = {
    "Norte": {"Q1": 15000, "Q2": 18000, "Q3": 20000, "Q4": 22000},
    "Sur": {"Q1": 12000, "Q2": 14000, "Q3": 16000, "Q4": 18000},
    "Este": {"Q1": 10000, "Q2": 13000, "Q3": 17000, "Q4": 21000},
    "Oeste": {"Q1": 20000, "Q2": 21000, "Q3": 23000, "Q4": 25000}
}

# 2. Calcular ventas totales por región
totales_por_region = {}
for region, trimestres in ventas_por_region.items():
    totales_por_region[region] = sum(trimestres.values())

# 3. Encontrar región con mayores ventas
mejor_region = max(totales_por_region.items(), key=lambda x: x[1])
print(f"Región con mayores ventas: {mejor_region[0]} (${mejor_region[1]})")

# 4. Inicializar totales_por_trimestre
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

# 5. Acumular ventas por trimestre con iteración anidada
for region, trimestres in ventas_por_region.items():
    for trimestre, valor in trimestres.items():
        totales_por_trimestre[trimestre] += valor

# 6. Calcular gran total
gran_total = sum(totales_por_region.values())

# 7. Generar porcentajes con dict comprehension
porcentajes = {
    region: (total / gran_total) * 100
    for region, total in totales_por_region.items()
}

# 8. Imprimir reporte ordenado de mayor a menor
print("\n--- Reporte de Ventas por Región ---")
for region, total in sorted(totales_por_region.items(), key=lambda x: x[1], reverse=True):
    print(f"{region}: ${total} ({porcentajes[region]:.2f}%)")

# Extra: mostrar totales por trimestre
print("\n--- Ventas Totales por Trimestre ---")
for trimestre, total in totales_por_trimestre.items():
    print(f"{trimestre}: ${total}")