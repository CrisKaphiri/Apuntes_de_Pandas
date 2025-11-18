# Apuntes de Pandas

Este repositorio contiene apuntes personales organizados sobre Pandas, enfocado en el **análisis y manipulación de datos**.

A Continuación, se describe el contenido de este repositorio:

| Sección | Tema                           | Archivo asociado              |
| ------- | ------------------------------ | ----------------------------- |
| 1       | Crear, Leer y guardar archivos | `01_crear_leer_guardar.ipynb` |


## 01 Leer y guardar archivos

## 02 Crear DataFrame o Serie




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
| `.size`    | Devuelve la totalidad de elementos en una serie o dataframe   |

## Métodos comunes de un DataFrame

| Métodos           | Descripción                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| `.apply()`        | Aplica una función sobre un eje de un df                                 |
| `.copy()`         | Hace una copia de los índices y datos del df                             |
| `.describe()`     | Devuelve estadísticas descriptivas de un df                              |
| `.drop()`         | Elimina las etiquetas especificadas de filas y columnas de un df         |
| `.head()`         | Devuelve las primeras filas de un df                                     |
| `.info()`         | Devuelve un resumen del df (Podemos ver si existen valores nulos)        |
| `.isnull()`       | Devuelve un df booleano del mismo tamaño indicando si cada valor es nulo |
| `.sort_values()`  | Ordena los valores de un eje determinado                                 |
| `.value_counts()` | Devuelve una serie que contiene los recuentos de filas únicas de un df   |
| `.groupby()`      | Agrupa un conjunto de datos, aplica una función y combina resultados     |
| `.agg()`          | Permite aplicar varios cálculos o funciones a grupos de datos            |
| `.merge()`        | Combina dos DataFrames según columnas o índices comunes (tipo SQL JOIN)  |
| `.concat()`       | Combina DataFrames por filas o columnas (apila uno sobre otro)           |

Estos son solo alguno de los atributos y metodos más utilizados. Para una lista más detallada, consulte la [documentación de DataFrame en Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), que incluye ejemplos útiles de cómo utilizar cada herramienta. 

## Máscaras Booleanas

| Operador | Significado | Ejemplo                                                 |
| -------- | ----------- | ------------------------------------------------------- |
| `&`      | AND         | `(planetas["Lunas"] > 20) & ~(planetas["Lunas"] == 80)` |
| `\|`     | OR          | `(planetas["Lunas"] < 10) \| (planetas["Lunas"] > 50)`  |
| `~`      | NOT         | `~(planetas["Lunas"] == 80)`                            |

## Groupby()

La función `groupby()` es un método que pertenece a la clase de los DataFrame. Funciona dividiendo los datos en grupos en función de criterios especificados, aplicando una función a cada grupo de forma independiente y combinando los resultados en una estructura de datos.

Sirve para:
- Agregación: Cálculo de estadísticas de resumen para cada grupo.
- Transformación: Aplicar funciones a cada grupo y devolver los datos modificados.
- Filtración: Selección de grupos específicos en función de determinadas condiciones.
- Iteración: Iteración sobre grupos o valores.

Estas son alguna de las funciones más utilizadas de agregación:

| Función    | Descripción                                              |
| ---------- | -------------------------------------------------------- |
| `count()`  | Devuelve el número de valores **no nulos** en cada grupo |
| `sum()`    | Calcula la **suma** de los valores de cada grupo         |
| `mean()`   | Calcula la **media aritmética** de los valores           |
| `median()` | Devuelve la **mediana**, el valor central del grupo      |
| `min()`    | Retorna el **valor mínimo** de cada grupo                |
| `max()`    | Retorna el **valor máximo** de cada grupo                |
| `std()`    | Calcula la **desviación estándar** de los valores        |
| `var()`    | Devuelve la **varianza** de cada grupo                   |

Es necesario especificar el parámetro `numeric_only` cuando se apliquen funciones de agregación.
```
# Agrupar planetas por tipo y campo magnético. Calcular valores prmedios de las columnas numéricas.
planetas.groupby(['Tipo', 'Campo_magnetico']).mean(numeric_only= True)
```

## Agg()

La función `agg()` es útil cuando se desea aplicar varias funciones a un df. Sus parámetros más importantes son:
- `func`: La función a aplicar.
- `axis`: El eje sobre el que aplicar la función

En el siguiente ejemplo se aplica la función `mean()` y `median()` a los valores numéricos. 

```
# Agrupar planetas por su tipo y calcular valores medios y medianos
planetas.groupby(['Tipo'])[planetas.select_dtypes(include=['number']).columns].agg(['mean', 'median'])
```

## Merge()

`merge()` permite combinar dos DataFrames basándose en columnas o índices, similar a las uniones de SQL.

##### Parámetros clave

- `on`: columna(s) por las que se unen ambos DataFrames.
- `left_on` / `right_on`: si el nombre de la columna es distinto en cada tabla.
- `left_index` / `right_index`: usa el índice como clave de unión.
- `how`: tipo de unión.

##### Tipos de unión

| Tipo      | Descripción                                                              |
| --------- | ------------------------------------------------------------------------ |
| `"inner"` | Devuelve solo las coincidencias entre ambos DataFrames.                  |
| `"left"`  | Mantiene todas las filas del DataFrame izquierdo y agrega coincidencias. |
| `"right"` | Mantiene todas las filas del DataFrame derecho y agrega coincidencias.   |
| `"outer"` | Mantiene todas las filas de ambos, rellena con `NaN` donde no hay match. |

```
df_merged = pd.merge(df1, df2, on="id", how="inner")
```

## Concat()

`concat()` sirve para apilar DataFrames uno encima del otro o uno al lado del otro.

##### Parámetros clave

- `axis=0`: concatena por filas (uno debajo de otro).
- `axis=1`: concatena por columnas (uno al lado del otro).
- `ignore_index=True`: reinicia el índice.
- `join`: `"outer"` mantiene todas las columnas, `"inner"` solo las que coinciden.

Apilar columnas
```
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
```

Unir columnas
```
df_concat = pd.concat([df1, df2], axis=1)
```

