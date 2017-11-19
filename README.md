# Arquitectura-Micro-Servicios
Repositorio de la tarea 2

## Sistema de Procesamiento de Comentarios

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt  

Los paquetes que se instalarán son los siguientes:

Paquete | Versión | Descripción
--------|---------|------------
Flask   | 0.10.1  | Micro framework de desarrollo
requests| 2.12.4  | API interna utilizada en Flask para trabajar con las peticiones hacia el servidor
textblob| 0.12.0  | API que hace el analisis de comentarios
tweepy  | 3.5.0   | API que se conecta a twitter
pymysql | 0.7.11  |	API de base de datos
 
*__Nota__: También puedes instalar éstos prerrequisitos manualmente ejecutando los siguientes comandos*   
 sudo pip install Flask==0.10.1  

> sudo pip install requests==2.12.4

> sudo pip install textblob==0.12.0  

> sudo pip install tweepy==3.5.0

> sudo pip install pymysql==0.7.11

Una vez instalados los prerrequisitos es momento de ejcutar el sistema siguiendo los siguientes pasos:  
1. Ejecutar el servicio:  
   > python micro_servicios/sv_information.py

   > python micro_servicios/sv_SentimentAnalysis.py
   
   > python micro_servicios/sv_twitter.py

1. Ejecutar el GUI:  
   > python gui.py  
1. Abrir el navegador
1. Acceder a la url del sistema:
   > http://localhost:8000/ - página de inicio!
