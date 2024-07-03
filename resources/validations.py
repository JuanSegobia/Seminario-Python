#------------------------------------------- INCISO 2 -------------------------------------------
def check_elevation_str(elevation):
    ''' Esta funcion lo que hace es verificar que la elevacion que el usuario le ingresa por parametro sea valida.'''
    
    while elevation != 'bajo' and elevation != 'medio' and elevation != 'alto':
        print('❌ La elevacion ingresada no es valida, por favor ingrese "bajo", "medio" o "alto"')
        elevation = input('Ingrese la elevacion que desea: ')
    return elevation

#------------------------------------------- INCISO 3 -------------------------------------------
def check_elevation_int(elevation):
    ''' Esta funcion lo que hace es verificar que la elevacion que el usuario le ingresa por parametro sea valida.'''
    
    while type (elevation) != int:
        print('❌ La elevacion ingresada no es valida, por favor ingrese un valor numerico.')
        elevation = int (input('Ingrese la elevacion que desea: '))
    return elevation

def check_condition (condition):
    ''' Esta funcion lo que hace es verificar que la condicion que el usuario le ingresa por parametro sea valida.'''
    
    while condition != 'mayor' and condition != 'menor':
        print('❌ La condicion ingresada no es valida, por favor ingrese "mayor" o "menor"')
        condition = input('Ingrese la condicion que desea: ')
    return condition

# Agregue un if, ya que tambien se llama a esta funcion en validar respuestas y no todas las recibidas son Strings
def validar(word:str)-> str:  # Reemplaza las letras con acento de un string una sin acentos
    '''Esta funcion retorna el string en minusculas que se recibio y sin acentos'''
    if (type(word) == str):
        word = word.lower()
        tildes={"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
        for i in tildes:
            word = word.replace(i,tildes[i])
        return word
    

def exceptions(row, column_question, selected_theme):
    if selected_theme == "Aeropuertos": 
        if column_question == "Nombre de la Provincia":
            row[column_question].values[0] = row[column_question].values[0].replace(" (Autonomous City)","")
            row[column_question].values[0] = row[column_question].values[0].replace(" Province","")
        if column_question == "Nombre":
            row[column_question].values[0] = row[column_question].values[0].replace(" Airport","")
        if column_question == "Pies de Elevacion":
            row[column_question].values[0] = row[column_question].values[0].replace(".0","")