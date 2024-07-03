import csv
from validations import validar
#------------------------------------------- INCISO 1 -------------------------------------------
def airport_types(aeropuerto:csv.DictReader):
    """ Esta funcion lo que hace es crear una lista vacia, en la cual yo voy a ir agregando los tipos de aeropuertos
    que se encuentran en el dataset, verificando que no se repitan."""
    
    types = []
    for line in aeropuerto:
        value = line['type']
        if value not in types:
            types.append(value)
    return types

def informar_airport_types(airports:list):
    """ Esta funcion lo que hace es informar los tipos de aeropuertos que se encuentran en el dataset."""
    
    print(f''' En los tipos de aeropuertos encontramos distintos tipos: 
    \t➡️ Por tamaño: 
    \t\t🛩️ {airports[0]} - {airports[1]} - {airports[3]}
    \t➡️ Por situacion actual: 
    \t\t❌ {airports[2]}
    \t➡️ Por tipo:
    \t\t🚁 {airports[4]} - {airports[5]} ''')

#------------------------------------------- INCISO 2 -------------------------------------------
def airports_type_elevation(aeropuerto:csv.DictReader, elevation:str):
    """ Esta funcion lo que hace es crear una lista vacia, en la cual yo voy a ir agregando los aeropuertos, que se encuentran en la 
    elevacion que el usuario le ingresa por parametro."""
    
    airports_list = []
    for line in aeropuerto:
        if line['elevation_name'] == elevation:
            airports_list.append(line['name'])
    return airports_list

def informar_airports_elevations(airports:list, elevation:str):
    ''' Esta funcion lo que hace es informar los aeropuertos que cumplen la condicion.'''
    
    print(f''' \t \t 🔸 El tipo de elevacion elegida fue: {elevation} 🔸
    🛫 Los aeropuertos que se encuentran en esa elevacion son: ''')
    for airport in airports:
        print(f'🛩️: {airport}')

#------------------------------------------- INCISO 3 -------------------------------------------

def airports_by_condition_elevation(reader:csv.DictReader, elevation:int, condition:str):
    """ Esta funcion lo que hace es crear una lista vacia, en la cual yo voy a ir agregando los aeropuertos, que se encuentran en la 
    elevacion que el usuario le ingresa por parametro y que cumplen la condicion que el usuario le ingresa por parametro."""
    
    airports_list = []
    match condition:
        case 'mayor':
            for line in reader:
                elevation_ft = line['elevation_ft']
                if elevation_ft == "":
                    pass
                elif int(elevation_ft) > elevation:
                    airports_list.append(line['name'])
        case 'menor':  
            for line in reader:
                elevation_ft = line['elevation_ft']
                if elevation_ft == "":
                    pass
                elif int(elevation_ft) < elevation:
                    airports_list.append(line['name'])
    return airports_list


def informar_airports_elevations_condition(airports:list, elevation:int, condition:str):
    """ Esta funcion lo que hace es informar los aeropuertos que cumplen la condicion."""
   
    print(f''' \t \t 🔸 La elevacion elegida fue: {elevation} .ft 🔸
    🛫 Los aeropuertos que se encuentran {condition}es a {elevation}.ft son: ''')
    for airport in airports:
        print(f'🛩️: {airport}')

#------------------------------------------- INCISO 4 -------------------------------------------
def airports_lakes_connectivity_by_population(resumen_adaptado:csv.DictReader, airports:csv.DictReader, lakes:csv.DictReader, conectivity:csv.DictReader):
    '''Este proceso informa sobre aeropuertos, lagos y conectividades en base a la población de las provincias.
    Se informan con 2 inputs los cuales son un numero (ingresar poblacion) y un mayor o menor,
    que este sirve para informar respectivamente los datos mayores o menores al numero.
    '''
    number = int(input('Ingrese el numero de poblacion que desee: '))

    higher_or_lower = input('Ingrese si quiere buscar los datos mayores o menores a la poblacion ingresada (MAYOR / MENOR): ')

    provinces = []

    next(resumen_adaptado) # Paso al siguiente ya que el primero tiene la poblacion total.

    for line in resumen_adaptado:
        if higher_or_lower == 'mayor':
            if int(line['Total de población']) > number:
                provinces.append(line['Jurisdicción'].lower())
        if higher_or_lower == 'menor':
            if int(line['Total de población']) < number:
                provinces.append(line['Jurisdicción'].lower())

    print('Aeropuertos: ')

    for line in airports:
        if line['municipality'].lower() in provinces:
            print(f"ID: {line['id']}, Nombre: {line['name']}")
            
    print('Lagos: ')

    for line in lakes:
        if line['Ubicación'].lower() in provinces:
            print(f"Nombre: {line['Nombre']}, Ubicación: {line['Ubicación']}")

    print('Conectividades: ')

    for line in conectivity:
        if line['Provincia'].lower() in provinces:
            print(f"Provincia: {line['Provincia']}, Localidad: {line['Localidad']}")
