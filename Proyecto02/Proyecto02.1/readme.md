# Parte 1: Recolección y Almacenamiento de Evidencias

## Índice

1. [**Introducción**](#introducción)
2. [**La Recolección**](#la-recolección)
3. [**La Evidencia**](#la-evidencia)
4. [**Tipo de Evidencia**](#tipo-de-evidencia)
5. [**Orden de Volatilidad**](#orden-de-volatilidad)
6. [**Cadena de Custodia**](#cadena-de-custodia)
7. [**Almacenamiento**](#almacenamiento)
8. [**Metodología Seguida**](#metodología-seguida)

## Introducción
En este proyecto, abordaremos la recolección y almacenamiento de evidencias en un entorno informático, siguiendo una metodología específica.

## La Recolección
Hemos llevado a cabo la recolección del equipo informático, implementando nuestra norma **APINAG4**. 

### Aislamiento
Hemos realizado un aislamiento de personas no autorizadas en la escena.

### Fotografía de la Escena
Se ha documentado visualmente la escena mediante fotografías (en este caso no podemos colocar imagenes de la escena).

### Registro de la Hora
Hemos obtenido la máquina el lunes, 6 de noviembre de 2023, 08:00.

### Entorno de Trabajo
Estamos operando en una máquina virtual en vivo, manteniendo el equipo encendido sin apagarlo.

## La Evidencia
### Descripción de la Evidencia
En la máquina, se ha identificado un mensaje de error de "Windows Script Host" asociado a un archivo existente en la ruta "C:\Windows\Temp\HoVgcPUXNBk.vbs."

### Imágenes Relevantes
![Error de Windows Script Host](https://github.com/PlacidoDiaz/AFI/assets/86500067/89e7d6cb-0bce-4346-8bea-eece1b3ffe2f)

La máquina presenta un mensaje de reinicio, al cual hemos optado por seleccionar "Restart Later."

![Mensaje de Reinicio](https://github.com/PlacidoDiaz/AFI/assets/86500067/4de40f6a-c442-416d-befa-2bc342e466cf)

## Tipo de Evidencia
Tras localizar la evidencia, se realizará un análisis del impacto que esta podría tener.

## Orden de Volatilidad

Siguiendo nuestra metodología, se seguirá el orden de volatilidad establecido. Se conectará un pendrive al dispositivo para utilizar las herramientas necesarias.

### Conexión del Pendrive

![Conexión del Pendrive](https://github.com/PlacidoDiaz/AFI/assets/86500067/4495f673-3e5b-487a-bf07-af29be1d1182)

### Paso 1: Captura de Memoria Volátil

Utilizaremos **RamCapture64** para capturar la memoria volátil.

![Captura de Memoria Volátil](https://github.com/PlacidoDiaz/AFI/assets/86500067/65e918e5-04e5-47fe-81be-1e571123bd45)

### Paso 2: Triaje con WinAudit

Se realizará un triaje utilizando la aplicación **WinAudit** con parámetros específicos. La imagen se guardará en una unidad extraíble.

![Triaje con WinAudit](https://github.com/PlacidoDiaz/AFI/assets/86500067/e2c84d18-58cf-475d-a95b-8423d424da03)

![Guardar Triaje](https://github.com/PlacidoDiaz/AFI/assets/86500067/39381b20-56fc-4cea-a190-72559a01a6e1)

### Paso 3: Copia Completa del Disco con FTK Imager

Reaplizamos un clonado completo del disco.

![FTK Imager](https://github.com/PlacidoDiaz/AFI/assets/86500067/7b5b9592-ed27-4dbc-8852-b3e9fb1292c5)

Guardamos la copia en un disco duro limpio.

![Guardar Imagen](https://github.com/PlacidoDiaz/AFI/assets/86500067/d88cfc2f-3774-4519-af67-b31d5b87036f)


## Cadena de Custodia

## Almacenamiento
Las evidencias se almacenarán en dispositivos seguros con demostrada seguridad, capaces de detectar intentos de acceso no autorizados.

## Metodología Seguida
Hemos seguido la norma APINAG4, que proporciona un marco sólido para investigaciones forenses informáticas. La metodología aborda diferentes aspectos, incluyendo el proceso de recolección en equipos informáticos, dispositivos móviles, orden de volatilidad, procedimientos de análisis, almacenamiento, herramientas y consideraciones legales.
