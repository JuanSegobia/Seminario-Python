#------------------------------------------- INCISO 1 -------------------------------------------
def airport_types(aeropuerto):
    ''' Esta funcion lo que hace es crear una lista vacia, en la cual yo voy a ir agregando los tipos de aeropuertos
    que se encuentran en el dataset, verificando que no se repitan.'''
    
    types = []
    for line in aeropuerto:
        value = line['type']
        if value not in types:
            types.append(value)
    return types

def informar_airport_types(airports):
    ''' Esta funcion lo que hace es informar los tipos de aeropuertos que se encuentran en el dataset.'''
    
    print(f''' En los tipos de aeropuertos encontramos distintos tipos: 
    \t➡️ Por tamaño: 
    \t\t🛩️ {airports[0]} - {airports[1]} - {airports[3]}
    \t➡️ Por situacion actual: 
    \t\t❌ {airports[2]}
    \t➡️ Por tipo:
    \t\t🚁 {airports[4]} - {airports[5]} ''')

#------------------------------------------- INCISO 2 -------------------------------------------
def airports_type_elevation(aeropuerto, elevation):
    ''' Esta funcion lo que hace es crear una lista vacia, en la cual yo voy a ir agregando los aeropuertos, que se encuentran en la 
    elevacion que el usuario le ingresa por parametro.'''
    
    airports_list = []
    for line in aeropuerto:
        if line['elevation_name'] == elevation:
            airports_list.append(line['name'])
    return airports_list

def informar_airports_elevations(airports, elevation):
    ''' Esta funcion lo que hace es informar los aeropuertos que cumplen la condicion.'''
    
    print(f''' \t \t 🔸 El tipo de elevacion elegida fue: {elevation} 🔸
    🛫 Los aeropuertos que se encuentran en esa elevacion son: ''')
    for airport in airports:
        print(f'🛩️: {airport}')

#------------------------------------------- INCISO 3 -------------------------------------------

def airports_by_condition_elevation(reader, elevation, condition):
    ''' Esta funcion lo que hace es crear una lista vacia, en la cual yo voy a ir agregando los aeropuertos, que se encuentran en la 
    elevacion que el usuario le ingresa por parametro y que cumplen la condicion que el usuario le ingresa por parametro.'''
    
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


def informar_airports_elevations_condition(airports, elevation, condition):
    ''' Esta funcion lo que hace es informar los aeropuertos que cumplen la condicion.'''
   
    print(f''' \t \t 🔸 La elevacion elegida fue: {elevation} .ft 🔸
    🛫 Los aeropuertos que se encuentran {condition}es a {elevation}.ft son: ''')
    for airport in airports:
        print(f'🛩️: {airport}')

#------------------------------------------- INCISO 4 -------------------------------------------
def punto4(resumen_adaptado,aeropuerto,lagos,conectividad):
    numero = input('Ingrese un numero: ')

    numero = int(numero)

    mayOmen = input('Ingrese mayor o menor: ')

    provinciasMayores = []

    next(resumen_adaptado) # Paso al siguiente ya que el primero tiene la poblacion total.

    for line in resumen_adaptado:
        if mayOmen == 'mayor':
            if int(line['Total de población']) > numero:
                provinciasMayores.append(line['Jurisdicción'].lower())
        if mayOmen == 'menor':
            if int(line['Total de población']) < numero:
                provinciasMayores.append(line['Jurisdicción'].lower())

    print('Aeropuertos: ')

    for line in aeropuerto:
        if line['municipality'].lower() in provinciasMayores:
            print(f"ID: {line['id']}, Nombre: {line['name']}")
            
    print('Lagos: ')

    for line in lagos:
        if line['Ubicación'].lower() in provinciasMayores:
            print(f"Nombre: {line['Nombre']}, Ubicación: {line['Ubicación']}")

    print('Conectividades: ')

    for line in conectividad:
        if line['Provincia'].lower() in provinciasMayores:
            print(f"Provincia: {line['Provincia']}, Localidad: {line['Localidad']}")
#------------------------------------------- INCISO 5 -------------------------------------------
def punto5(ar, aeropuerto):
    capitales = {}

    for line in ar:
        capitales[line['city']] = line['capital']

    for line in aeropuerto:
        if line['municipality'] in capitales:
            if capitales[line['municipality']] == 'admin':
                print(f"ID: {line['id']}, Nombre: {line['name']}")
#------------------------------------------- INCISO 6 -------------------------------------------
def punto6(lagos):
    tamaño = input('Ingrese un tamaño (chico,medio,grande):').lower()

    for line in lagos:
        if line['Sup Tamaños'] == tamaño:
            print(f"Nombre: {line['Nombre']}, Ubicación: {line['Ubicación']}, Tamaño: {line['Sup Tamaños']}")
#------------------------------------------- INCISO 7 -------------------------------------------

