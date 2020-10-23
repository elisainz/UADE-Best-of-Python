'''Ejercicio: 
Contraseñas! En general las contraseñas a crear deben cumplir reglas por seguridad para que sean válidas.
Desarrolle un programa que ingrese contraseñas hasta ingresar una contraseña vacía.
A medida que se ingresan verifique e informe si cumple con las reglas:
No puede comenzar con número.
Debe contener al menos dos números, una letra mayuscula y una longitud de 8 caracteres mínimo.

Resolver utilizando exclusivamente manejo de excepciones y estructura While-True,
creando una nueva excepción o utilizando una existente (ValueError) cuando no cumpla alguno de las dos reglas,
mostrar mensaje aclaratorio correspondiente en cada caso.'''


class ComienzaConNumeroError(Exception):
    pass

class NoCumpleRequisitosError(Exception):
    pass


def ingresarContraseña():
    contraseña = input("Ingrese una contraseña: ")
    return contraseña

def verificarContraseña():
    contraseña = ingresarContraseña()
    while True:
        if contraseña == "":
            break
        elif contraseña != "":
            try:
                cont_numeros = 0
                cont_mayusculas = 0
                if contraseña[0].isdigit(): #verificar si el primer caracter es un numero
                    raise ComienzaConNumeroError
                if len(contraseña) < 8: #verificar si la longitud es menor a 8
                    raise NoCumpleRequisitosError
        
                for caracter in contraseña:
                    if caracter.isdigit():
                        cont_numeros = cont_numeros + 1 #contar la cantidad de numeros en la contraseña
                    if caracter.isupper():
                        cont_mayusculas = cont_mayusculas + 1 #contar la cantidad de mayusculas en la contraseña
                if cont_numeros < 2 or cont_mayusculas <= 0: 
                    raise NoCumpleRequisitosError
            
                else:
                    print("La contraseña es válida!")
            except ComienzaConNumeroError:
                print("No puede comenzar con número")
            except NoCumpleRequisitosError:
                print("No cumple con los requisitos de seguridad")
        
            contraseña = input("Ingrese otra contraseña: ")
        
verificarContraseña()

        



