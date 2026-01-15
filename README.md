# Apuntes de Pandas

Este repositorio contiene apuntes personales sobre Pandas, organizados en 6 secciones principales que cubren desde la lectura de datos hasta la combinación de DataFrames. Cada sección incluye ejemplos, tablas de métodos, y ejercicios prácticos.

## Dataset

El dataset utilizado proviene de Kaggle - [Netflix Streaming Data](https://www.kaggle.com/datasets/ahmadrazakashif/netflix-streaming-data).
Para ejecutar los ejemplos correctamente, descarga el archivo desde Kaggle y colócalo dentro de una carpeta llamada `data/` en la raíz del proyecto.

```
data/
├─ netflix_titles.csv
```

## Secciones 

| Sección  | Tema                               | Archivo asociado                                                     |
| -------- | -------------------------------- | ---------------------------------------------------------------------- |
| 01       | Crear, leer y guardar archivos   | [01_crear_leer_guardar.ipynb](notebooks/01_crear_leer_guardar.ipynb)   |
| 02       | Información, filtros y selección | [02_informacion_filtrar.ipynb](notebooks/02_informacion_filtrar.ipynb) |
| 03       | Funciones estadísticas y maps    | [03_std_map.ipynb](notebooks/03_std_map.ipynb)                         |
| 04       | Agrupación y clasificación       | [04_groupby_sorting.ipynb](notebooks/04_groupby_sorting.ipynb)         |
| 05       | Tipos de datos y valores nulos   | [05_tipo_de_datos.ipynb](notebooks/05_tipo_de_datos.ipynb)             |
| 06       | Renombrar y combinar             | [06_renombrar_combinar.ipynb](notebooks/06_renombrar_combinar.ipynb)   |

Cada notebook corresponde a un bloque conceptual del ecosistema Pandas, e integra los métodos y conceptos más usados en el análisis de datos.

## 01 - Crear, Leer y Guardar archivos

Resumen de algunos métodos para crear, leer y guardar archivos en Pandas.

| Comandos                       | Descripción                                          |
| ------------------------------ | ---------------------------------------------------- |
| `pd.DataFrame()`               | Crea un DataFrame                                    |
| `pd.Series()`                  | Crea una Serie                                       |
| `df['Nombre_columna'] = serie` | Agrega una Serie al DataFrame como una nueva columna |
| `serie = df['columna']`        | Convierte una columna de un DataFrame a una Serie    |
| `pd.read_csv("")`              | Lee un archivo csv                                   |
| `pd.read_sql("")`              | Lee un archivo sql previa conexion con base de datos |
| `df.to_csv("")`                | Guarda df en un archivo csv                          |
| `df.to_sql("")`                | Inserta df en una tabla o crea una base SQLite (.db) |

Puedes encontrar ejemplos en el siguiente notebook:
[01_crear_leer_guardar.ipynb](notebooks/01_crear_leer_guardar.ipynb)

> [!NOTE]
> Si guardo un DataFrame en una base SQLite existente, se creará o reemplazará una tabla.
> Si el archivo .db no existe, se creará automáticamente.

## 02 - Información, filtros y selección

Resumen para acceder a información de dataframes, indexar, seleccionar y asignar datos en Pandas.

### Información general sobre el Dataframe

| Comando                        | Descripción                                      |
| ------------------------------ | ------------------------------------------------ |
| `df.info()`                    | Datos generales: columnas, tipos, totales, nulos |
| `df.dtypes`                    | Devuelve los tipos de datos del df               |
| `df.shape`                     | Cantidad de filas y columnas                     |
| `df.columns`                   | Lista de columnas de un dataframe                |
| `df.head()`                    | Primeras filas del DataFrame                     |
| `df.tail()`                    | Últimas filas del DataFrame                      |
| `df.size`                      | Cantidad total de elementos, incluyendo nulos    |
| `df.count()`                   | Cantidad de datos **no nulos** por columna       |
| `df.values`                    | Devuelve un array del df                         |
| `df['columna'].unique()`       | Devuelve Array de valores únicos de una columna  |
| `df.nunique()`                 | Cantidad de valores únicos por columna           |
| `df['columna'].value_counts()` | Frecuencias de cada valor en una columna         |

### Selección de columnas y filas

| Comando                   | Descripción                            |
| ------------------------- | -------------------------------------- |
| `df['columna']`           | Selecciona una columna (retorna Serie) |
| `df[['col1','col2']]`     | Selecciona múltiples columnas          |
| `df.loc[fila, columna]`   | Selección por **etiquetas**            |
| `df.iloc[fila, columna]`  | Selección por **posición numérica**    |
| `df.set_index('columna')` | Usa una columna como índice            |
| `df['columna'].idxmax()`  | Índice del valor máximo                |
| `df['columna'].idxmin()`  | Índice del valor mínimo                |
| `.notnull()`              | Accede a valores no nulos              |
| `.isnull()`               | Accede a valores nulos                 |

### Filtros y condiciones

| Comando                           | Descripción                               |
| --------------------------------- | ----------------------------------------- |
| `df[df['col'] > valor]`           | Filtra filas según condición              |
| `df[df['columna'].isin([1,2,3])]` | Filtra filas según valores permitidos     |
| `df['col'].str.contains('texto')` | Filtra filas cuyo texto contiene un valor |
| `df.query("columna > 10")`        | Filtro usando sintaxis tipo SQL           |

### Asignación de datos

| Comando                       | Descripción                    |
| ----------------------------- | ------------------------------ |
| `df['nueva_columna'] = datos` | Crea/reescribe una columna     |
| `df.loc[cond, 'col'] = valor` | Asigna valores según condición |

Si trabajamos con **dataframes**, podemos seleccionar tanto filas como columnas. Si solamente indicamos la fila, asumira que queremos toda la información de la columna.
```
df.iloc[filas, columnas]
```
Si trabajos con **series**, solo podemos seleccionar las filas.
```
df['columna'].iloc[filas]
```

### Diferencia clave entre `iloc` y `loc`

`iloc` usa **posición númerica** para indexar (como listas en python):
- El inicio del rango **se incluye**.
- El final del rango **se excluye**.

`loc` usa **etiquetas** para indexar (los nombres del índice):
- El inicio **se incluye**.
- El final **también se incluye**.

Ejemplo:
- `df.iloc[0:1000]` devuelve **1000 filas**.
- `df.loc[0:1000]` devuelve **1001 filas**.

Puedes encontrar ejemplos en el siguiente notebook:
[02_informacion_filtrar.ipynb](notebooks/02_informacion_filtrar.ipynb)

## 03 - Funciones y maps 

Funciones para obtener información estadística, realizar operaciones aritméticas entre columnas y aplicar transformaciones personalizadas con funciones, `apply` y `map`.

### Información estadístisca

| Comando                        | Descripción                             |
| ------------------------------ | --------------------------------------- |
| `df.describe()`                | Estadísticas generales por columna      |
| `df.count()`                   | Conteo de datos no nulos de un df       |
| `.mean()`                      | **Promedio**                            |
| `.median()`                    | **mediana**, el valor central del grupo |
| `.mode()`                      | **Moda**, puede retornar varias         |
| `.min()` / `.max()`            | Mínimo y máximo                         |
| `.sum()`                       | Suma                                    |
| `.std()`                       | Desviación estándar                     |
| `.var()`                       | Varianza                                |
| `.quantile(0.25)`              | Percentil específico                    |
| `df['columna'].unique()`       | Valores únicos de una columna           |
| `df.nunique()`                 | Cantidad de valores únicos por columna  |
| `df['columna'].value_counts()` | Frecuencias de cada valor en la columna |

### Operaciones con columnas

| Comando                       | Descripción                       |
| ----------------------------- | --------------------------------- |
| `df['a'] + df['b']`           | Suma de columnas                  |
| `df['a'] - df['b']`           | Resta                             |
| `df['a'] * df['b']`           | Multiplicación                    |
| `df['a'] / df['b']`           | División                          |
| `df['nueva'] = df['a'] * 10`  | Crear columna derivada            |
| `df['col'] = df['col'].abs()` | Transformación simple             |
| `df.eval()`                   | Operaciones con sintaxis tipo SQL |

### Maps y Apply

| Comando                  | Descripción                                          |
| ------------------------ | ---------------------------------------------------- |
| `df['col'].apply(func)`  | Aplica una función a cada valor de una columna       |
| `df.apply(func, axis=1)` | Aplica función por fila o columna                    |
| `df['col'].map(serie)`   | Reemplaza valores según un mapeo                     |
| `df.applymap(func)`      | Aplica función a **todos** los valores del dataframe |
| `lambda x: ...`          | Funciones rápidas en una línea                       |

- `map()` es ideal para reemplazar valores (ej: 0 -> "No", 1 -> "Si")
```
df['columna'] = df['columna'].map({0: 'No', 1: 'Sí'})
```

- `apply()` es para lógica más completa
```
df['total'] = df.apply(lambda row: row['precio'] * row['cantidad'], axis=1)
```

Puedes encontrar ejemplos en el siguiente notebook:
[03_std_map.ipynb](notebooks/03_std_map.ipynb)

## 04 - Agrupación y Clasificación

Métodos para ordenar información, agrupar datos por una o varias columnas y aplicar funciones de agregación.

### Ordenar

| Comando                                  | Descripción                                     |
| ---------------------------------------- | ----------------------------------------------- |
| `df.sort_values('col')`                  | Ordena por una columna (ascendente por defecto) |
| `df.sort_values(['a','b'])`              | Ordena por múltiples columnas                   |
| `df.sort_values('col', ascending=False)` | Orden descendente                               |
| `df.sort_index()`                        | Ordena por índice                               |

### Agrupación con groupby

| Comando                                 | Descripción                   |
| --------------------------------------- | ----------------------------- |
| `df.groupby('col')`                     | Agrupa por una columna        |
| `df.groupby(['col1', 'col2'])`          | Agrupa por múltiples columnas |
| `df.groupby('col').size()`              | Cuenta filas por grupo        |
| `df.groupby('col').count()`             | Conteo por columna            |
| `df.groupby('col').mean()`              | Promedio por grupo            |
| `df.groupby('col').sum()`               | Suma por grupo                |
| `df.groupby('col').nunique()`           | Valores únicos por grupo      |
| `df.groupby('col').agg(['mean','max'])` | Varios cálculos por columna   |

### Groupby()

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
### Agg()

La función `agg()` es útil cuando se desea aplicar varias funciones a un df. Sus parámetros más importantes son:
- `func`: La función a aplicar.
- `axis`: El eje sobre el que aplicar la función

En el siguiente ejemplo se aplica la función `mean()` y `median()` a los valores numéricos. 

```
# Agrupar planetas por su tipo y calcular valores medios y medianos
planetas.groupby(['Tipo'])[planetas.select_dtypes(include=['number']).columns].agg(['mean', 'median'])
```

Puedes encontrar ejemplos en el siguiente notebook:
[04_groupby_sorting.ipynb](notebooks/04_groupby_sorting.ipynb)

## 05 - Tipos de datos y valores núlos

Métodos para trabajar con tipos de datos, convertir columnas, manejar valores faltantes y limpiar estructuras.

### Tipos de datos y conversiones

| Comando                                     | Descripción                                 |
| ------------------------------------------- | ------------------------------------------- |
| `df.dtypes`                                 | Muestra el tipo de dato de cada columna     |
| `df['col'] = df['col'].astype(int)`         | Conversión directa                          |
| `pd.to_numeric(df['col'], errors='coerce')` | Convierte a número (forzando errores a NaN) |

### Datos faltantes

| Comando                              | Descripción                                       |
| ------------------------------------ | ------------------------------------------------- |
| `df.isnull()`                        | Indica valores faltantes                          |
| `df.notnull()`                       | Indica valores NO faltantes                       |
| `df.dropna()`                        | Elimina filas con valores nulos                   |
| `df.dropna(subset=['col'])`          | Elimina filas solo si ciertas columnas tienen NaN |
| `df.dropna(how='all')`               | Elimina filas si todas las columnas tienen nulos  |
| `df.fillna(0)`                       | Rellena nulos con un valor                        |
| `df.fillna({'col': 0})`              | Rellena nulos por columna                         |
| `df['col'].fillna(df['col'].mean())` | Rellena con promedio u otra estadística           |
| `df['col'].bfill()`                  | Rellena valores NaN con el valor siguiente        |
| `df['col'].ffill()`                  | Rellena valores NaN con el valor anterior         |
| `df['col'].replace('actual','nuevo')`| Reeplaza un valor                                 |

Puedes encontrar ejemplos en el siguiente notebook:
[05_tipo_de_datos.ipynb](notebooks/05_tipo_de_datos.ipynb)

## 06 - Renombrar y combinar

Métodos para renombrar columnas, eliminar filas/columnas y combinar DataFrames usando concat y join.

### Renombrar

| Comando                              | Descripción                                |
| ------------------------------------ | ------------------------------------------ |
| `df.rename(columns={'old': 'new'})`  | Renombra columnas específicas              |
| `df.rename(index={0: 'primero'})`    | Renombra etiquetas del índice              |
| `df.rename_axis("", axis = 0)`       | Renombra el nombre del eje de las filas    |
| `df.rename_axis("", axis = 1)`       | Renombra el nombre del eje de las columnas |
| `df.set_axis([...], axis=1)`         | Asigna nuevos nombres a todas las columnas |
| `df.set_axis([...], axis=0)`         | Renombra todas las filas (índice)          |
| `df.columns = ['a','b','c']`         | Cambio directo de nombre de columnas       |
| `df = df.add_prefix('col_')`         | Agrega prefijo a todas las columnas        |
| `df = df.add_suffix('_2025')`        | Agrega sufijo a todas las columnas         |

### Unir dataframes - concat

| Comando                             | Descripción                                           |
| ----------------------------------- | ----------------------------------------------------- |
| `pd.concat([df1, df2])`             | Une dataframes verticalmente (uno bajo otro)          |
| `pd.concat([df1, df2], axis=1)`     | Une dataframes horizontalmente (uno al lado del otro) |

> [IMPORTANT!]
> Deben tener las mismas columnas para realizar una concatenación de dataframes

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

### Unir dataframes - merge

| Comando                                                 | Descripción                              |
| ------------------------------------------------------- | ---------------------------------------- |
| `pd.merge(df1, df2, on='col')`                          | Unión simple por columna                 |
| `pd.merge(df1, df2, left_on='a', right_on='b')`         | Unión por columnas con nombres distintos |
| `pd.merge(df1, df2, on='col', how='left')`              | LEFT JOIN                                |
| `pd.merge(df1, df2, on='col', how='right')`             | RIGHT JOIN                               |
| `pd.merge(df1, df2, on='col', how='outer')`             | FULL OUTER JOIN                          |
| `pd.merge(df1, df2, on='col', how='inner')`             | INNER JOIN (por defecto)                 |
| `pd.merge(df1, df2, left_index=True, right_index=True)` | Unión por índice                         |
| `df1.join(df2, how='left')`                             | Atajo para unir DataFrames por índice    |

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

Es mejor usar **concat** cuando los DataFrames tienen las mismas columnas y quieres apilarlos. **merge** cuando los DataFrames tienen columnas en común y quieres unirlos como en SQL.

Puedes encontrar ejemplos en el siguiente notebook:
[06_renombrar_combinar.ipynb](notebooks/06_renombrar_combinar.ipynb)

## 07 - Estadística

| Número | Comando                                      | Descripción                                       |
| ------ | -------------------------------------------- | ------------------------------------------------- |
| 1      | `.sample(n, replace, random_state)`          | Simula una muestra aleatoria                      |
| 2      | `df['columna'].std() / np.sqrt(df.shape[0])` | Calcular el error estándar de la muestra          |
| 3      | `stats.norm.interval(alpha, loc, scale)`     | Construye un intervalo de confianza               |
| 4      | `stats.ttest_ind(a, b, equal_var)`           | Obtiene el estadístico p-valor de dos muestras    |
| 5      | `stats.ttest_1samp(a, mu, alternative)`      | Obtiene el estadístico t p-valor para una muestra |


1. `n` tamaño de muestra (sobre 30 ideal), `replace` si es con reemplazo, `random_state` número de semilla para guardar la muestra aleatoria.
2. `df['columna']` debe contener la variable cuantitativa que se desea analizar.
3. `alpha` nivel de confianza, `loc` media de la muestra, `scale` error estándar de la muestra.
4. `a` datos de la primera muestra, `b` datos de la segunda muestra, `equal_var` booleano para indicar si asume que varianza poblacional es igual.
5. `a` datos de la muestra, `mu` media poblacional hipotética, `alternative` less, greater o two-sided.

## 08 - Regresión lineal

| Número | Comando                                             | Descripción                                       |
| ------ | --------------------------------------------------- | ------------------------------------------------- |
| 1      | `sns.pairplot(data)`                                | Crea un gráfico de dispersión por pares           |
| 2      | `ols_data = data[["col_1", "col_2"]]`               | Guardo en ols_data las variables y, x             |
| 3      | `ols_formula = "col_1 ~ col_2"`                     | Guardo la ols formula en orden Y, X               |
| 4      | `OLS = ols(formula = ols_formula, data = ols_data)` | Implementa un OLS                                 |
| 5      | `model = OLS.fit()`                                 | Crea un modelo de regresión lineal                | 
| 6      | `model.summary()`                                   | Obtiene un resumen del modelo                     |
| 7      | `sns.regplot(x = "col_1", y = "col_2", data = ols_data)` | Grafica un OLS con la línea de mejor ajuste  |
| 8      | `residuals = model.resid`                                | Guarda el residuo del modelo                 |
| 9      | `fig = sns.histplot(residuals)`                          | Grafica la distribución de los residuos      |
| 10     | `sm.qqplot(residuals, line='s')`                         | Grafica un QQ plot                           |
| 11     | `fig = sns.scatterplot(x=model.fittedvalues, y=model.resid)` | Grafica residuos frente a valores ajustados |



1. Trabajar con aquellos que tengan una correlación lineal.
2. Guarda los datos para crear un OLS
3. Guarda la formula para crear un OLS
4. Crea un OLS
5. Crea un modelo
6. Resume el modelo, obtieniendo información como la intercepción y la pendiente
7. Grafica la linea de mejor ajuste para comprobar el supuesto de linealidad
8. Guarda el residuo
9. Grafica la distribución de los residuos para comprobar el supuesto de normalidad
10. Grafica un QQ Plot para verificar el supuesto de normalidad
11. Grafica un diagrama de dispersión para verificar el supuesto de homocedasticidad (datos dispersos como una nube)

## Documentación adicional

Estos son solo alguno de los atributos y metodos más utilizados. Para una lista más detallada, consulte la [documentación de DataFrame en Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), que incluye ejemplos útiles de cómo utilizar cada herramienta. 


