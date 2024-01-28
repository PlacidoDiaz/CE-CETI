import math

def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

# Ejemplo de uso de la función
cateto_a = 3  # Puedes cambiar este valor
cateto_b = 4  # Puedes cambiar este valor

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
print("La hipotenusa es:", hipotenusa)




# b. Aquí te proporciono un algoritmo en Python para calcular el área de un cuadrado:

def calcular_area_cuadrado(lado):
    """Función para calcular el área de un cuadrado."""
    return lado * lado

# Ejemplo de uso de la función
lado = 4  # Puedes cambiar este valor para calcular el área de diferentes cuadrados

area = calcular_area_cuadrado(lado)
print("El área del cuadrado es:", area)