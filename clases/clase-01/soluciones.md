# Clase 1: soluciones

Los resultados numéricos salen de [`soluciones.py`](soluciones.py).

## Ejercicio 1

Hay varias respuestas válidas. Por ejemplo:

> Quiero ayudar al área de nómina a decidir cómo distribuir los turnos, usando el registro de horas extras, para reducir ese gasto un 10 % en tres meses.

La respuesta es buena si nombra a una persona, una decisión, unos datos y un resultado medible. El dashboard solo sería el medio.

## Ejercicio 2

| Columna | Qué significa | Tipo | Ejemplo |
| --- | --- | --- | --- |
| `fecha` | Día de la venta | Fecha | 2026-03-02 |
| `dia` | Día de la semana | Texto | lunes |
| `producto` | Producto vendido | Texto | Limonada |
| `categoria` | Grupo del producto | Texto | bebida |
| `unidades` | Cantidad vendida | Número entero (tiene 1 vacío) | 12 |
| `precio_unitario` | Precio de una unidad, en pesos | Número entero | 4000 |
| `temperatura_c` | Temperatura del día, en grados Celsius | Número entero | 19 |

**Periodo:** del 2 al 10 de marzo de 2026. No hay datos del domingo 8.

## Ejercicio 3

Los promedios son x̄ = 3 e ȳ = 4.

| x − x̄ | y − ȳ | Producto | (x − x̄)² | (y − ȳ)² |
| --- | --- | --- | --- | --- |
| −2 | −2 | 4 | 4 | 4 |
| −1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 2 | 1 | 2 | 4 | 1 |
| **Suma** | | **6** | **10** | **6** |

r = 6 / √(10 × 6) = 6 / 7,746 = **0,7746**

Es una relación positiva: cuando x sube, y tiende a subir.

## Ejercicio 4

**r = 0**, aunque la relación es perfecta: y = x². La correlación de Pearson solo mide relaciones en línea recta. Aquí y baja y luego sube, y esos dos tramos se cancelan. Por eso primero se grafica.

## Ejercicio 5

- Sin el punto extremo: **r = 0**
- Con (20, 40): **r = 0,9793**

Un solo dato crea una relación casi perfecta que los otros cinco no muestran. Antes de eliminarlo, averigua si es un error o un caso real importante.

## Ejercicio 6

```python
import pandas as pd

ventas = pd.read_csv("ventas_ejemplo.csv")
print(ventas.shape)
print(ventas.isna().sum())
```

Tiene **16 filas y 7 columnas**. Hay **1 vacío**, en `unidades`: el sandwich del jueves 5 de marzo.

## Ejercicio 7

```python
ventas["ingreso"] = ventas["unidades"] * ventas["precio_unitario"]
print(ventas.groupby("producto")[["unidades", "ingreso"]].sum())
```

| Producto | Unidades | Ingreso |
| --- | --- | --- |
| Limonada | 140 | $560.000 |
| Sandwich | 72 | $648.000 |

La limonada vende más unidades, pero el sandwich genera más dinero. Por eso es importante definir qué significa "vender más".

Pandas ignora el vacío al sumar, así que el sandwich podría estar subestimado. Un vacío no significa necesariamente cero ventas.

## Ejercicio 8

```python
print(ventas.groupby("dia")["unidades"].mean())
```

| Día | Promedio de unidades |
| --- | --- |
| Lunes | 9,75 |
| Martes | 12,75 |
| Miércoles | 13,50 |
| Jueves | 9,00 |
| Viernes | 20,00 |
| Sábado | 23,00 |

El jueves solo promedia la limonada, porque el sandwich está vacío. Los demás días promedian ambos productos. Además, la limonada se vende más que el sandwich, así que esta comparación mezcla cosas distintas. Conviene separarla por producto.

## Ejercicio 9

```python
for producto, grupo in ventas.groupby("producto"):
    print(producto, grupo["temperatura_c"].corr(grupo["unidades"]))

print(ventas["temperatura_c"].corr(ventas["unidades"]))
```

| Grupo | r |
| --- | --- |
| Limonada | 0,986 |
| Sandwich | 0,805 |
| Todo junto | 0,688 |

La correlación baja al juntar todo porque cada producto tiene un nivel de ventas distinto. Con la misma temperatura, la limonada vende más, y esa diferencia no tiene que ver con el clima.

**No se puede concluir que el calor cause las ventas.** Los días más calurosos fueron viernes y sábado, que también pueden ser días fuertes por otras razones. Además, son muy pocos datos. Para separar ambos efectos harían falta más semanas.

## Ejercicio 10

Depende de la herramienta. Una buena auditoría encuentra estos puntos:

- Dice qué hizo con el vacío.
- Sus totales coinciden con los de los ejercicios 6 y 7.
- No afirma que el calor causa las ventas.

## Ejercicio 11

Compara tu hoja con los ejercicios 1 y 2. Debe dejar claro quién usará el resultado, qué decisión mejora y qué contiene cada columna. Si los datos tienen información personal, anonimízalos antes de compartirlos.
