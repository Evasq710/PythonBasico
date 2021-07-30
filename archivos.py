# Modulo para eliminar archivos y carpetas dentro del sistema operativo
import os

# c se vuelve en el archivo
c = open('chanchito.txt', 'a')
# segundo argumento String asigna los permisos que queremos tener con el archivo
# 'r'-READ Leer (por defecto)
# 'a'-APPEND Permite agregar al final más texto
# 'w'-WRITE Permite modificar el archivo completamente, si el archivo no existe, python CREA el archivo
# 'x'- Crea un archivo, si ya existe arrojará un error
# 'r+' - Lectura y escritura

# === LEYENDO UN ARCHIVO ===
# print(c.read()) # Lee la TOTALIDAD del archivo
# print(c.readline()) # Lee primera linea
# print(c.readline()) # Lee segunda línea
# print(c.readline()) # Lee tercera línea
# for x in c:
#     print(x) # x es cada una de las líneas del archivo

# === MODIFICANDO EL ARCHIVO ===
c.write('\nAgregamos una nueva linea al archivo')
# fue necesario el permiso 'a'-APPEND
# si se usaba el perimso 'w'-WRITE, hubiera modificado TODO el archivo, quedando solo la linea agregada

c.close()

# === ELIMINANDO EL ARCHIVO ===
if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
    print('Se eliminó el archivo correctamente')
else:
    print('El archivo no existe')

# === ELIMINANDO UNA CARPETA O DIRECTORIO ===
os.rmdir('micarpeta')