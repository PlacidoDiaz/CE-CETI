# Instalación

Instalamos el servicio apache.

![alt text](image.png)

Añadimos un index para comprobar que todo funciona correctamente.

![alt text](image-1.png)

Entramos en [Duck DNS](https://www.duckdns.org/domains), nos registramos y vinculamos nuestro dominio gratuito con nuesta ip.

![image](https://github.com/PlacidoDiaz/Notas-PT/assets/86500067/b23837e5-5606-4a60-9f06-5f17c5ade034)

Probamos que todo funciona, colocando el dominio en el navegador.

![image](https://github.com/PlacidoDiaz/Notas-PT/assets/86500067/fee040a6-7bd0-4ec1-98cd-e07e60c5ca70)

# Instalación del certificado

    sudo snap install --classic certbot
    
    sudo ln -s /snap/bin/certbot /usr/bin/certbot
    
    sudo certbot --apache

![image](https://github.com/PlacidoDiaz/Notas-PT/assets/86500067/08c53b11-bfe1-4640-a921-1a38ed299bf8)

Una vez instalado nuestro certificado gratuito, nos pararecera un certificaado en nuestro dominio ``proyecto9.duckdns.org``

![image](https://github.com/PlacidoDiaz/Notas-PT/assets/86500067/cc739c4d-df82-4c8a-8b6c-74819ebd2967)


