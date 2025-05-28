import sys
import os

os.system("clear")

try:
    if len(sys.argv) != 2:
            print("Argumento inválido, prueba de la siguiente manera: nombre_archivo.py nombre_texto.txt\n")
            exit()

    archivo = sys.argv[1]

    with open(archivo, "r", encoding="utf-8") as t:
            texto = t.read()

    caract_dist = set(texto)
    texto_coma = texto.replace(",", "")
    sin_puntuacion = (texto_coma.replace(".", "")).lower()
    palab_dist = set(sin_puntuacion.split())

    print(f"El número de caracteres distintos es: {len(caract_dist)}")
    print(f"El número de palabras distintas es: {len(palab_dist)}")


    print('\nNota: Para el conteo de palabras se omitieron como palabras distintas\nlas palabras que van seguidas de un signo de puntuación o que inician\
          \ncon una mayúscula. Por ejemplo: "hola," "hola." "Hola" "hola" se contaron\ncomo una sola palabra.\n')


except FileNotFoundError:
       print("Archivo no encontrado...\nIntenta nuevamente\n")
       exit()
