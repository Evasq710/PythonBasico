# IMPORTA UN MÓDULO, PARA ACCEDER A FUNCIONES Y VARIABLES CREADAS
import modulos as xs # as es para renombrar el módulo
# from modulos import saludo, mascotas # esto es para importar algo en específico del módulo

from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Juan')

c = CamelCase()
s = 'esta oracion necesita CamelCase!'
camelcased = c.hump(s)
print(camelcased)
# Esta Oracion Necesita CamelCase!