#Matias Soria 8/04/2026
""" primer_nombre, primer_apellido, pais, edad, estado_civil = 'Matias' , 'Soria' , 'Ecuador' , '16' , 'soltero'
print (primer_nombre, primer_apellido, edad, estado_civil)
print ('primer_nombre:', primer_nombre)
print ('primer_apellido:', primer_apellido)
print ('edad:', edad)
print ('estado_civil:', estado_civil)"""

#Matias Soria, 10/04/2026 EJERCICIOS VARIABLES
# %%
nombre = "Matias"
apellido = "Soria"
nombreCompleto = nombre + apellido
pais = "Ecuador"
ciudad = "Quito"
edad = 16
anio = 2026
estaCasado = False
esVerdadero = True
luzEncendida = False

# Declarar varias variables en una sola línea
x, y, z = "uno", "dos", "tres"

# 1. Comprobar tipo de dato de todas las variables

print("Tipo de nombre:", type(nombre))
print("Tipo de apellido:", type(apellido))
print("Tipo de nombreCompleto:", type(nombreCompleto))
print("Tipo de pais:", type(pais))
print("Tipo de ciudad:", type(ciudad))
print("Tipo de edad:", type(edad))
print("Tipo de anio:", type(anio))
print("Tipo de estaCasado:", type(estaCasado))
print("Tipo de esVerdadero:", type(esVerdadero))
print("Tipo de luzEncendida:", type(luzEncendida))
print("Tipo de x, y, z:", type(x), type(y), type(z))

# 2. Longitud de la variable nombre
long_nombre = len(nombre)
print("Longitud de nombre:", long_nombre)

# 3. Comparar longitud de nombre y apellido
long_apellido = len(apellido)
print("Longitud de apellido:", long_apellido)
print("¿Nombre tiene más caracteres que apellido?", long_nombre > long_apellido)

# 4-11. Operaciones aritméticas con numeroUno = 5 y numeroDos = 4
numeroUno = 5
numeroDos = 4

total = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
residuo = numeroDos % numeroUno  # residuo de dividir numeroDos entre numeroUno
potencia = numeroUno ** numeroDos
divisionEntera = numeroUno // numeroDos

print("total:", total)
print("diferencia:", diferencia)
print("producto:", producto)
print("division:", division)
print("residuo (numeroDos % numeroUno):", residuo)
print("potencia (numeroUno ** numeroDos):", potencia)
print("division entera (numeroUno // numeroDos):", divisionEntera)

# 12-14. Cálculos con radio = 30
import math

radio = 30  # metros
areaCirculo = math.pi * radio ** 2
circunferenciaCirculo = 2 * math.pi * radio

print("Radio:", radio)
print("Área del círculo:", areaCirculo)
print("Circunferencia del círculo:", circunferenciaCirculo)

# 15. Pedir al usuario el radio y calcular el área
try:
    radio_input = float(input("Ingrese el radio del círculo (m): "))
    area_input = math.pi * radio_input ** 2
    print("Área con radio ingresado:", area_input)
except ValueError:
    print("Entrada inválida para el radio.")

# 16. Usar input() para obtener nombre, apellido, pais y edad del usuario
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
pais_usuario = input("Ingrese su país: ")
edad_usuario = input("Ingrese su edad: ")

print("Usuario:", nombre_usuario, apellido_usuario, pais_usuario, edad_usuario)

# 17 help('keywords')

import keyword
#print(keyword.kwlist)