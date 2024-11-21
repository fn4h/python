import time
numero = int(input("Piensa en un número del 1 al 10: "))
if(numero<0):
    print("Mis trucos de adivinación sólo funcionan si el número es del 1 al 10!")
if(numero>10):
    print("Es un número demasiado grande!")
# Print iterations progress
def printProgressBar (iteration, total, prefijo = '', sufijo = '', decimales = 1, longitud = 100, fill = '█', printEnd = "\r"):
  
    porcentaje = ("{0:." + str(decimales) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(longitud * iteration // total)
    barra = fill * filledLength + '-' * (longitud - filledLength)
    print(f'\r{prefijo} |{barra}| {porcentaje}% {sufijo}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


# A List of Items
items = list(range(0, 43))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefijo = 'Adivinando:', sufijo = 'Completado', longitud = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefijo = 'Adivinando:', sufijo = 'Completado', longitud = 50)



print("Listo! Has pensado en el", numero,".")
