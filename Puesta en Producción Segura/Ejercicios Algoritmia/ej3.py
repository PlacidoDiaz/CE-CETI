N = 0  # Inicializamos N en 0
Suma = 0  # Inicializamos la suma en 0

while N < 10:
    N = N + 1  # Incrementamos N
    Suma = Suma + N  # Acumulamos la suma

print(Suma)  

# Ejercicio a: Sumatoria de números enteros múltiplos de 5 entre 1 y 100
multiplos_5 = [i for i in range(1, 101) if i % 5 == 0]
sumatoria_multiplos_5 = sum(multiplos_5)
print("Números múltiplos de 5 entre 1 y 100:", multiplos_5)
print("Sumatoria de los múltiplos de 5:", sumatoria_multiplos_5)

# Ejercicio b: Sumatoria de números enteros pares entre 1 y 100
pares = [i for i in range(1, 101) if i % 2 == 0]
sumatoria_pares = sum(pares)
print("\nNúmeros pares entre 1 y 100:", pares)
print("Sumatoria de los números pares:", sumatoria_pares)

# Ejercicio c: Cantidad y sumatoria de números impares entre 1 y 300
impares = [i for i in range(1, 301) if i % 2 != 0]
cantidad_impares = len(impares)
sumatoria_impares = sum(impares)
print("\nCantidad de números impares entre 1 y 300:", cantidad_impares)
print("Sumatoria de los números impares:", sumatoria_impares)
