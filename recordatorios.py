import os

os.system('clear')

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


#####Cambios a realizar

# Añadir recordatorios:

recordatorio_1 = ['2021-01-02', '06:00', 'Empezar el año']
recordatorio_2 = ['2021-12-24', '22:00', 'Cena de Navidad']
recordatorio_3 = ['2021-12-31', '22:00', 'Cena de Año Nuevo']

recordatorios.insert(1, recordatorio_1)
recordatorios.insert(5, recordatorio_2)
recordatorios.insert(7, recordatorio_3)

#Quitar error 15 de Julio:

recordatorios[3][0] = recordatorios[3][0].replace('15', '16')

# Eliminar evento dia del trabajo:

recordatorios.pop(2)


# Output

for i in recordatorios:
    print(i)
