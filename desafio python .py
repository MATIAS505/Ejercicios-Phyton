


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
puntaje = float(input("Ingrese su puntaje: "))
asistencia = float(input("Ingrese su porcentaje de asistencia: "))
codigo_invitacion = input("Ingrese su código de invitación: ")



nombre_mayusculas = nombre.upper()
caracteres_nombre = len(nombre.replace(" ", ""))
promedio = (puntaje + asistencia) / 2



if edad >= 14:
    if promedio >= 80:
        if codigo_invitacion == "PYTHON2026":
            resultado = "Acceso VIP"
        else:
            resultado = "Acceso general"
    elif 60 <= promedio < 80:
        resultado = "Acceso con observación"
    else:
        resultado = "No puede ingresar por bajo rendimiento"
else:
    if codigo_invitacion == "PYTHON2026":
        resultado = "Acceso especial con acompañante"
    else:
        resultado = "No cumple la edad mínima"



if puntaje >= 90 and asistencia >= 90:
    mensaje_adicional = "Candidato destacado"       
elif puntaje < 50 or asistencia < 50:
    mensaje_adicional = "Requiere refuerzo previo"
else:
    mensaje_adicional = "Sin mensaje adicional"



print(f"Participante: {nombre_mayusculas}")
print(f"Caracteres del nombre: {caracteres_nombre}")
print(f"Promedio general: {promedio:.2f}")
print(f"Resultado: {resultado}")
print(f"Mensaje adicional: {mensaje_adicional}")



