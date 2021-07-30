# Dentro de la función, es argumento
def imprimeDato(argumentoUno):
    print('Mi argumento es:', argumentoUno)
# Al llamar la función, es parámetro
imprimeDato('parametro 1')

def funcionTupla(*nombres): # * para cantidad variable de argumentos que se convierten en una TUPLA
    print('La TUPLA de nombres es:', nombres)
    print(nombres[0])
funcionTupla('Pa', 'Pe', 'Pi', 'Po', 'Pu')

#Otra sintaxis para llamar a una función por el nombre de los argumentos
def nombreCompleto(apellido, nombre):
    print(nombre, apellido)
nombreCompleto(nombre='Juan', apellido='Perez')

# **  Agrupa los argumentos de una función en un diccionario (keywords args)
def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])
nombreCompleto2(nombre='Jose', apellido='Martinez')

def funcion(argumento = 'Por Defecto'):
    print(argumento)
funcion('Argumento Cambiado')
funcion()

# Función que recorre una lista y retorna un valor
def concatena(lista):
    i = ''
    for elemento in lista:
        i = i + elemento
    return i
palabraConcatenada = concatena(['Chancho', 'Feliz'])
print(palabraConcatenada)