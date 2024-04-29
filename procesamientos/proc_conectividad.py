import csv
import pathlib

ADSL = 4
LINK = 13

read_dataset = pathlib.Path('../datasets/Conectividad_Internet.csv')
write_dataset = pathlib.Path('../custom_datasets/Conectividad_Internet.csv')

def complete_values(line, reader):
    '''Completa los valores faltantes en las columnas entre ADSL y LINK con "NO".'''
    for column in reader.fieldnames[ADSL:LINK]:
        if line[column] == "--":
            line[column] = "NO"
    return line

def new_column(line, reader):
    '''Retorna "SI" si alguna de las columnas entre ADSL y LINK es "SI" y "NO" en caso contrario.'''

    return "SI" if any(line[column] == "SI" for column in reader.fieldnames[ADSL:LINK]) else "NO"

def create_new_file(read_dataset, write_dataset):
    with read_dataset.open(mode='r', encoding='utf-8') as read_file, \
         write_dataset.open(mode='w', encoding='utf-8') as write_file:
        
        reader = csv.DictReader(read_file)
        # Definir los nombres de las columnas, agregando la nueva columna "posee_conectividad"
        fieldnames = reader.fieldnames + ['posee_conectividad']
        
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in reader:
                        
            line = complete_values(line, reader)

            line['posee_conectividad'] = new_column(line, reader)

            writer.writerow(line)

if __name__ == '__main__':
    create_new_file(read_dataset, write_dataset)

