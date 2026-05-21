
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Primera Aplicación Flask</title>
</head>
<body>
    <h1>¡Holiii desde Flask!</h1>
</body>
</html>

# Respuestas de Reflexión Técnica - Tarea 1
<h1>Luna Gabriela Castro Molina-1114</h1>
### 1. ¿Qué problema concreto resuelve el entorno virtual en un proyecto Python?
El entorno virtual resuelve el problema del conflicto de dependencias. Permite crear un espacio aislado para cada proyecto, garantizando que las librerías instaladas aquí no interfieran con otros proyectos de la computadora.

### 2. ¿Qué diferencia hay entre instalar Flask globalmente y hacerlo dentro de .venv?
* **Globalmente:** Flask se instala en el sistema operativo principal, quedando expuesto a que futuras actualizaciones de software rompan tus proyectos antiguos.
* **Dentro de `.venv`:** La instalación es local y exclusiva de este proyecto. Si borras la carpeta del entorno, tu sistema operativo queda completamente limpio.

### 3. ¿Por qué requirements.txt forma parte del proyecto y no de tu máquina personal?
Forma parte del proyecto para garantizar la portabilidad y reproducibilidad del software. Funciona como una receta que le indica a cualquier otro desarrollador o servidor en la nube las librerías exactas que debe instalar para que el sistema funcione igual que en tu máquina.

### 4. ¿Cuando ejecutas python app.py, qué archivo actúa como punto de entrada y por qué?
El archivo que actúa como punto de entrada es `app.py`. Actúa así porque es el script que inicializa el objeto principal de Flask (`app = Flask(__name__)`) y arranca el servidor web local al ser ejecutado directamente en la consola.

### 5. ¿Qué relación hay entre la ruta /, la función inicio() y el archivo templates/index.html?
Existe una relación de flujo secuencial: cuando el usuario ingresa a la dirección raíz (`/`), el servidor Flask intercepta la solicitud, ejecuta la función `inicio()` que tiene asociada y esta última renderiza y envía el archivo visual `templates/index.html` al navegador.

### 6. ¿Qué evidencia te da la terminal de que el servidor arrancó correctamente?
La terminal muestra líneas de texto plano con información del sistema, destacando visualmente el mensaje de estado: `* Running on http://127.0.0.1:5000`. Esto indica que el puerto local está abierto y escuchando peticiones.

### 7. Si cambias el HTML y el navegador muestra otra cosa, ¿qué te demuestra eso sobre el flujo entre backend y frontend en este proyecto?
Demuestra que el frontend no es independiente ni estático. Prueba que existe un flujo dinámico donde el navegador no abre el archivo directo del disco duro, sino que se lo solicita a Flask (backend), el cual lee el código HTML guardado en tiempo real y le sirve la versión actualizada en cada recarga.
