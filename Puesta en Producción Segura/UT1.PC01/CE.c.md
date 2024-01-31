
# Comentarios de los Ejercicios

A continuación, se proporcionan comentarios detallados para los ejercicios de verificador de vocales, palíndromo, y clase Persona, explicando los elementos del código fuente utilizados y su función.

## Ejercicio de Verificador de Vocales

```python
def vocalChecker(char):
    # Utiliza la sentencia 'in' para verificar si el carácter dado está dentro de la cadena de vocales.
    # La cadena incluye vocales tanto en mayúsculas como en minúsculas para cubrir ambos casos.
    if char in 'aeiouAEIOU':
        return True  # Retorna True si el carácter es una vocal.
    else:
        return False  # Retorna False si el carácter no es una vocal.

if __name__ == '__main__':
    print(vocalChecker('h'))  # Imprime el resultado de la función vocalChecker cuando se le pasa 'h'.
```

- **`def`:** Define una función. `vocalChecker` es el nombre de la función.
- **`char`:** Parámetro de la función, representa el carácter a verificar.
- **`if`:** Sentencia condicional que evalúa si el carácter está entre las vocales.
- **`return`:** Retorna `True` o `False` dependiendo de la condición evaluada.
- **`__name__ == '__main__'`:** Asegura que el bloque de código se ejecute solo cuando el archivo es ejecutado directamente.

## Ejercicio Palíndromo

```python
def es_palindromo(string):
    # Compara el string original con su versión invertida.
    if string == string[::-1]:
        return True  # Retorna True si el string es palíndromo.

if __name__ == '__main__':
    es_palindromo("radar")  # Llama a la función con "radar" como argumento.
```

- **`string[::-1]`:** Invierte el string. Es una forma concisa en Python de obtener un string al revés.
- **`if`:** Verifica si el string original es igual a su versión invertida.

## Ejercicio Clase Persona

```python
class Persona:
    def __init__(self, nombre="", edad=0, dni="", telefono="", email=""):
        # Constructor de la clase con parámetros predeterminados.
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email
        # Inicializa los atributos de la instancia.

    # Métodos setters y getters para cada atributo permiten modificar y acceder a los valores de los atributos de manera controlada.
    # Métodos mostrar() y esMayorDeEdad() proporcionan funcionalidades específicas para la clase.

if __name__ == '__main__':
    persona1 = Persona("Naim", 21, "12345678A", "123456789", "Naim@gmail.com")
    persona1.mostrar()
    print(persona1.esMayorDeEdad())
```

- **`class`:** Define una clase. `Persona` es el nombre de la clase.
- **`__init__`:** Constructor de la clase, inicializa los atributos de la instancia.
- **Métodos:** Funciones definidas dentro de la clase que operan con los atributos de la instancia.
