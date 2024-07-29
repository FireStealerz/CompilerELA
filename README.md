# Compilador para lenguaje de programación ELA

### Introducción

En el ámbito de la informática y el desarrollo de software, los compiladores juegan un papel crucial al traducir código fuente escrito en un lenguaje de programación de alto nivel a un lenguaje de máquina comprensible para el hardware de una computadora. Este proceso de traducción no solo permite que el software sea ejecutado, sino que también optimiza y verifica el código para mejorar su rendimiento y corregir errores.

El presente proyecto tiene como objetivo desarrollar un compilador funcional para un lenguaje de programación específico. Este compilador será capaz de realizar varias tareas fundamentales, incluyendo el análisis léxico, análisis sintáctico y análisis semántico.

### Informacion Tecinca y Especificaciones

Compilador para lenguaje ELA escrito en Python3. Este compilador se limita a las diferentes etapas de analizis, siendo el analisis lexico, sintactico y semantico, no se realizan mas etapas. Creado utilizando la libreria de (PLY - Lex - Yacc). Para los modulos de analisis lexico y sintactico.
Creado por:
* Edson Gutierrez
* Victor Alvarado
* Ivan Herran

### Identificadores aceptados
* Variable
* Constante



### Tipos de datos

<table>
  <thead>
    <tr>
      <th>Tipo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valor númerico entero</td>
    </tr>
    <tr>
      <td>Valor númerico decimal</td>
    </tr>
    <tr>
      <td>Caracter</td>
    </tr>
    <tr>
      <td>Cadena de caracteres</td>
    </tr>
  </tbody>
</table>

### Palabras reservadas
<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Palabara reservada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Variable</td>
      <td>var</td>
    </tr>
    <tr>
      <td>Constante</td>
      <td>const</td>
    </tr>
    <tr>
      <td>Valor númerico entero</td>
      <td>int</td>
    </tr>
    <tr>
      <td>Valor númerico decimal</td>
      <td>float</td>
    </tr>
    <tr>
      <td>Caracter</td>
      <td>char</td>
    </tr>
    <tr>
      <td>Cadena de caracteres</td>
      <td>string</td>
    </tr>
  </tbody>
</table>


### Operadores Aritmeticos
\+
\+
\*
/

### Operadores Relacionales
<
\>
<=
\>=
==

### Operadores Logicos
* or
* and
* true
* false

### Caracteres especiales 
* 0
* ; 
* {}
* ()

### Sentencias Controladores
* IF()
* WHILE()
* DO - WHILE()
* FOR(int x; x <= 0; x++)
* '''
