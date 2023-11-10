# Parte 1: Recolección y almacenamiento de evidencias

## Indice

## Introducción
En este proyecto...

## La Recolección

Hemos realizado la recolección del equipo informático, siguiendo nuestra metodología. 

Para ello alejamos a las personas no autorizadas de la escena. 

Hemos fotografiado la escena.

Anotaremos la hora de obtención de la máquina.

Estamos trabajando sobre una máquina virtual en live. 

Mantendremos el equipo encendido y no lo apagaremos.

## La Evidencia

## Descripción de la evidencia

En la máquina aparece un mensaje de Error de "Windows Script Host". Este error muestra un archivo que ya existe en la linea 19 de 2 carácteres en "C:\Windows\Temp\HoVgcPUXNBk.vbs"

![image](https://github.com/PlacidoDiaz/AFI/assets/86500067/89e7d6cb-0bce-4346-8bea-eece1b3ffe2f)

La máquina nos pregunta si deseamos reinicar para aplicar los cambios. Pulsaremos en "Restart Later".

![image](https://github.com/PlacidoDiaz/AFI/assets/86500067/4de40f6a-c442-416d-befa-2bc342e466cf)


## Tipo de evidencia
Una vez localizada la evidencia analizamos el impacto que esta puede llevar. 

## Orden de volatilidad
Ahora nos dispondremos a seguir el orden de volatilidad establecido en nuestra metodología. 
Para ello conectaremos nuestro pendrive al dispostivo para usar las herramientas necesarias.

![image](https://github.com/PlacidoDiaz/AFI/assets/86500067/4495f673-3e5b-487a-bf07-af29be1d1182)

**Paso 1:** Capturaremos la memoria volátil, utilizaremos **RamCapture64**.

  ![image](https://github.com/PlacidoDiaz/AFI/assets/86500067/65e918e5-04e5-47fe-81be-1e571123bd45)

**Paso 2:** Realizaremos un triaje con la aplicación **WinAudit**. 

  Seleccionamos los siguentes parámetros:

  ![image](https://github.com/PlacidoDiaz/AFI/assets/86500067/e2c84d18-58cf-475d-a95b-8423d424da03)

  Esperamos que se realice la imagen y pulsamos sobre "Save" para guardarelo en nuestra unidad extraible.

  ![image](https://github.com/PlacidoDiaz/AFI/assets/86500067/39381b20-56fc-4cea-a190-72559a01a6e1)

**Paso 3:** Realizaremos una copia completa del disco en una unidad limpia, utilizaremos **FTK Imager**.





## Cadena de custodia

## Almacenamiento

Almacenar las evidencias en dispositivos cuya seguridad haya sido demostrada y que permita detectar intentos de acceso no autorizados.

## Metodología seguida

Hemos utilizado APINAG4 esta norma tiene como objetivo proporcionar un marco sólido para realizar investigaciones forenses informáticas.
