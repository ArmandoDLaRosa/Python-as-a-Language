"""
Crea una lista que contenga los números múltiplos de 3 o los números multiplos de 5 
entre el 1000 y 0, en orden descendente. 
    Por ejemplo, el 325 es mútiplo de 5, por lo que debe de estar en la lista. 
    El 936 es múltiplo de 3, por lo que debe de ir en la lista. 
    El 675 es múltiplo de 3 y de 5, por lo que debe de estar en la lista.

Crea una lista que contenga las palabras "fizz" y "buzz" en base a la lista anterior. 
    Si el número es múltiplo de 3 entonces agrega la palabra "fizz" y si el número es
       múltiplo de 5 entonces agrega la palabra "buzz". 
    Si el número es múltiplo de 3 Y de 5, como el caso de 675, entonces agrega la
       palabra "fizzbuzz".
"""

# Crear lista vacía
respuestaUno = []
# For con range en reversa entre 0 y 1000
for number in range(999, 0, -1):
    # Un múltiplo indica que el residuo debe ser 0
    # Módulo nos dice el residuo
    if(number % 5 == 0 or number % 3 == 0 ):
        respuestaUno.append(number)
print(respuestaUno)

# Crear lista vacía
respuestaDos = []
# For con range en reversa
for number in respuestaUno:
    # Un múltiplo indica que el residuo debe ser 0
    # Módulo nos dice el residuo
    if(number % 5 == 0 and number % 3 == 0 ):
        respuestaDos.append("fizzbuzz")

    elif(number % 5 == 0 ):
        respuestaDos.append("buzz")
    
    elif(number % 3 == 0):
        respuestaDos.append("fizz")

print(respuestaDos)

