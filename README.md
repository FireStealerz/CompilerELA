# <img src="https://raw.githubusercontent.com/FireStealerz/CompilerELA/main/documentationGraphics/univaLogo.png" alt="Texto alternativo" width="30" height="32"> Universidad del Valle de Atemajac
---
**Fecha de publicación:** 06/08/2024

**Publicado por:** 
* Edson Rodriguez Rey
* Iván Herrán Silva
* Víctor Alvarado Pérez

---

## Secciones 

* [Introducción](#introducción)
* [Información técnica y especificaciones](#información-técnica-y-especificaciones)
* [Instalación y ejecución](#instalación-y-ejecución)
* [Estructura del lenguaje](#estructura-del-lenguaje)
  * [Tipos de datos](#tipos-de-datos)
  * [Variables](#variables)
  * [Operadores aritmeticos](#operadores-aritmeticos)
  * [Operadores relacionales](#operadores-relacionales)
  * [Caracteres especiales](#caracteres-especiales)
  * [Funcion de impresión](#funcion-de-impresión)
  * [Sentencias de control](#sentencias-de-control)

* [Ejemplos de casos de uso](#ejemplos-de-casos-de-uso)
  


---

## Introducción

En el ámbito de la informática y el desarrollo de software, los compiladores juegan un papel crucial al traducir código fuente escrito en un lenguaje de programación de alto nivel a un lenguaje de máquina comprensible para el hardware de una computadora. Este proceso de traducción no solo permite que el software sea ejecutado, sino que también optimiza y verifica el código para mejorar su rendimiento y corregir errores.

El presente proyecto tiene como objetivo desarrollar un compilador funcional para un lenguaje de programación específico. Este compilador será capaz de realizar varias tareas fundamentales, incluyendo el análisis léxico, análisis sintáctico y análisis semántico.

---

## Información técnica y especificaciones

Compilador para lenguaje ELA está escrito en Python3. Este compilador se limita a las diferentes etapas de analizis, siendo el analisis lexico, sintactico y semantico, no se realizan mas etapas. Creado utilizando la libreria de (PLY - Lex - Yacc). Para los modulos de analisis lexico y sintactico.

---

## Instalación y ejecución

El compilador necesita de los siguientes requerimientos para su instalación y funcionamiento: 

* **Sistema operativo:** Multiplataforma
* **Versión minima:** Python 3.12.6

**Para ejecutar el compilador**

1. Verifica la versión requerida por el proyecto. Para realizarlo puedes ejecutar el siguiente comando: 
`pip --version`

2. Instalación: Instala las dependencias listadas usando pip.
`pip install -r requirements.txt`

3. Entorno Virtual (Opcional pero Recomendado). Usar un entorno virtual (virtualenv) ayuda a aislar las dependencias del proyecto y evitar conflictos. Para activarlo asegurate de estar en la carpeta raiz del proyecto general y ejecuta el siguiente comando: 
`source venv/bin/activate`


---

## Estructura del lenguaje 


### Tipos de datos

A continuación, se presenta una guía básica sobre los tipos de datos y su uso.

* **Valor númerico entero:** Funciona para todos los valores númericos sin punto decimal. 
**Ejemplo:**
`1, 24, 64456`

* **Valor númerico decimal:** Funciona para para todos los valores númericos no enternos. Todos los casos llevan una 'f' al final.
**Ejemplo:**
`1.1f, 12.53f, 55.2432f`
* **Caracter**: Unidad básica de información puede representar una letra, número, símbolo. 
**Ejemplo:** 
`'H', 'o', 'l', y 'a'`
* **Cadena de texto**: Secuencia de caracteres que forman un conjunto de datos de texto. 
**Ejemplo:** 
`'Hola', 'Adios'`

---

### Variables
Una variable es capaz de contener cualquier tipo de dato del lenguaje de programación, para declarar una variable es necesario agregar un '$' antes del nombre de la variable seguida de un = para asginar el valor. 

```
$nombre_variable = 3.1416f

Ejemplo:
$pi = 3.1416f
```

---

### Operadores Aritmeticos

A continuación, se presenta una guía básica sobre los operadores aritméticos y su uso.

**Operador de Suma (+)** 
**Descripción:** Realiza la adición de dos valores numéricos.
**Uso:** a + b

```
$x = 5
$y = 3
resultado = x + y  # resultado es 8
```

**Operador de Resta (-)**
**Descripción:** Realiza la sustracción de dos valores numéricos.
**Uso:** a - b

```
$x = 5
$y = 3
resultado = x - y  # resultado es 2
```

**Operador de Multiplicación (*)**
**Descripción:** Realiza la multiplicación de dos valores numéricos.
**Uso:** a * b
```
$x = 5
$y = 3
resultado = x * y  # resultado es 15
```

**Operador de División (/)**
**Descripción:** Realiza la división de dos valores numéricos. El resultado es un número de punto flotante o entero.
**Uso:** a / b
```
$x = 10
$y = 2
resultado = x / y  # resultado es aproximadamente 5
```

**Operador de modulo (%)**
**Descripción:** Retorna el residuo de uan división. El resultado puede ser un número flotante o entero.
**Uso:** a % b
```
$x = 15
$y = 2
resultado = x % y  # resultado es aproximadamente 7.5
```

---

### Operadores Relacionales

A continuación, se presenta una guía básica sobre los operadores relacionales y su uso.

**Operador Menor que (<)**
**Descripción:** Compara si el valor a la izquierda es menor que el valor a la derecha.
**Uso:** a < b
**Retorno:** Devuelve True si a es menor que b; de lo contrario, devuelve False.
```
$x = 5
$y = 10
resultado = x < y  # resultado es True
```

**Operador Menor o Igual que (<=)**
**Descripción:** Compara si el valor a la izquierda es menor o igual que el valor a la derecha.
**Uso:** a <= b
**Retorno:** Devuelve True si a es menor o igual que b; de lo contrario, devuelve False.
```
$x = 5
$y = 5
resultado = x <= y  # resultado es True
```

**Operador Mayor que (>)**
**Descripción:** Compara si el valor a la izquierda es mayor que el valor a la derecha.
**Uso:** a > b
**Retorno:** Devuelve True si a es mayor que b; de lo contrario, devuelve False.
```
$x = 10
$y = 5
resultado = x > y  # resultado es True
```

**Operador Mayor o Igual que (>=)**
**Descripción:** Compara si el valor a la izquierda es mayor o igual que el valor a la derecha.
**Uso:** a >= b
**Retorno:** Devuelve True si a es mayor o igual que b; de lo contrario, devuelve False.
```
$x = 10
$y = 10
resultado = x >= y  # resultado es True
```

**Operador Igual a (==)**
**Descripción:** Compara si dos valores son iguales.
**Uso:** a == b
**Retorno:** Devuelve True si a es igual a b; de lo contrario, devuelve False.
```
$x = 5
$y = 5
resultado = x == y  # resultado es True
```

**Operador Diferente de (!=)**
**Descripción:** Compara si dos valores son diferentes.
**Uso:** a != b
**Retorno:** Devuelve True si a es diferente de b; de lo contrario, devuelve False.
```
$x = 5
$y = 10
resultado = x != y  # resultado es True
```

---

### Caracteres especiales 
* **Caracter ';' :** Utilizado para indicar el final de una instrucción o declaración.
```
Ejemplo:

int $x = 10;  // Fin de la declaración
$x = x + 5;   // Fin de la instrucción de asignación
```

* **Caracteres '{ }':** Utilizados para indiciar la agrupación de variables o valores. 

```
Ejemplo: 

$x1 = 2
$x2 = 3
$x3 = 4

a = {1,2,4,5,6}
b = {$x1, $x2, $x3 }

```

* **Caracteres '( )':** Utilizados para la agrupación de condciones: 

```
Ejemplo: 

if (a>b):
  condicion
```

---

### Funcion de impresión 
**Descripción:** Se utiliza para mostrar datos en la consola o salida estándar. Permite al programador ver el valor de variables, mensajes, o resultados durante la ejecución del programa.
```
Ejemplo 
$text = "Hola mi nombre es Julito"

print("Hola") #Salida "Hola"
print($text) #Salida "Hola mi nombre es Julito"
```

---

### Sentencias de control

**If-else**
**Descripción:** Se utiliza para ejecutar diferentes bloques de código según si una condición es verdadera o falsa.

```
Ejemplo: 

x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x es 5 o menor")
```

**Do-while**
**Descripción:** Ejecuta un bloque de código al menos una vez y luego repite la ejecución mientras una condición sea verdadera.
```
Ejemplo: 
 
$x = 0;
do {
    printf("%d\n", $x);
    $x++;
} while ($x < 5);

```

**For**
**Descripción:** Ejecuta un bloque de código un número específico de veces, controlado por un contador.
```
Ejemplo: 

for ($x; $x <= 0; $x++)
  print("hello")
```

---

### Ejemplos de casos de uso

A continuación se muestras ejemplos de casos de uso para el uso del lenguaje de programación ELA. 

```
Ejemplo incorrecto: 


```

```
Ejemplo correcto:


```