#------------------------------------------- INCISO 5 -------------------------------------------
def airports_in_capitals(ar:csv.DictReader, airport:csv.DictReader):
    '''Este proceso busca e informa los aeropuertos que se encuentran en capitales.
    El proceso crea un diccionario donde las claves son ciudades y los valores son "si son o no capitales" (admin TRUE, minor FALSE).
    Luego, itera sobre los aeropuertos. Si la municipalidad/ubicacion/ciudad del aeropuerto está presente en el diccionario
    de capitales y es capital (admin), imprime la información de ese aeropuerto.
    '''

    capitals = {}

    for line in ar:
        capitals[line['city']] = line['capital']

    for line in airport:
        if line['municipality'] in capitals:
            if capitals[line['municipality']] == 'admin':
                print(f"ID: {line['id']} | Nombre: {line['name']} | Provincia: {line['prov_name']}")
#------------------------------------------- INCISO 6 -------------------------------------------
def lakes_by_surface_area(lakes:csv.DictReader):
    '''Esta funcion informa los lagos en base a un tamaño dado a traves de un input. (chico,medio,grande)'''
    tamaño = input('Ingrese un tamaño (chico,medio,grande):').lower()

    for line in lakes:
        if line['Sup Tamaños'] == tamaño:
            print(f"Nombre: {line['Nombre']}, Ubicación: {line['Ubicación']}, Tamaño: {line['Sup Tamaños']}")
#------------------------------------------- INCISO 7 -------------------------------------------

def top5_juridicciones(reader_resumen_adaptado:csv.DictReader):
    '''Esta funcion retorna una lista con las 5 jurisdicciones con mayor porcentaje de poblacion en situacion de calle'''
    next(reader_resumen_adaptado) #ignora la fila Total Pais

    rows = sorted(reader_resumen_adaptado, key=lambda x: float(x['Porcentaje de poblacion en situacion de calle'])) #ordena de manera ascendete segun Porcentaje de poblacion en situacion de calle 

    top_5_jurisdicciones = rows[-5:] #ultimas 5

    return top_5_jurisdicciones[::-1] #invertimos la lista asi queda de mayor a menor

#------------------------------------------- INCISO 8 -------------------------------------------

def gender_gap(reader_resumen_adaptado:csv.DictReader):
    '''Esta función retorna la juridisccion donde hay una mayor diferencia entre la cantidad de hombres y mujeres registrados al nacer,
    y también retorna cuán grande es esa diferencia. (retorna un str y un int)'''
    mayor_brecha_jurisdiccion = ""
    mayor_brecha = 0

    next(reader_resumen_adaptado) #ignora la fila Total Pais

    for row in reader_resumen_adaptado:                                 #calculo la brecha max, guardando ese max y la jurisdiccion
        poblacion_varones = int(row['Varones Total de población'])
        poblacion_mujeres = int(row['Mujeres Total de población'])
        brecha = abs(poblacion_varones - poblacion_mujeres)
        
        if brecha > mayor_brecha:
            mayor_brecha = brecha
            mayor_brecha_jurisdiccion = row['Jurisdicción']
            
    return mayor_brecha_jurisdiccion, mayor_brecha

#------------------------------------------- INCISO 9 -------------------------------------------

def connection_types(reader_conectividad:csv.DictReader):
    '''Esta funcion retorna una lista con los tipos de conectividad existentes'''
    encabezados_no_deseados = ["Provincia", "Partido", "Localidad", "Poblacion", "link", "Latitud", "Longitud", "posee_conectividad"] #me guardo los campos a ignorar

    conexiones = [encabezado for encabezado in reader_conectividad.fieldnames if not encabezado in encabezados_no_deseados] #agarro los campos de conexiones

    return conexiones
    
