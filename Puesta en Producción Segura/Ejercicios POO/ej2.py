class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han ingresado {cantidad:.2f}. Saldo actual: {self.cantidad:.2f}")
        else:
            print("No se puede ingresar una cantidad negativa.")

    def retirar(self, cantidad):
        self.cantidad -= cantidad
        print(f"Se han retirado {cantidad:.2f}. Saldo actual: {self.cantidad:.2f}")

# Ejemplo de uso:
cuenta = Cuenta("Juan Pérez")
cuenta.mostrar()
cuenta.ingresar(1000)
cuenta.retirar(500)
cuenta.mostrar()
