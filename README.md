# Apuntes de Pandas

## Dataset

El dataset utilizado proviene de Kaggle - [Netflix Streaming Data](https://www.kaggle.com/datasets/ahmadrazakashif/netflix-streaming-data).
Para ejecutar los ejemplos correctamente, descarga el archivo desde Kaggle y colócalo dentro de una carpeta llamada `data/` en la raíz del proyecto.

```
data/
├─ netflix_titles.csv
```

## Atributos comunes de un DataFrame

| Atributo   | Descripción                                                   |
| ---------- | ------------------------------------------------------------- |
| `.columns` | Devuelve las columnas de un df                                |
| `.dtypes`  | Devuelve los tipos de datos del df                            |
| `.iloc`    | Accede a un grupo de filas y columnas utilizando su índice    |
| `.loc`     | Accede a un grupo de filas y columnas por su etiqueta         |
| `.shape`   | Devuelve una tupla con la cantidad de filas y columnas del df |
| `.values`  | Devuelve un array del df                                      |

## Métodos comunes de un DataFrame

| Métodos           | Descripción                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| `.apply()`        | aplica una función sobre un eje de un df                                 |
| `.copy()`         | Hace una copia de los índices y datos del df                             |
| `.describe()`     | Devuelve estadísticas descriptivas de un df                              |
| `.drop()`         | Elimina las etiquetas especificadas de filas y columnas de un df         |
| `.groupby()`      | Agrupa un conjunto de datos, aplica una función y combina resultados     |
| `.head()`         | Devuelve las primeras filas de un df                                     |
| `.info()`         | Devuelve un resumen del df (Podemos ver si existen valores nulos)        |
| `.isnull()`       | Devuelve un df booleano del mismo tamaño indicando si cada valor es nulo |
| `.sort_values()`  | Ordena los valores de un eje determinado                                 |
| `.value_counts()` | Devuelve una serie que contiene los recuentos de filas únicas de un df   |

Estos son solo alguno de los atributos y metodos más utilizados. Para una lista más detallada, consulte la [documentación de DataFrame en Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), que incluye ejemplos útiles de cómo utilizar cada herramienta. 

## Máscaras Booleanas

| Operador | Significado | Ejemplo                                                 |
| -------- | ----------- | ------------------------------------------------------- |
| `&`      | AND         | `(planetas["Lunas"] > 20) & ~(planetas["Lunas"] == 80)` |
| `\|`     | OR          | `(planetas["Lunas"] < 10) \| (planetas["Lunas"] > 50)`  |
| `~`      | NOT         | `~(planetas["Lunas"] == 80)`                            |