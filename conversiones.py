import sys
import os

os.system("clear")
try:
    if len(sys.argv) != 5:
        print("Argumento no válido\nIntenta la forma: nombre_archivo.py tasa_conv_soles tasa_conv_peso_argentino tasa_conv_dolar pesos_chilenos_a_convertir\n")
        exit()

    tasa_sol = float(sys.argv[1])
    tasa_arg = float(sys.argv[2])
    tasa_dolar = float(sys.argv[3])
    clp = int(sys.argv[4])

    soles = clp * tasa_sol
    argentinos = clp * tasa_arg
    dolares = clp * tasa_dolar

    print(f"Los {clp} pesos equivalen a:\n{soles} Soles\n{argentinos} Pesos Argentinos\n{dolares} Dólares")
      

except ValueError:
    print("Argumento no válido\nIntenta la forma: nombre_archivo.py tasa_conv_soles tasa_conv_peso_argentino tasa_conv_dolar pesos_chilenos_a_convertir\n")
    exit()