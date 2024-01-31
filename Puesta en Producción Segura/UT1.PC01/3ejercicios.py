"""
 Ejercicio 2.4
 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
 contrario devuelve False.
"""

def vocalChecker(char):
    if char in 'aeiouAEIOU':
        return True
    else:
        return False


if __name__ == '__main__':
    print(vocalChecker('h'))

"""
Actividad 1. Palindromo
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría
que devolver True.
"""


def es_palindromo(string):
    if string == string[::-1]:
        return True


if __name__ == '__main__':
    es_palindromo("radar")

"""
Actividad 3. Clase persona
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad, DNI,
teléfono y email. Construye los siguientes métodos para la clase:
    ● Un constructor, donde los datos pueden estar vacíos.
    ● Los setters y getters para cada uno de los atributos. Importante: hay que validar
    las entradas de datos a través de sus correspondientes funciones.
    ● Método mostrar(): Muestra los datos de la persona.
    ● Método esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de
    edad.

"""


class Persona:
    def __init__(self, nombre="", edad=0, dni="", telefono="", email=""):
        self.nombre = nombre
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.edad = edad
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setDni(self, dni):
        self.dni = dni

    def getDni(self):
        return self.dni

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def mostrar(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + str(self.edad))
        print("DNI: " + self.dni)
        print("Teléfono: " + self.telefono)
        print("Email: " + self.email)

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False


if __name__ == '__main__':
    persona1 = Persona("Naim", 21, "12345678A", "123456789", "Naim@gmail.com")
    persona1.mostrar()
    print(persona1.esMayorDeEdad())

