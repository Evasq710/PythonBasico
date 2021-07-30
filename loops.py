i = 0
while i < 5:
    i += 1
    if i == 3:
        continue # Continúa en el siguiente bucle del while, ignorando el código debajo
        # break
    # print(i)

# == FOR LOOP ==
# Para iterar en listas, tuplas, diccionarios, etc
usuarios = ['Chanchito', 'Felipe', 'Roberto', 'Nicolas']
for usuario in usuarios:
    if usuario == 'Roberto':
        continue # Continúa en la siguiente iteración
        # break
    print(usuario)
#Iterar en los caracteres de un String:
user = 'Chancho Feiz'
for caracter in user:
    print(caracter)
# Con Range:
for x in range(6): # 0-5
    print(x)
else:
    print('SE HA TERMINADO EL FOR 1')
for y in range(3, 6): # 3-5
    print(y)
else:
    print('SE HA TERMINADO EL FOR 2')
for z in range(3, 30, 5): #último argumento para indicar el paso
    print(z)
else:
    print('SE HA TERMINADO EL FOR 3')