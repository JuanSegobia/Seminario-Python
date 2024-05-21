import csv
import pathlib

def reemplazo(line):
    for item in line:   #recorro cada item de la ciudad
        if line[item] == '///' or line[item] == '-':
            line[item] = 0

def modulo_punto4():

    read_dataset = pathlib.Path('../datasets/c2022_tp_c_resumen_adaptado.csv')
    write_custom_dataset = pathlib.Path('../custom_datasets/c2022_tp_c_resumen_adaptado.csv') 

    read_file = read_dataset.open(mode='r', encoding= 'utf-8')
    write_custom_file = write_custom_dataset.open(mode='w', encoding= 'utf-8', newline='')

    reader = csv.DictReader(read_file)
    campos = reader.fieldnames
    campos.append('Porcentaje de poblacion en situacion de calle')
    writer = csv.DictWriter(write_custom_file, fieldnames= campos)
    writer.writeheader()
        
    for line in reader:
        reemplazo(line)
        
        line['Porcentaje de poblacion en situacion de calle'] = (float(line['Población en situación de calle(²)']) / float(line['Total de población']) * 100)
        
        writer.writerow(line)

    read_file.close()
    write_custom_file.close()

if __name__ == '__main__':
    modulo_punto4()