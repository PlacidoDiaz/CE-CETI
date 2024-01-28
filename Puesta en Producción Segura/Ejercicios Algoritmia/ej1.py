def encontrar_mayor(a, b):
    if a > b:
        return a
    else:
        return b

def encontrar_menor(a, b):
    if a < b:
        return a
    else:
        return b

def sumar_numeros(a, b):
    return a + b

# Inicio del programa
print("Algoritmo para Determinar el Valor Mayor, Menor y Sumar Dos Números")

# Solicitar la introducción de dos valores
A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Asegurar que los valores sean distintos para los ejercicios de mayor y menor
while A == B:
    print("Los valores deben ser distintos para determinar el mayor y el menor.")
    A = float(input("Introduce el valor de A nuevamente: "))
    B = float(input("Introduce el valor de B nuevamente: "))

# Ejercicio a: Encontrar el mayor
mayor = encontrar_mayor(A, B)
print(f"El mayor entre {A} y {B} es: {mayor}")

# Ejercicio b: Encontrar el menor
menor = encontrar_menor(A, B)
print(f"El menor entre {A} y {B} es: {menor}")

# Ejercicio c: Sumar dos números
suma = sumar_numeros(A, B)
print(f"La suma de {A} y {B} es: {suma}")

