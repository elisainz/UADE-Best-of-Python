'''Escribir un programa que juegue con el usuario a adivinar un número.
El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo.
Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar
es mayor o menor que el ingresado.
Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número.
Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y se lo contará como un intento más.'''

import random

def ingresarNumero():
    numero = int(input("Ingrese un número del 1 al 500: "))
    return numero

def adivinarNumero():
    cont_intentos = 0
    azar = random.randint (1, 500)
    while True: #True en vez de cont_intentos >= 0 porque el while siempre va a ser verdadero
        try:
            cont_intentos = cont_intentos + 1
            numero = ingresarNumero() #numero ingresado en la funcion ingresarNumero
            if azar < numero:
                print ("El número que debes adivinar es MENOR al ingresado")
            elif azar > numero:
                print ("El número que debes adivinar es MAYOR al ingresado")
            elif azar == numero:
                break
        except ValueError:
            #cont_intentos = cont_intentos -1 ? si no quisiera contar el error
            print("Error, se esperaba que ingrese un número entero.")

    if azar == numero:
        print("Genial, adivinaste con", cont_intentos, "intentos")
    
adivinarNumero()


