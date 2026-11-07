"""
Calcula las respuestas de la clase 1. Intenta los ejercicios antes de correrlo.

Uso, desde la carpeta principal del repositorio:
    python -m pip install -r requirements.txt
    python clases/clase-01/soluciones.py
"""
from pathlib import Path
import sys

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
ventas = pd.read_csv(Path(__file__).with_name("ventas_ejemplo.csv"))


def correlacion_a_mano(x, y):
    x, y = np.array(x, dtype=float), np.array(y, dtype=float)
    dx, dy = x - x.mean(), y - y.mean()
    print("  desviaciones de x:", dx.tolist())
    print("  desviaciones de y:", dy.tolist())
    print("  suma de productos:", float((dx * dy).sum()))
    print("  suma dx^2:", float((dx**2).sum()), "| suma dy^2:", float((dy**2).sum()))
    return float((dx * dy).sum() / np.sqrt((dx**2).sum() * (dy**2).sum()))


print("Ejercicio 3: correlación a mano")
print("  r =", round(correlacion_a_mano([1, 2, 3, 4, 5], [2, 4, 5, 4, 5]), 4))

print("\nEjercicio 4: relación perfecta que la correlación no ve (y = x^2)")
print("  r =", round(float(np.corrcoef([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])[0, 1]), 4))

print("\nEjercicio 5: efecto de un valor extremo")
x, y = [1, 2, 3, 4, 5], [5, 4, 5, 4, 5]
print("  sin el valor extremo: r =", round(float(np.corrcoef(x, y)[0, 1]), 4))
print("  con (20, 40):         r =", round(float(np.corrcoef(x + [20], y + [40])[0, 1]), 4))

print("\nEjercicio 6: revisar la tabla")
print("  filas y columnas:", ventas.shape)
print("  vacíos por columna:", ventas.isna().sum().to_dict())

print("\nEjercicio 7: ventas por producto")
ventas["ingreso"] = ventas["unidades"] * ventas["precio_unitario"]
print(ventas.groupby("producto")[["unidades", "ingreso"]].sum().to_string())

print("\nEjercicio 8: promedio de unidades por día")
orden = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
print(ventas.groupby("dia")["unidades"].mean().reindex(orden).round(2).to_string())

print("\nEjercicio 9: temperatura y unidades por producto")
for producto, grupo in ventas.groupby("producto"):
    print(f"  {producto}: r = {grupo['temperatura_c'].corr(grupo['unidades']):.3f} ({grupo['unidades'].notna().sum()} días con dato)")
print(f"  Todo junto, sin separar: r = {ventas['temperatura_c'].corr(ventas['unidades']):.3f}")