#------------------------------------------- INCISO 10 -------------------------------------------

def cant_Localidades_Conectividad (reader_conectividad:csv.DictReader):
    '''Esta funcion retorna un diccionario con todos los tipos de conectividad y la cantidad de localidades que la poseen'''
    ADSL = 4
    LINK = 13
    cant_conectividad = {} 
    fieldnames = reader_conectividad.fieldnames[ADSL:LINK]  # Lista con los tipos de conectividad

    for conectividad in fieldnames:  # inicializo el contador de cada conectividad en 0
        cant_conectividad[conectividad] = 0
        
    for line in reader_conectividad:  # recorro el archivo
        for clave in fieldnames:  # analizo los items cuyo indice estan en el diccionario, osea que sean tipos de conectividad
            if line[clave] == 'SI':
                cant_conectividad[clave] += 1

    return cant_conectividad

#------------------------------------------- INCISO 11 -------------------------------------------

def provincias_ciudades_con_fibraoptica (reader_ar:csv.DictReader, reader_conectividad:csv.DictReader):
    '''Esta funcion retorna los nombres de la provincias que tengan todas sus ciudades con fibra optica, si alguna ciudad no se conoce si tiene o no fibra optica se tendran en cuenta las demas que si tengan'''
    provCiudades = {}
    next(reader_ar)
    for line in reader_ar: # creo un diccionario cuya llave es el nombre de cada provincia y sus elementos todas las ciudades de dicha provincia
        nom_prov = validar(line['admin_name'].lower())
        if nom_prov not in provCiudades:  # utilizo la funcion validar ya que los nombres de las provincias en cada archivo son diferentes
            provCiudades[nom_prov] = [line['city']]
        else:
            provCiudades[nom_prov].append(line['city'])
    provCiudades['tierra del fuego'] = provCiudades.pop('tierra del fuego, antartida e islas del atlantico sur')  # arreglo el nombre de tierra del fuego para que se pueda comparar en ambos archivos

    provinciasConFibraOptica = {}
    for line in reader_conectividad:  # creo un diccionario cuya llave es el nombre de la provincia y su dato es true si todas las ciudades tienen fibra optica y false si al menos 1 no tiene
        if 'CABA' not in line['Provincia']:
            nom_prov = validar(line['Provincia']).lower()
            if line['Localidad'] in provCiudades[nom_prov]:  # si la localidad pertenece a alguna ciudad de su capital
                if nom_prov not in provinciasConFibraOptica:
                    provinciasConFibraOptica[nom_prov] = True
                if line['FIBRAOPTICA'] == 'NO':
                    provinciasConFibraOptica[nom_prov] = False

    for prov in provinciasConFibraOptica:
        if provinciasConFibraOptica[prov] == True:
            print(f" 🔸 {prov}")

#------------------------------------------- INCISO 12 -------------------------------------------

def provincias_capitales_conectividad (reader_ar:csv.DictReader, reader_conectividad:csv.DictReader):
    '''Esta funcion retorna un diccionario cuya llaves son los nombres de la provincia y su valor su respectiva capital y ademas si posee conectividad, si no se encuentra la capital entonces dira conectividad desconocida'''
    capitales = {}
    next(reader_ar)
    for line in reader_ar:  # creo un diccionario el cual tiene como llave el nombre de cada provincia y como dato su respectiva capital
        if line['capital'] == 'admin':  # guardar el nombre de la provincia y su capital en variables para que sea mas facil de leer
            capitales[validar(line['admin_name'].lower())] = line['city']
    capitales['tierra del fuego'] = capitales.pop('tierra del fuego, antartida e islas del atlantico sur')  # arreglo el nombre de tierra del fuego de nuevo

    for line in reader_conectividad:  # recorro el archivo verificando si cada localidad pertenece a la capital de alguna provincia
        if line['Localidad'] in capitales.values():  # si la localidad pertenece a alguna capital
            if line['posee_conectividad'] == 'SI':
                capitales[validar(line['Provincia'].lower())] += ' posee conectividad'
            else:
                capitales[validar(line['Provincia'].lower())] += ' NO posee conectividad'

    for prov in capitales:  # recorro el diccionario para verificar si alguna ciudad no se encontro
        if 'conectividad' not in capitales[prov]:
            capitales[prov] = capitales[prov] + ' conectividad desconocida'

    return capitales