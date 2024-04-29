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

