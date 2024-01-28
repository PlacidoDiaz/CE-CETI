# Inicio
# Inicialización de variables
A = B = C = 0

# Leer y almacenar los tres valores asegurando que sean distintos
while True:
    A = float(input("Introduce el valor de A: "))
    B = float(input("Introduce el valor de B: "))
    C = float(input("Introduce el valor de C: "))

    if A != B and A != C and B != C:
        break
    else:
        print("Los valores deben ser distintos. Por favor, inténtalos de nuevo.")

# Determinar y mostrar el mayor
if A > B and A > C:
    print(f"{A} es el mayor.")
elif B > A and B > C:
    print(f"{B} es el mayor.")
else:
    print(f"{C} es el mayor.")

# Determinar y mostrar el menor
if A < B and A < C:
    print(f"{A} es el menor.")
elif B < A and B < C:
    print(f"{B} es el menor.")
else:
    print(f"{C} es el menor.")



