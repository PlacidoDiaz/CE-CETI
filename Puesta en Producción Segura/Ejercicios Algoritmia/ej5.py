import math

def calcular_area_volumen_cilindro(radio, altura):
    """Función para calcular el área y volumen de un cilindro."""
    area = 2 * math.pi * radio * (radio + altura)
    volumen = math.pi * radio**2 * altura
    return area, volumen

# Ejemplo de uso de la función para un cilindro
radio_cilindro = 5  # Puedes cambiar este valor
altura_cilindro = 10  # Puedes cambiar este valor

area_cilindro, volumen_cilindro = calcular_area_volumen_cilindro(radio_cilindro, altura_cilindro)
print("Área del cilindro:", area_cilindro)
print("Volumen del cilindro:", volumen_cilindro)


# a. Realiza un algoritmo que le permita determinar el área de un rectángulo. 

def calcular_area_rectangulo(base, altura):
    """Función para calcular el área de un rectángulo."""
    return base * altura

# Ejemplo de uso de la función para un rectángulo
base_rectangulo = 4  # Puedes cambiar este valor
altura_rectangulo = 6  # Puedes cambiar este valor

area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("Área del rectángulo:", area_rectangulo)

