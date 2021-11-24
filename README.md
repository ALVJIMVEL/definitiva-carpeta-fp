[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5979465&assignment_repo_type=AssignmentRepo)
# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<2021\>/\<2022\>)
Autor/a: \<ÁLVARO v JIMÉNEZ VELÁZQUEZ\>   uvus:\<ALVJIMVEL>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.
Este dataset trata información sobre los valores del mercado de una moneda virtual durante su apertura y cierre contando sus máximos y mínimos ofrenciéndonos la información más relevante sobre el mismo(trabajo actualmente con un csv limitado, debido a que estoy haciendo modificaciones como la creación de nuevas variables para hacerlo más completo y venía con algunos errores).

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<funciones_de_proyecto.py\>**: Describe aquí el módulo principal.
  * **\<test_de_las_funciones.py\>**: Describe aquí el módulo de pruebas.
  * **\<modulo2.py\>**: Añade descripciones para el resto de módulos que pueda tener tu proyecto. Por ejemplo, sería conveniente tener un módulo separado con funciones genéricas para dibujar gráficas y/o otro con funciones genéricas de conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<Ethereum Historial Data.csv\>**: Añade una descripción genérica del dataset.
    * **\<dataset2.csv\>**: Añade una descripción del resto de datasets que puedas tener.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<N\> columnas, con la siguiente descripción:

* **\<Date>**: de tipo \<datetime\>, representa.... el día en el que se producen el resto de datos en el mercado
* **\<Price>**: de tipo \<float\>, representa.... el precio con el que cierra en el mercado
* **\<Open>**: de tipo \<float\>, representa el precio con el que se abre el mercado en un dia determinado
* **\<High>**: de tipo \<float\>, representa el precio más alto que obtiene durante un día determinado
* **\<Low>**: de tipo \<float\>, representa el precio más bajo que obtiene durante un día determinado
* **\<Vol.>**: de tipo \<float\>, representa el volumen de mercado durante un día determinado
* **\<Change %>**: de tipo \<float\>, representa el cambio a mejor o a peor en forma de porcentaje,es decir, sus subidas o bajadas
* **\<Problemas %>**: de tipo \<bool\>, representa si ese día hubo algun tipo de problema en el mercado
* **\<Paises %>**: de tipo \<str\>, representa el país que adquirió más cantidad en un determinado día
## Tipos implementados

Descrbe aquí la o las namedtuple que defines en tu proyecto.
Ethereum=namedtuple('Ethereum','Date, Price,Open, High, Low, Vol, Change, Problemas, Paises')

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<funciones_de_proyecto.py\>

* **<funcion_lectura>**: Descripción de la función 1. Nos recorre el csv creando una lista con todos sus datos
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test_de_las_funciones.py\>

* **<test_funcion_lectura>**: Descripción de las pruebas realizadas a la función 1. Comprobamos que la función funciona correctamente devolviendonos los 3 primeros datos del csv
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
