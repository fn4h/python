# Lista para almacenar los números
lista = []

# Solicitar la longitud de la lista, asegurándose de que sea mayor que 0
cantidad = 0
while cantidad <= 0:
    cantidad = int(input("¿Cuántos números quieres ingresar? (debe ser mayor que 0): "))
    if cantidad <= 0:
        print("Por favor, ingresa un número mayor que 0.")

# Ingresar los números en la lista
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    lista.append(numero)

# Menú de opciones a escoger
funcion = int(input("""Escoja una opción:
1. Sumatorio
2. Cuadrado de cada número
3. Promedio
> """))

# Realizar la operación según la opción seleccionada
if funcion == 1:
    respuesta = sum(lista)
    print("El total es", respuesta, ".")
elif funcion == 2:
    respuesta = [x ** 2 for x in lista]
    print("El cuadrado de todos los números es", respuesta, ".")
elif funcion == 3:
    respuesta = sum(lista) / len(lista)
    print("El promedio es", respuesta, ".")
else:
    print("Escoge una opción de la lista.")




    
