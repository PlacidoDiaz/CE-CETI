class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def esMayorDeEdad(self):
        return self.edad >= 18

# Ejemplo de uso
persona1 = Persona("Juan", 30, "12345678A")
persona2 = Persona("Ana", 17, "87654321B")

print(persona1.mostrar())
print(persona1.esMayorDeEdad())
print(persona2.mostrar())
print(persona2.esMayorDeEdad())
