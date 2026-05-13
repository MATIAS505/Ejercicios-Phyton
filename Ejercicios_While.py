#Ejercicio 1.
"""numero = int(input("Ingrese un número entero: "))
suma=0
control=1
while numero < 0:
    print("ingrese un número positivo")
    numero = int(input("Ingrese un número entero: "))    
while control <= numero:
    suma += control
    control += 1

print(f"La suma de los números enteros desde 1 hasta {numero} es: {suma}")"""




suma=0

while True:
    precio=int(input("Ingrese el precio de el producto "))
    if precio <=0:
        break
    suma = suma + precio 
print("el precio total es", suma)





