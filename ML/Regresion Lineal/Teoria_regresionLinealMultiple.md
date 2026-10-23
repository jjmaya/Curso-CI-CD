# Teoria_regresionMultiple

## 1. Idea central de la regresión lineal múltiple

La regresión lineal múltiple extiende la regresión lineal simple para modelar una variable objetivo usando varias variables explicativas al mismo tiempo.

La idea es construir un modelo que relacione una salida continua $y$ con varias entradas $x_1, x_2, \dots, x_d$ mediante una combinación lineal:

$$
\hat{y} = w_0 + w_1x_1 + w_2x_2 + \cdots + w_dx_d
$$

Donde:

- $\hat{y}$ es el valor predicho.
- $w_0$ es el intercepto.
- $w_1, \dots, w_d$ son los coeficientes del modelo.
- $x_1, \dots, x_d$ son las variables explicativas.

En este tipo de modelos, cada coeficiente mide el efecto de su variable correspondiente sobre la respuesta, manteniendo constantes las demás variables.

## 2. Qué representa un dato en el conjunto

Cada observación del conjunto de datos puede escribirse como un par:

$$
(x_i, y_i) = (x_{i1}, x_{i2}, \dots, x_{id}, y_i)
$$

Y el conjunto completo como:

$$
D = \{(x_i, y_i)\}_{i=1}^{N}
$$

Donde $N$ es el número total de instancias y $d$ la dimensionalidad del espacio de entrada, es decir, el número de variables predictoras.

## 3. Cómo aprende el modelo

El algoritmo de aprendizaje busca los valores de $w_0, w_1, \dots, w_d$ que produzcan el mejor ajuste a los datos.

Para decidir qué tan bueno es un conjunto de parámetros, se utiliza una función de costo. En regresión lineal, una de las más comunes es el error cuadrático medio:

$$
\mathrm{MSE} = \frac{1}{N}\sum_{i=1}^{N}(\hat{y}_i - y_i)^2
$$

El objetivo del entrenamiento es minimizar esa función de costo.

## 4. Interpretación de los coeficientes

Interpretar un modelo de regresión lineal múltiple significa responder esta pregunta: ¿qué pasa con el valor esperado de la variable objetivo cuando una variable explicativa aumenta en una unidad, manteniendo las demás constantes?

La respuesta está en el coeficiente asociado a esa variable.

- Si el coeficiente es positivo, la relación es positiva.
- Si el coeficiente es negativo, la relación es negativa.

Esta interpretación es local y controlada: solo describe el cambio esperado cuando el resto de variables no cambia.

## 5. Ejemplo de inmuebles

Supongamos que queremos predecir el precio de venta de un inmueble usando estas variables:

- área de construcción
- número de baños
- área del lote

El modelo obtenido es:

$$
\text{precio} = 204674.49 + 177.89 \cdot \text{área de construcción} - 28453.62 \cdot \text{número de baños} - 0.02 \cdot \text{área del lote}
$$

Este resultado muestra que el precio estimado depende de una combinación lineal de las variables del problema.

## 6. Significancia estadística de los coeficientes

No basta con mirar el valor del coeficiente. También conviene saber si ese coeficiente es estadísticamente significativo.

Para ello se usa la prueba t de Student, con hipótesis como las siguientes para cada parámetro:

$$
H_0: w_j = 0
$$

$$
H_a: w_j \neq 0
$$

Si el p-valor es menor o igual que el nivel de significancia $\alpha$, se rechaza la hipótesis nula y se considera que la variable aporta información relevante al modelo.

### Tabla de ejemplo

| Atributo | Coeficiente | Estadístico t | p-valor |
|---|---:|---:|---:|
| área de construcción | 177.89 | 46.391 | 0.000 |
| número de baños | -28453.62 | -10.516 | 0.000 |
| área del lote | -0.02 | -0.02 | 0.667 |
| intercepto | 204674.49 | 32.274 | 0.000 |

Si usamos $\alpha = 0.05$, entonces:

