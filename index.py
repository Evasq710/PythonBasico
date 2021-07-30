#==MULTIPLES VARIABLES==
a, b, c = "Lala", "Lele", "Lili"
# print(a, b, c)
# print(c, b, a)
valor1 = valor2 = valor3 = "Chancho Feliz"
# print(valor1, valor2, valor3)

#==CONCATENACIÓN==
inicio="Hola"
final="Mundo"
# print(inicio + final)
# print(inicio, final)

#==VARIABLES==
palabra = "hola" #string
entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j
# print(palabra, entero, conDecimales, complejo)

print(palabra[::-1]) # para darle vuelta a un String
print(palabra[0:2]) # RESULTADO: ho
print(palabra[2:4]) # RESULTADO: la

#==LISTAS==
lista=['primero', 'segundo', 'tercero'] #pueden no ser todos los elementos del mismo tipo
lista2 = lista.copy() #copia el contenido de una lista a otra
lista.append('cuarto') #agrega un elemento al final de la lista
# lista.clear() #elimina todos los elementos de la lista
# print(lista, lista2.count('primero')) #count retorna la cantidad de veces que se repite un valor en la lista
# print(len(lista)) # len tamaño de la lista
# print(lista[0]) #retorna el primer elemento de una lista
# lista.pop() #elimina el último elemento de la lista
# lista.remove('primero') #elimina UN elemento por su valor (el primero que encuentre)
lista.reverse() #invierte el orden de la lista
lista.sort() #Para ordenar las listas, deben tener el mismo tipo de datos
# print(lista)

#==TUPLAS==
tupla = ('hola', 'mundo', 'somos', 'tupla') #Estas NO SON MODIFICABLES
# print(tupla, tupla.count('hola'), tupla.index('hola')) #index devuelve la posición del elemento (DEBE EXISTIR EL ELEMENTO)
listaDeTupla = list(tupla) #copia una tupla a una lista para modificarla
listaDeTupla.append('extra')
# print(listaDeTupla)

#==RANGE==
rango = range(6) #Longitud de el rango 0 - 5
# print(rango)

#==DICCIONARIOS==
diccionario = {
    "nombre": "Rigoberta",
    "raza": "Persa",
    'edad': 5
}
# print(diccionario['nombre']) #obtiene un valor del diccionario
# print(diccionario.get('raza')) #obtiene un valor del diccionario
diccionario['nombre'] = 'Floffy' # para cambiar el valor de un elemento
# print(len(diccionario))
diccionario['ronronea'] = 'Si' #Agrega un nuevo valor al diccionario
# print(diccionario)
copiaDiccionario = diccionario.copy() #copia de un diccionario
copiaDiccionario2 = dict(diccionario) #copia de un diccionario
# diccionario.pop('ronronea') #elimina el valor del diccionario por su nombre clave
# diccionario.popitem() #elimina el último valor agregado al diccionario
del diccionario['raza'] #elimina el valor del diccionario por su nombre clave
diccionario.clear() #elimina todos los elementos de un diccionario
# print(diccionario, copiaDiccionario)
gatitos = {
    "Fluffy": {
        'nombre': "Fluffy",
        'edad': 4
    },
    "Mamba": {
        'nombre': "Black Mamba",
        'edad': 12
    }
} #diccionarios anidados
print(gatitos)
perritos = dict(nombre="Lulu", edad=6, raza="Lhasa Apso") #crear diccionario con el constructor dict
print(perritos)

# input
dato = input('Ingrese un número: ')
 #parseo - try except
try:
    numero = int(dato)
    print('Se ingresó un entero')
except:
    print('No has ingresado un número entero')

# exit() detiene la ejecución de la aplicación al instante