import csv
import os

# escribir un csv
# with open('archivos/archivo.csv', 'w', newline='') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(['twit_id', 'user_id', 'texto'])
#     writer.writerow([1000, 1, 'este es un twit'])
#     writer.writerow([1001, 2, 'este es otro twit'])


# leer un csv
# with open('archivos/archivo.csv', 'r') as archivo:
#     reader = csv.reader(archivo)
#     for fila in reader:
#         print(fila)

# actualizar un csv


with open('archivos/archivo.csv') as r, open('archivos/archivo_temp.csv', 'w', newline='') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for fila in reader:
        if fila[0] == "1000":
            writer.writerow([1000, 1, 'este es un twit modificado'])
        else:
            writer.writerow(fila)

os.remove('archivos/archivo.csv')
os.rename('archivos/archivo_temp.csv', 'archivos/archivo.csv')
