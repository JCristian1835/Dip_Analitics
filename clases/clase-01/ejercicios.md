# Clase 1: ejercicios

Intenta cada ejercicio antes de abrir las [soluciones](soluciones.md). Los datos de [`ventas_ejemplo.csv`](ventas_ejemplo.csv) son ficticios.

## Nivel 1: el proyecto

**Ejercicio 1. Encuentra el para qué.** Reescribe esta idea con la frase de la [teoría](teoria.md#2-el-para-qué-del-proyecto): *"Quiero hacer un dashboard con Python de los datos de nómina"*.

**Ejercicio 2. Diccionario de datos.** Escribe el diccionario de `ventas_ejemplo.csv`: qué significa cada columna, su tipo y un ejemplo. Anota también el periodo que cubre.

## Nivel 2: correlación

**Ejercicio 3. A mano.** Calcula r con lápiz y calculadora:

| x | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| y | 2 | 4 | 5 | 4 | 5 |

**Ejercicio 4. La curva.** Antes de calcular, dibuja los puntos y predice r. Después compruébalo:

| x | −2 | −1 | 0 | 1 | 2 |
| --- | --- | --- | --- | --- | --- |
| y | 4 | 1 | 0 | 1 | 4 |

¿Hay relación entre x e y? ¿Por qué r dice otra cosa?

**Ejercicio 5. El valor extremo.** Calcula r con estos datos. Luego agrega el punto (20, 40) y calcúlala otra vez. ¿Qué concluyes?

| x | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| y | 5 | 4 | 5 | 4 | 5 |

## Nivel 3: Pandas

Usa `ventas_ejemplo.csv`.

**Ejercicio 6. Revisa la tabla.** ¿Cuántas filas y columnas tiene? ¿Cuántos vacíos hay y en qué columna?

**Ejercicio 7. Ventas por producto.** Crea la columna `ingreso` y calcula unidades e ingresos por producto. ¿Cuál vende más unidades? ¿Cuál genera más dinero? ¿Qué pasó con la fila vacía?

**Ejercicio 8. Promedio por día.** Calcula el promedio de `unidades` por día de la semana. Mira el jueves: ¿por qué ese promedio no es comparable con los demás?

**Ejercicio 9. Temperatura y ventas.** Calcula la correlación entre `temperatura_c` y `unidades`, primero por producto y luego con todo junto. ¿Por qué cambia? ¿Puedes concluir que el calor causa las ventas? Revisa qué días fueron los más calurosos.

## Nivel 4: tu proyecto

**Ejercicio 10. Audita a la IA.** Pídele a una herramienta de IA que analice `ventas_ejemplo.csv`. Compara sus respuestas con las tuyas de los ejercicios 6 a 9. Anota qué hizo con el valor vacío y si alguna conclusión dice más de lo que los datos permiten.

**Ejercicio 11. Prepara tu entrega.** Escribe en una hoja el para qué de tu proyecto y el diccionario de tu base de datos. Es la tarea que el profesor pidió para la clase siguiente.
