class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0, edad_titular=18):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad_titular = edad_titular

    def esTitularValido(self):
        return 18 <= self.edad_titular < 25

    def mostrar(self):
        super().mostrar()
        print(f"Tipo de cuenta: Cuenta Joven")
        print(f"Bonificación: {self.bonificacion}%")
        print(f"Titular válido: {'Sí' if self.esTitularValido() else 'No'}")

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero. El titular no es válido para Cuenta Joven.")

# Ejemplo de uso:
cuenta_joven = CuentaJoven("Ana López", 1000, 10, 22)
cuenta_joven.mostrar()
cuenta_joven.ingresar(500)
cuenta_joven.retirar(200)
cuenta_joven.mostrar()

cuenta_joven_edad_no_valida = CuentaJoven("Pedro Martínez", 1000, 10, 26)
cuenta_joven_edad_no_valida.mostrar()
cuenta_joven_edad_no_valida.retirar(200)
