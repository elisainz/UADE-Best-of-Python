'''Leer las frases del archivo frases.txt y crear un nuevo archivo con las frases eliminando las palabras repetidas
de cada registro, dejando un solo ejemplar de cada una, ordenadas según su longitud y separadas por punto y coma.
Se adjunta un archivo de frases de ejemplo'''

'''Entrada:
frases'''

'''Salidas:
frases sin sus respectivas palabras repetidas (eliminandolas y dejando un solo ejemplar),
ordenadas según su longitud y separadas por punto y coma.'''

def main():
    try:
        archLectura = open(r"frases.txt","r")
        archEscritura = open(r"frasesFormatted.txt","wt")

        fraseUnformatted = archLectura.readline() #leemos una frase
        while fraseUnformatted:
            conjuntoPalabras = set(fraseUnformatted.split()) #obtenemos la lista de palabras de la frase y la transformamos en un conjunto para eliminar repetidos
            listaPalabras = list(conjuntoPalabras) #volvemos a transformar el conjunto a una lista para poder ordenar las palabras
            listaPalabras.sort(key=len) #ordenamos las palabras por longitud 

            #escribimos las palabras separadas por ;
            for palabra in listaPalabras:
                archEscritura.write(palabra+";")

            archEscritura.write("\n") #escribimos el salto de linea para luego imprimir la siguiente frase en una linea nueva
            fraseUnformatted = archLectura.readline() #leemos la siguiente frase

    except IOError:
        print("Hubo un problema al abrir el archivo")
    finally:
        print("Cadenas escritas correctamente!")
        archLectura.close()
        archEscritura.close()

main()