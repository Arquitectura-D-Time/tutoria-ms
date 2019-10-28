# Microservicio de tutorias
Este microservicio se encarga de gestionar las tutorias es decir crearlas, eliminarlas, editarlas y consultarlas. (Exceptuando el horario de las mismas)

## Despliegue
La primera vez que se despliega se necesita correr las instrucciones:
-docker-compose run tutoria_ms python3 manage.py migrate
-docker-compose build
-docker-compose up

