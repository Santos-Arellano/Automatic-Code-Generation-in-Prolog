# Pasos para la Generación de Código en Prolog
1. Instala SWI-Prolog 8.4.2.
2. Asegúrate de que el camino a SWI-Prolog esté en tus variables de sistema.
3. Clona el repositorio.
4. Crea un entorno virtual.
5. Instala `pyswipl`.
6. Lanza la interfaz e introduce el lenguaje deseado y las especificaciones.

Por ejemplo:

Lenguaje: cpp

Especificaciones: assign(x, 10), loop(i, 0, 5, [assign(sum, 'sum + i')]), if_else('x > 0', [assign(y, 'x - 1')], [assign(y, 'x + 1')])

# Flujo de Trabajo de Generación de Código en Prolog
1. **Resumen de Predicados**
    - **Predicado syntax/3**: Genera código basado en patrones especificados (Spec) y lenguaje (Lang).
    - **Predicado generate/3**: Orquesta el proceso de generación y maneja el éxito o el fracaso.
    - **Predicado generate_code/3**: Actúa como el punto de entrada principal para generar código para una lista de especificaciones (Specs) en un lenguaje especificado (Lang).
    
2. **Predicados Incorporados**
    - **findall/3**: Recoge todas las instancias de un término especificado que satisface un objetivo.
    - **format/2 y format/3**: Genera cadenas de texto formateadas.
    - **atom/1**: Convierte un término en un término atómico (un átomo).
    - **maplist/2**: Aplica un predicado a cada elemento de una lista.

3. **Capacidades de Generación de Código Anidado**
    Las capacidades de predicado recursivo de Prolog permiten la generación de código anidado, permitiendo estructuras de código complejas.

# Tareas Avanzadas
### a) Soporte para Múltiples Lenguajes Objetivo
Extiende el programa para soportar la generación de código para múltiples lenguajes objetivo (por ejemplo, Python, JavaScript).

### b) Generación de Código Interactiva
Crea una interfaz interactiva para especificar código de alto nivel y generar código de lenguaje objetivo.

### c) Optimización y Refactorización
Implementa técnicas de optimización para mejorar el código generado. Ejemplo: Combina múltiples asignaciones en una sola declaración cuando sea posible.

# Entrega
- Envía el archivo fuente de Prolog que contiene la sintaxis del lenguaje objetivo, el lenguaje de especificación y las funciones de generación de código.
- Incluye un archivo README con documentación y explicaciones.
- Proporciona un informe con casos de prueba y sus resultados.
- Haz y envía una presentación para explicar la solución.


Este programa es una interfaz gráfica de usuario (GUI) que permite a los usuarios especificar código de alto nivel y generar código en un lenguaje objetivo (C++ o Rust). Utiliza el lenguaje de programación lógica Prolog para definir la sintaxis del lenguaje objetivo y las reglas para generar el código.

La interfaz de usuario está construida con Tkinter, una biblioteca de Python para la creación de interfaces gráficas. Permite a los usuarios seleccionar el lenguaje objetivo, ingresar las especificaciones de código de alto nivel, y generar, copiar y visualizar el código generado. También proporciona una opción para cargar un archivo Prolog personalizado y una ventana de ejemplos para ayudar a los usuarios a entender cómo escribir las especificaciones.

Las reglas de Prolog definen la sintaxis del lenguaje objetivo y cómo generar el código a partir de las especificaciones de alto nivel. Cada regla de sintaxis toma una especificación (como una asignación, un bucle o una condición) y genera el código correspondiente en el lenguaje objetivo. La función generate_code toma una lista de especificaciones y genera el código para todas ellas.

Cuando el usuario hace clic en el botón "Generate Code", el programa construye una consulta Prolog con las especificaciones ingresadas y el lenguaje seleccionado, y luego ejecuta la consulta para generar el código. Si la generación de código es exitosa, el código se muestra en la interfaz de usuario. Si ocurre un error, se muestra un mensaje de error.
