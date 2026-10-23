# Teoria_regresionLineal

## 1. Idea general de la regresión lineal

La regresión es una técnica de aprendizaje supervisado que construye una función a partir de datos para estimar una variable de salida continua $\hat{y}$ a partir de una entrada $x$.

En regresión lineal, esa función se expresa como una combinación lineal de las variables explicativas:

$$
\hat{y} = w_0 + w_1x_1 + w_2x_2 + \cdots + w_dx_d
$$

Donde:

- $w_0$ es el intercepto.
- $w_1, \dots, w_d$ son los coeficientes o pesos del modelo.
- $d$ es el número de variables explicativas.

El objetivo del aprendizaje es encontrar los valores de los parámetros que hagan que las predicciones estén lo más cerca posible de los valores reales.

## 2. Regresión lineal simple

En la regresión lineal simple solo hay una variable predictora. En ese caso, el modelo toma la forma de una recta:

$$
\hat{y} = w_0 + w_1x
$$

Interpretación geométrica:

- $w_0$ es el intercepto de la recta.
- $w_1$ es la pendiente o inclinación.

Si la variable predictora es el área de construcción y la variable objetivo es el precio de un inmueble, el modelo aprende la relación entre ambas variables y ajusta la recta que mejor se adapte a los datos.

## 3. ¿Por qué hay infinitas rectas posibles?

Para un conjunto de puntos siempre pueden definirse infinitas rectas. Cada combinación distinta de $w_0$ y $w_1$ genera una recta diferente. El problema del aprendizaje consiste en elegir la recta que mejor explique los datos.

La “mejor” recta es la que produce el menor error global de predicción.

## 4. Error de predicción y función de costo

Si el modelo predice un valor \(\hat{y}\) y el valor real es \(y\), existe un error de predicción.

Una forma muy usada para medirlo es el error cuadrático medio (MSE, *Mean Squared Error*):

$$
\mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

Esta función de costo depende de los parámetros del modelo, por lo que el aprendizaje consiste en encontrar los valores de $w_0$ y $w_1$ que la minimicen.

## 5. Enfoques para resolver el problema

### 5.1. Enfoque analítico

En regresión lineal simple, los parámetros pueden obtenerse con el método de mínimos cuadrados.

Primero se calculan las medias de entrada y salida:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i, \qquad \bar{y} = \frac{1}{n}\sum_{i=1}^{n}y_i
$$

Luego, la pendiente se calcula como:

$$
w_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

Y el intercepto como:

$$
w_0 = \bar{y} - w_1\bar{x}
$$

### 5.2. Enfoque numérico

También puede resolverse mediante optimización numérica, por ejemplo con descenso por gradiente u otros métodos de minimización.

## 6. Ejemplo del inmueble

Para el problema de estimar el precio de un inmueble con base en el área de construcción, se obtuvo el siguiente modelo:

$$
\text{precio} = 52516.31 + 185.82 \cdot \text{área de construcción}
$$

Esto significa que:

- $w_0 = 52516.31$
- $w_1 = 185.82$.

### Ejemplo numérico

Si el área de construcción es 100, entonces:

$$
\text{precio} = 52516.31 + 185.82 \cdot 100 = 71098.31
$$

Si el área aumenta a 101:

$$
\text{precio} = 52516.31 + 185.82 \cdot 101 = 71284.13
$$

La diferencia es 185.82, así que una unidad adicional en el área de construcción incrementa el precio esperado en esa misma cantidad.

## 7. Interpretación de los coeficientes

### 7.1. Pendiente $w_1$

La pendiente indica cuánto cambia el valor esperado de la variable dependiente cuando la variable independiente aumenta en una unidad.

- Si $w_1 > 0$, la relación es positiva.
- Si $w_1 < 0$, la relación es negativa.

En el ejemplo del inmueble, la relación es positiva: al aumentar el área de construcción, aumenta el precio estimado.

### 7.2. Intercepto $w_0$

El intercepto representa el valor estimado de la variable dependiente cuando la variable independiente vale cero.

En la práctica, muchas veces no tiene interpretación útil, porque el valor cero de la variable independiente puede no ser válido en el contexto del problema.

Solo tiene sentido interpretarlo si cero es un valor posible y válido para la variable explicativa.

## 8. Significancia estadística de los coeficientes

Además de interpretar el valor de los coeficientes, conviene evaluar si son estadísticamente significativos.

Para ello se usa la prueba t de Student sobre cada coeficiente.

Para $w_1$:

$$
H_0: w_1 = 0
$$

$$
H_a: w_1 \neq 0
$$

Interpretación del p-valor:

- Si el p-valor $\leq \alpha$, se rechaza $H_0$ y el coeficiente se considera estadísticamente significativo.
- Si el p-valor $> \alpha$, no hay evidencia suficiente para rechazar $H_0$.

### Ejemplo con el modelo del inmueble

| Atributo | Coeficiente | Estadístico t | p-valor |
|---|---:|---:|---:|
| Área de construcción | 185.82 | 8.256 | 0.000 |
| Intercepto | 52516.31 | 1.358 | 0.181 |

Si se usa un nivel de significancia $\alpha = 0.05$, entonces el coeficiente del área de construcción es significativo porque su p-valor es menor que $\alpha$.

## 9. Resumen

- La regresión lineal modela la relación entre una variable dependiente y una o más variables explicativas mediante una combinación lineal.
- En regresión lineal simple solo existe una variable predictora y el modelo es una recta.
- El algoritmo aprende los parámetros $w_0$ y $w_1$ buscando minimizar una función de costo, típicamente el MSE.
- La pendiente $w_1$ indica cuánto cambia la predicción ante una variación de una unidad en la variable independiente.
- El intercepto $w_0$ suele tener poca interpretación práctica, salvo que cero sea un valor válido en el contexto.
- La significancia estadística de los coeficientes se evalúa con el p-valor y un nivel de significancia $\alpha$.

## 10. Referencias

- Coursera, *Modelos predictivos con aprendizaje automático*, video “Regresión lineal simple”. https://www.coursera.org/learn/modelos-predictivos-con-aprendizaje-automatico/lecture/EAlOD/regresion-lineal-simple
- Bruce, P., Bruce, A., Gedeck, P. (2020). *Practical Statistics for Data Scientists. 50+ Essential Concepts Using R and Python*. Second edition. O'Reilly Media. Capítulo 4.
- James, G., Witten, D., Hastie, T., Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. Capítulo 3.