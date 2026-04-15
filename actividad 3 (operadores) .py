# Ejercicio 1: Declara tu edad como variable entera
edad = 25
print("Ejercicio 1 - Mi edad:", edad)

# Ejercicio 2: Declara tu estatura como variable decimal (float)
estatura = 1.75
print("Ejercicio 2 - Mi estatura:", estatura)

# Ejercicio 3: Calcular área de un triángulo
base = float(input("Ejercicio 3 - Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area_triangulo = 0.5 * base * altura
print(f"El área del triángulo es: {area_triangulo}")

# Ejercicio 5: Calcular perímetro de un triángulo
a = float(input("Ejercicio 5 - Ingresa el lado a del triángulo: "))
b = float(input("Ingresa el lado b del triángulo: "))
c = float(input("Ingresa el lado c del triángulo: "))
perimetro = a + b + c
print(f"El perímetro del triángulo es: {perimetro}")

# Ejercicio 6: Área y perímetro de un rectángulo
longitud = float(input("Ejercicio 6 - Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print(f"Área del rectángulo: {area_rectangulo}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo}")

# Ejercicio 7: Área y circunferencia de un círculo
radio = float(input("Ejercicio 7 - Ingresa el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print(f"Área del círculo: {area_circulo}")
print(f"Circunferencia: {circunferencia}")

# Ejercicio 9: Pendiente y distancia euclidiana entre puntos (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Ejercicio 9 - Pendiente:", pendiente)
print("Distancia euclidiana:", distancia)

# Ejercicio 11: Función y = x² + 6x + 9
# Probando diferentes valores de x
print("Ejercicio 11 - Función y = x² + 6x + 9")
for x in range(-10, 1):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
# Cuando y = 0, x = -3
print("Para y = 0, x debe ser -3")

# Ejercicio 12: Longitud de palabras y comparación booleana
palabra1 = "python"
palabra2 = "dragón"
longitud1 = len(palabra1)
longitud2 = len(palabra2)
print("Ejercicio 12 - Longitud de 'python':", longitud1)
print("Longitud de 'dragón':", longitud2)
print("¿Son iguales?", longitud1 == longitud2)

# Ejercicio 13: Verificar si "on" está en "python" y en "dragón"
print("Ejercicio 13 - 'on' en 'python':", "on" in "python")
print("'on' en 'dragón':", "on" in "dragón")
print("'on' en ambos (and):", "on" in "python" and "on" in "dragón")

# Ejercicio 14: Verificar si "jerga" está en la oración
oracion = "Espero que este curso no esté lleno de jerga."
print("Ejercicio 14 - 'jerga' en oración:", "jerga" in oracion)

# Ejercicio 15: Verificar si "on" está en "python" y en "dragon" (sin acento)
print("Ejercicio 15 - 'on' en 'python' y 'dragon':", "on" in "python" and "on" in "dragon")

# Ejercicio 16: Longitud de "python" convertida a float y string
texto = "python"
longitud_texto = len(texto)
print("Ejercicio 16 - Longitud de 'python':", longitud_texto)
print("Convertida a float:", float(longitud_texto))
print("Convertida a string:", str(float(longitud_texto)))

# Ejercicio 18: Verificar división entera de 7 entre 3
resultado = 7 // 3
print("Ejercicio 18 - 7 // 3 =", resultado)
print("¿Es igual a 2?", resultado == 2)
print("¿Es igual a int(2.7)?", resultado == int(2.7))

# Ejercicio 19: Comparar tipos de datos de "10" y 10
print("Ejercicio 19 - Tipo de '10':", type("10"))
print("Tipo de 10:", type(10))
print("¿Son iguales?", type("10") == type(10))

# Ejercicio 20: Verificar si int('9.8') es igual a 10
print("Ejercicio 20 - int('9.8'):", int('9.8'))  # Esto causará error
print("¿Es igual a 10?", int('9.8') == 10)

# Ejercicio 21: Calcular pago por horas trabajadas
horas = float(input("Ejercicio 21 - Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
pago_total = horas * tarifa
print(f"El pago total es: {pago_total}")

# Ejercicio 22: Calcular segundos vividos
años = int(input("Ejercicio 22 - Ingresa los años que has vivido: "))
segundos = años * 365 * 24 * 60 * 60
print(f"Has vivido {segundos} segundos")

# Ejercicio 23: Mostrar tabla
print("Ejercicio 23 - Tabla:")
print("1  1  1  1  1")
print("2  1  2  4  8")
print("3  1  3  9  27")
print("4  1  4  16 64")
print("5  1  5  25 125")