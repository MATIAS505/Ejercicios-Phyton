nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
ancho = float(input("Ingrese el ancho de la pared (m): "))
alto = float(input("Ingrese el alto de la pared (m): "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * alto
costo_total = area * precio
nombre_completo = f"{nombre} {apellido}"
print(f"""Reporte final:
Nombre completo: {nombre_completo}
Área calculada: {area} m²
Costo total: ${costo_total:.2f}
""")
print(nombre_completo.upper())
print(f"Longitud del nombre completo: {len(nombre_completo)}")
# Verifica si la letra 'a' está en el nombre completo
contiene_a = 'a' in nombre_completo
	print("El costo total es mayor que 100.")
if costo_total > 100:
	print("El costo total es mayor que 100.")
else:
	print("El costo total NO es mayor que 100.")
