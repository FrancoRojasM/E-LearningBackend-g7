<!-- Documentando nuestra aplicaion -->
<!-- https://github.com/axnsan12/drf-yasg/ -->

<!-- desplegar -->
-Configuramos los static files para que nos pueda cargar swagger
-Crear nuestro archivo Procfile
-Crear una base de datos en Heroku con JawsDB
-Crear nuestras variables de entorno en heroku con las credenciales de JawsDB
-Inicializar git en nuestro proyecto con: git init
-Hacemos una conexion remota con: heroku git:remote -a
-Desplegamos el proyecto con: git add . && git commit -m "Inicializacion" && git push heroku
-Hacemos una migración de la base de datos con: heroku run python manage.py migrate