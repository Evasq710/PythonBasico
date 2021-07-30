class Usuario:
    #Metodo constructor que se inicia cada vez que se crea una instancia
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    # no es necesaria la palabra 'self', puede ser cualquiera, por ser el primer argumento del método
    def saludo(self):
        print('Nombre y Apellido:', self.nombre, self.apellido)

#Herencia de la clase Usuario:
#HEREDA EL CONSTRUCTOR INIT CON SUS ATRIBUTOS Y TODOS SUS MÉTODOS
class Admin(Usuario):
    def superSaludo(self):
        print('Me llamo', self.nombre, self.apellido, 'y soy ADMIN xd')

# === EXTENDIENDO EL MÉTODO INIT DE LA CLASE PADRE EN LAS CLASES HIJAS:
# FORMA 1
class Profesor(Usuario):
    def __init__(self, nombre, apellido): # Al definir un __init__, se ignorará el __init__ de la clase padre
        Usuario.__init__(self, nombre, apellido) #Esto para indicar que se quiere ejecutar el __init__ de la clase padre
        print('Aquí se puede extender el __init__ de la clase padre')

# FORMA 2
class Alumno(Usuario):
    def _init__(self, nombre, apellido):
        super().__init__(nombre, apellido) # super() hace referencia a la clase padre, no hace falta el self
        print('Aquí también se puede extender el __init__ de la clase padre')



usuario1 = Usuario('Felipe', 'Perez')
usuario2 = Usuario('Juan', 'Martinez')

usuario1.saludo()
usuario2.saludo()
usuario2.nombre = 'NombreCambiado'
usuario2.saludo()
# del usuario2.nombre
# del usuario2

admin = Admin('Admin', 'Mamon')
admin.saludo()
admin.superSaludo()

profe = Profesor('Nomb_Profe1', 'Ape_Profe1')
profe.saludo()