def top5_juridicciones(reader_resumen_adaptado):
    next(reader_resumen_adaptado) #ignora la fila Total Pais

    filas = sorted(reader_resumen_adaptado, key=lambda x: float(x['Porcentaje de poblacion en situacion de calle'])) #ordena las jurisdicciones de manera ascendete

    top_5_jurisdicciones = filas[-5:] #ultimas 5

    for jurisdiccion in reversed(top_5_jurisdicciones): #recorre al reves para que se lea de la mayor a la menor
        print(f"Jurisdicción: {jurisdiccion['Jurisdicción']}, Porcentaje: {jurisdiccion['Porcentaje de poblacion en situacion de calle']}")

#------------------------------------------- INCISO 8 -------------------------------------------

def informar_gender_gap(reader_resumen_adaptado):
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
            
    print(f"Jurisdicción con mayor brecha: {mayor_brecha_jurisdiccion}")
    print(f"Brecha poblacional: {mayor_brecha}")

#------------------------------------------- INCISO 9 -------------------------------------------

def informar_connection_types(reader_conectividad):
    encabezados_no_deseados = ["Provincia", "Partido", "Localidad", "Poblacion", "link", "Latitud", "Longitud", "posee_conectividad"] #me guardo los campos a ignorar

    conexiones = [encabezado for encabezado in reader_conectividad.fieldnames if not encabezado in encabezados_no_deseados] #agarro los campos de conexiones

    print("Tipos de conexciones:")
    print(conexiones)
    
#------------------------------------------- INCISO 10 -------------------------------------------

def validar(palabra:str)-> str:  # Reemplaza las letras con acento de un string una sin acentos
    tildes={"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    for i in tildes:
        palabra = palabra.replace(i,tildes[i])
    return palabra

def cant_Localidades_Conectividad (reader_conectividad):
    ADSL = 4
    LINK = 13
    cant_conectividad = {} 
    fieldnames = reader_conectividad.fieldnames[ADSL:LINK]  # Lista con los tipos de conectividad

    for conectividad in fieldnames:  # inicializo el contador de cada conectividad en 0
        cant_conectividad[conectividad] = 0
        
    for line in reader_conectividad:  # recorro el archivo
        for clave in fieldnames:  # analizo los items cuyo indice estan en el diccionario
            if line[clave] == 'SI':
                cant_conectividad[clave] += 1

    return cant_conectividad

#------------------------------------------- INCISO 11 -------------------------------------------

def provincias_ciudades_con_fibraoptica (reader_ar, reader_conectividad):
    provCiudades = {}
    next(reader_ar)
    for line in reader_ar:  # creo un diccionario cuya llave es el nombre de cada provincia y sus elementos todas las ciudades de dicha provincia
        if validar(line['admin_name'].lower()) not in provCiudades:  # utilizo la funcion validar ya que los nombres de las provincias en cada archivo son diferentes
            provCiudades[validar(line['admin_name']).lower()] = [line['city']]
        else:
            provCiudades[validar(line['admin_name']).lower()].append(line['city'])
    provCiudades['tierra del fuego'] = provCiudades.pop('tierra del fuego, antartida e islas del atlantico sur')  # arreglo el nombre de tierra del fuego para que se pueda comparar en ambos archivos

    provinciasConFibraOptica = {}
    for line in reader_conectividad:  # creo un diccionario cuya llave es el nombre de la provincia y su dato es true si todas las ciudades tienen fibra optica y false si al menos 1 no tiene
        if 'CABA' not in line['Provincia']:
            if line['Localidad'] in provCiudades[validar(line['Provincia']).lower()]:
                if validar(line['Provincia']).lower() not in provinciasConFibraOptica:
                    provinciasConFibraOptica[validar(line['Provincia']).lower()] = True
                if line['FIBRAOPTICA'] == 'NO':
                    provinciasConFibraOptica[validar(line['Provincia']).lower()] = False

    for prov in provinciasConFibraOptica:
        if provinciasConFibraOptica[prov] == True:
            print(prov)

#------------------------------------------- INCISO 12 -------------------------------------------

def provincias_capitales_conectividad (reader_ar, reader_conectividad):
    capitales = {}
    next(reader_ar)
    for line in reader_ar:  # creo un diccionario el cual tiene como llave el nombre de cada provincia y como dato su respectiva capital
        if line['capital'] == 'admin':  #guardar el nombre de la provincia y su capital en variables para que sea mas facil de leer
            capitales[validar(line['admin_name'].lower())] = validar(line['city'].lower())
    capitales['tierra del fuego'] = capitales.pop('tierra del fuego, antartida e islas del atlantico sur')  # arreglo el nombre de tierra del fuego de nuevo

    for line in reader_conectividad:  # recorro el archivo verificando si cada localidad pertenece a la capital de alguna provincia
        if validar(line['Localidad'].lower()) in capitales.values():
            if line['posee_conectividad'] == 'SI':
                capitales[line['Provincia'].lower()] += ' posee conectividad'
            else:
                capitales[line['Provincia'].lower()] += ' NO posee conectividad'

    for prov in capitales:  # recorro el diccionario para verificar si alguna ciudad no se encontro
        if 'conectividad' not in capitales[prov]:
            capitales[prov] = capitales[prov] + ' conectividad desconocida'

    return capitales