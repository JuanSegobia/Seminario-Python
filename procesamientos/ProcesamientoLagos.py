import csv
import pathlib

def size(km: int):
    if km <= 17:
        return 'chico'
    if km > 17 and km <= 59:
        return 'medio'
    if km > 59:
        return 'grande'

def calculateMinutes(coords: str): #EJEMPLO: "40°19'60""S" (buscando 19)
    minutes = coords.split("'") # Divide por ('), quedaria separado: (['40°19', '60S'])
    minutes = minutes[0] # Deja la primera parte del split, (40°19).
    minutes = minutes.split('°') # Divide por (°), quedaria separado: (['40', '19'])
    minutes = int(minutes[1]) # Deja solo la segunda parte y la convierte en integer para poder usarla en la cuenta: (19)
    return minutes

def calculateSeconds(coords: str): #EJEMPLO: "40°19'60""S" (buscando 60)
    seconds = coords.split('"') # Divide por ("), quedaria asi: (["40°19'60S"])
    seconds = seconds[0] # Le asigno la lista a seconds: (["40°19'60S"])
    seconds = seconds.split("'") # Divide en dos: (['40°19', '60S'])
    seconds = seconds[1] # Me quedo con la segunda parte: (60S)
    counter = 0 # Contador de chars para ver si es un numero de 2 digitos o 1 digito ya que estos no estan puestos con un 0 adelante.
    for s in seconds: 
        counter += 1 
    if counter == 3:
        seconds = seconds[0] + seconds[1] # Si son 3 chars, los segundos son 2 digitos, suman la primera pos y la segunda: (60)
    if counter == 2:
        seconds = seconds[0] # Si son 2 chars, los segundos es de 1 digito.
    seconds = int(seconds) # Convierte los segundos en integer.
    return seconds

def calculateGrades(coords: str): #EJEMPLO: "40°19'60""S" (buscando 40)
    grades = coords.split('°') # Divide la lista por (°): (['40', "19'60S"])
    grades = int(grades[0]) # Agarra el primer elemento de la lista (40) y lo convierte a integer.
    return grades

def coordinates(coords: str):
    direction = coords[-1] # El ultimo digito es la direccion asi que la guarda: (S)
    if direction == 'N' or direction == 'E':
        posORneg = '+'
    else:
        posORneg = '-'
    GD = posORneg + str(calculateGrades(coords) + calculateMinutes(coords) / 60 + calculateSeconds(coords) / 3600)
    return GD
    
def createNewFile():
    read_dataset = pathlib.Path('../datasets/lagos_arg.csv')
    write_dataset = pathlib.Path('../custom_datasets/lagos_arg.csv')

    read_file = read_dataset.open(mode='r', encoding='UTF-8')
    write_file = write_dataset.open(mode='w', encoding='UTF-8')

    reader = csv.DictReader(read_file)

    addFieldnames = reader.fieldnames + ['Sup Tamaños'] + ['Latitud'] + ['Longitud']
    
    writer = csv.DictWriter(write_file, fieldnames=addFieldnames)
    
    writer.writeheader()

    for line in reader:
        
        coordenadas = line['Coordenadas']

        coordenadas = coordenadas.split(' ')

        line['Latitud'] = coordinates(coordenadas[0])

        line['Longitud'] = coordinates(coordenadas[1])

        line['Sup Tamaños'] = size(int(line['Superficie (km²)']))

        writer.writerow(line)

    read_file.close()
    write_file.close()

if __name__ == '__main__':
    createNewFile() 