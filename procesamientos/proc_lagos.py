import csv
import pathlib


def size(km: int):
    """Devuelve el tamaño según la superficie en kilómetros cuadrados."""
    if km <= 17:
        return 'chico'
    elif 17 < km <= 59:
        return 'medio'
    else:
        return 'grande'


def calculate_minutes(coords: str):
    """Calcula los minutos a partir de coordenadas en formato DMS."""
    minutes = coords.split("'")
    minutes = minutes[0]
    minutes = minutes.split('°')
    minutes = int(minutes[1])
    return minutes


def calculate_seconds(coords: str):
    """Calcula los segundos a partir de coordenadas en formato DMS."""
    seconds = coords.split('"')
    seconds = seconds[0]
    seconds = seconds.split("'")
    seconds = seconds[1]
    counter = len(seconds)
    if counter == 3:
        seconds = seconds[0] + seconds[1]
    elif counter == 2:
        seconds = seconds[0]
    seconds = int(seconds)
    return seconds


def calculate_grades(coords: str):
    """Calcula los grados a partir de coordenadas en formato DMS."""
    grades = coords.split('°')
    grades = int(grades[0])
    return grades


def coordinates(coords: str):
    """Convierte coordenadas en formato DMS a formato decimal."""
    direction = coords[-1]
    if direction == 'N' or direction == 'E':
        posORneg = '+'
    else:
        posORneg = '-'
    GD = posORneg + str(calculate_grades(coords) + calculate_minutes(coords) / 60 + calculate_seconds(coords) / 3600)
    return GD


def create_new_file():
    """Crea un nuevo archivo CSV procesando coordenadas y superficies."""
    read_dataset = pathlib.Path('../datasets/lagos_arg.csv')
    write_dataset = pathlib.Path('../custom_datasets/lagos_arg.csv')

    with read_dataset.open(mode='r', encoding='UTF-8') as read_file, \
         write_dataset.open(mode='w', encoding='UTF-8') as write_file:

        reader = csv.DictReader(read_file)
        addFieldnames = reader.fieldnames + ['Sup Tamaños', 'Latitud', 'Longitud']
        writer = csv.DictWriter(write_file, fieldnames=addFieldnames)
        writer.writeheader()

        for line in reader:
            coordenadas = line['Coordenadas'].split(' ')
            line['Latitud'] = coordinates(coordenadas[0])
            line['Longitud'] = coordinates(coordenadas[1])
            line['Sup Tamaños'] = size(int(line['Superficie (km²)']))
            writer.writerow(line)


if __name__ == '__main__':
    create_new_file()
