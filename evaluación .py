# ===== PARTE A =====

# Respuesta 1:
'''1. Análisis de datos y código (15 puntos)
Observa el siguiente código:
nombre = "Lucía"   
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))

Responde:
a) Indica el tipo de dato de cada variable.

-nombre: str (cadena de texto)
-edad: int (entero)
-promedio: float (número decimal)
-cursos: list (lista)

b) Escribe qué mostraría el programa en pantalla.

-<class 'str'>
-<class 'int'>
-<class 'float'>
-<class 'list'>
-5

c) Explica qué hace len(nombre).

-len(nombre) devuelve la longitud de la cadena de texto almacenada en la variable nombre,
es decir, el número de caracteres que contiene. En este caso, len(nombre) devolvería 5,
ya que "Lucía" tiene 5 caracteres (L, u, c, í, a).'''

# Respuesta 2:
'''a) ¿Qué diferencia hay entre print() e input()?

-print() se utiliza para mostrar información en la pantalla, mientras que
input() se utiliza para recibir información del usuario a través del teclado.

b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?

-porque no estaria declarando el tipo de dato, y por defecto se toma como string,
lo que puede causar errores si se intenta realizar operaciones matemáticas sin convertirlo a un tipo numérico.

c) Explica la diferencia entre /, // y %.

/ es la división normal que incluye decimales
// es la división entera con el cociente sin decimales
y % es el operador llamado "modulo" que devuelve el residuo de la división entre dos números.

d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.

-import sys

e) Escribe una instrucción que permita consultar las palabras reservadas de Python.

-import keyword'''

# ...

# ===== PARTE B =====

# Código corregido

'''El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione.

ancho = input("Ingrese el ancho del terreno: ")
largo = input("Ingrese el largo del terreno: ")
precio = input("Ingrese el precio por metro cuadrado: ")
area = ancho * largo
costo = area * precio
print("Área total: " + area)
print("Costo estimado: " + costo)

codigo corregido:

ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: " + str(area))
print("Costo estimado: " + str(costo))


a) ¿Cuáles eran los errores principales?

-los errores principales eran que las variables ancho, largo y precio
se estaban tomando como strings por el uso de input() sin convertirlos a un tipo numérico,
lo que causaba que las operaciones de multiplicación no funcionaran correctamente.
Además, al intentar imprimir area y costo, también se necesitaba convertirlos a strings 
para concatenarlos con el texto.

b) ¿Por qué tu corrección sí permite obtener resultados válidos?

-Porque al convertir las entradas del usuario a float, ahora se pueden realizar
operaciones matemáticas correctament, y al convertir los resultados a strings para imprimirlos,
se evita el error de concatenación entre tipos de datos diferentes.'''   

# Escribe un fragmento de código que haga lo siguiente:
'''
1. Cree la variable frase con el texto "Tecnología para todos".
2. Muestre la frase en mayúsculas.
3. Muestre la cantidad de caracteres de la frase.
4. Verifique si la palabra "Python" está dentro de la frase.
5. Reemplace "Tecnología" por "Programación".
6. Divida la frase en palabras usando split(). '''   

frase = "Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
print(frase.replace("Tecnología", "Programación"))
print(frase.split())


# ===== PARTE C =====

# Programa integrador

# ...