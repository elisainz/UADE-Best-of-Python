'''Escribir un programa que permita ingresar cadenas de caracteres hasta una cadena vacia utilizando la estructura while-true.
Generar un archivo que contenga cada registro la frase ingresada seguida de dos puntos y
la cantidad de caracteres que contiene
(no contar espacios)
la frase debe estar en el archivo solo con la primera letra de cada palabra en mayúscula y el resto en minúscula.'''

'''Entrada:
cadenas de caracteres'''

'''Salida:
archivo que contenga cada registro la frase ingresada seguida de dos puntos y
la cantidad de caracteres que contiene, con la primera letra de cada palabra en mayúscula y el resto en minúscula'''


def getCantCaracteres(frase):
    return len(frase.replace(" ","")) #quitamos los espacios de la frase y devolvemos la longitud del string que nos queda

def formatear(frase):
    return frase.lower().title() #ponemos todas las letras en minuscula y luego sobre ese string llamamos a title(),
                                 #que pone la primera letra de cada palabra del string en mayuscula

def registrarFrases():
    frases = []
    while True:
        cad = input("Ingrese una cadena (o vacia para finalizar): ")
        if cad == "":
            break
        frases.append(cad)

    try:
        arch = open(r"frases.txt","wt")

        for frase in frases:
            arch.write(formatear(frase)+":"+str(getCantCaracteres(frase))+"\n")
    except IOError:
        print("Hubo un problema al abrir el archivo")
    finally:
        print("Cadenas escritas correctamente!")
        arch.close()


registrarFrases()
