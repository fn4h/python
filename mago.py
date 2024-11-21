import time

def pedir_respuesta_valida1():
    while True:
        respuesta1 = input("""-Mago Zarathos-  ¡Hola! ¡Soy el Mago Zarathos!

> ¡Hola! (1)
> ¿Y tú quién eres? (2)
> """).strip()

        if respuesta1 in ["1", "2"]:
            return respuesta1  
        else:
            print("""-Mago Zarathos- No entiendo tu respuesta.
--------------------------------------------""")

def pedir_respuesta_valida11(nombre):  
    while True:
        respuesta11 = input(f"""-Mago Zarathos-  Me alegro de conocerte, {nombre}. ¿Te gustaría que
te hiciese un truco de magia?
    
> Sí (1)
> No (2)
> """).strip()

        if respuesta11 in ["1", "2"]:
            return respuesta11  
        else:
            print("""-Mago Zarathos- No te entiendo, a ver si aprendemos a hablar.
--------------------------------------------""")
            
def pedir_respuesta_valida2(nombre):  
    while True:
        respuesta2 = input(f"""-Mago Zarathos-  ¡Yo soy el mago más poderoso 
de todos los tiempos!
                       
>No te creo.
>En serio? ¿Qué puedes hacer?
>""").strip()

        if respuesta2 in ["1", "2"]:
            return respuesta2 
        else:
            print("""-Mago Zarathos- Soy poderoso pero si no me hablas bien no te voy a entender nunca!
--------------------------------------------""")

def printProgressBar(iteracion, total, prefijo='', sufijo='', decimales=1, longitud=50, fill='█', printEnd="\r"):
    porcentaje = ("{0:." + str(decimales) + "f}").format(100 * (iteracion / float(total)))
    longitudRellenada = int(longitud * iteracion // total)
    barra = fill * longitudRellenada + '-' * (longitud - longitudRellenada)
    print(f'\r{prefijo} |{barra}| {porcentaje}% {sufijo}', end=printEnd)

    if iteracion == total:
        print()

respuesta1 = pedir_respuesta_valida1()
if respuesta1 == "1":
    nombre = input("""-Mago Zarathos-  ¿Cómo te llamas?
> """)
    
    respuesta11 = pedir_respuesta_valida11(nombre)  
    if respuesta11 == "1":
        print("""-Mago Zarathos-  ¡De acuerdo! ¿Qué tal un truco de adivinación?
        Pensarás en un número, y te aseguro que lo adivinaré.""")
        time.sleep(2)
        numero = int(input("Piensa en un número: "))

        
        items = list(range(0, 100))
        total = len(items)

        for i, item in enumerate(items):
            
            if i < total // 3:
                prefijo = "Adivinando..."
            elif i < total // 2:
                prefijo = "Leyendo tu mente..."
            elif i < total * 0.75:
                prefijo = "Recibiendo información divina..."
            else:
                prefijo = "Creo... Creo que lo he adivinado."
            
            time.sleep(0.03)  
            printProgressBar(i + 1, total, prefijo=prefijo, sufijo="Completado.", longitud=50)
        
        print(f"-Mago Zarathos-  ¡Zarathos siempre gana! Has pensado en el {numero}.")

    elif respuesta11 == "2":
        print("-Mago Zarathos-  Pues nada, tú sabrás.")


elif respuesta1 == "2":
    respuesta2 = input("""-Mago Zarathos-  ¡Yo soy el mago más poderoso 
de todos los tiempos!
                       
>No te creo. (1)
>En serio? ¿Qué puedes hacer? (2)
>""")
    if respuesta2 == "1":
        print("""-Mago Zarathos-  ¿¡Que no?! ¡¿A que te convierto en una rata en un segundo
haciendo uso únicamente de mi pulgar?! O mejor, más pacífico y cómodo de programar, te lo
demuestro haciéndote una adivinanza. Para ello, pensarás en un número y yo lo adivinaré.""")
        time.sleep(4)
        numero = int(input("Piensa en un número:"))
        items = list(range(0, 100))

        total = len(items)

        for i, item in enumerate(items):
            
            if i < total // 3:
                prefijo = "Adivinando..."
            elif i < total // 2:
                prefijo = "Leyendo tu mente..."
            elif i < total * 0.85:
                prefijo = "Recibiendo información divina..."
            else:
                prefijo = "Creo... Creo que lo he adivinado."
            
            time.sleep(0.1)  
            printProgressBar(i + 1, total, prefijo=prefijo, sufijo="Completado.", longitud=50)
        print(f"-Mago Zarathos-  ¡Zarathos siempre gana! Has pensado en el {numero}.")
        
    if respuesta2 == "2":
        print(f"""-Mago Zarathos-  Me alegra que lo preguntes. ¿Qué te parece si te hago un truco de magia?
pensarás en el número que tú quieras, y yo lo adivinaré.""")
        time.sleep(3)
        numero = int(input("Piensa en un número:"))
        items = list(range(0, 100))

        total = len(items)

        for i, item in enumerate(items):
            
            if i < total // 3:
                prefijo = "Adivinando..."
            elif i < total // 2:
                prefijo = "Leyendo tu mente..."
            elif i < total * 0.85:
                prefijo = "Recibiendo información divina..."
            else:
                prefijo = "Creo... Creo que lo he adivinado."
            
            time.sleep(0.1)  
            printProgressBar(i + 1, total, prefijo=prefijo, sufijo="Completado.", longitud=50)
        print(f"-Mago Zarathos-  ¡Zarathos siempre gana! Has pensado en el {numero}.")

        