- área de construcción es significativa.
- número de baños es significativa.
- área del lote no es significativa.

Por tanto, desde una perspectiva estadística, el área del lote podría eliminarse del modelo sin perder evidencia importante de relación con el precio.

## 7. Cómo interpretar el efecto de cada variable

En regresión múltiple, para ver el efecto de una variable, las demás deben mantenerse fijas.

### 7.1. Área de construcción

Supongamos un inmueble con 100 pies$^2$ de área de construcción y 3 baños. Ignorando temporalmente el área del lote para la explicación, el precio estimado es:

$$
\text{precio} = 204674.49 + 177.89 \cdot 100 - 28453.62 \cdot 3 = 137102.63
$$

Si aumentamos el área de construcción a 101, manteniendo fijo el número de baños:

$$
\text{precio} = 204674.49 + 177.89 \cdot 101 - 28453.62 \cdot 3 = 137280.52
$$

La diferencia es 177.89. Esto significa que, manteniendo constantes las demás variables, una unidad adicional en el área de construcción incrementa el precio esperado en 177.89.

### 7.2. Número de baños

Partimos del mismo inmueble con 100 pies$^2$ de área de construcción y 3 baños:

$$
\text{precio} = 204674.49 + 177.89 \cdot 100 - 28453.62 \cdot 3 = 137102.63
$$

Si aumentamos el número de baños a 4, manteniendo fija el área de construcción:

$$
\text{precio} = 204674.49 + 177.89 \cdot 100 - 28453.62 \cdot 4 = 108649.01
$$

La diferencia es -28453.62. Eso quiere decir que, con las demás variables constantes, una unidad adicional en el número de baños reduce el valor esperado del inmueble en 28453.62.

## 8. Cómo leer el intercepto

El intercepto $w_0 = 204674.49$ representa el valor estimado del precio cuando todas las variables explicativas valen cero.

En muchos problemas, ese valor no tiene interpretación práctica, porque cero puede no ser un valor realista o válido para todas las variables del modelo.

Por eso, aunque el intercepto forma parte del modelo y de su ajuste, normalmente se interpreta con cautela.

## 9. Qué nos enseña este ejemplo

Este caso resume bien la lógica de la regresión lineal múltiple:

- el modelo combina varias variables explicativas;
- cada coeficiente mide un efecto parcial sobre la respuesta;
- la significancia estadística ayuda a decidir qué variables aportan información;
- una variable con coeficiente grande no siempre es útil si su p-valor no muestra evidencia suficiente;
- interpretar el modelo exige fijar las demás variables mientras se analiza una sola.

## 10. Resumen

- La regresión lineal múltiple modela una variable objetivo continua usando varias variables predictoras.
- El modelo tiene la forma de una combinación lineal de los atributos.
- Cada coeficiente se interpreta como un cambio esperado en la respuesta cuando su variable aumenta en una unidad, manteniendo las demás constantes.
- El p-valor permite evaluar si un coeficiente es estadísticamente significativo.
- En el ejemplo, área de construcción y número de baños resultan significativas, mientras que área del lote no aporta evidencia suficiente al modelo.

## 11. Referencias

- Bruce, P., Bruce, A., Gedeck, P. (2020). *Practical Statistics for Data Scientists. 50+ Essential Concepts Using R and Python*. Second edition. O'Reilly Media. Capítulo 4.
- Kelleher, J. D., Mac Namee, B., D'Arcy, A. (2020). *Fundamentals of Machine Learning for Predictive Data Analytics*. The MIT Press. Capítulo 7, sección 47.4.1, “Interpreting multivariable linear regression models”.
- Larose, D. T., Larose, C. D. (2015). *Data Mining and Predictive Analytics*. Wiley. Capítulo 9, páginas 236-243, “An example of multiple regression”.
- James, G., Witten, D., Hastie, T., Tibshirani, R. (2021). *An Introduction to Statistical Learning*. Springer. Capítulos 3 y 6.