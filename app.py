from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Definimos las 3 variables en el backend
    nombre_usuario = "Luis Gabriel"
    mensaje_bienvenida = "¡Bienvenido a tu primer panel dinámico en Flask!"
    fecha_actual = "Miércoles, 20 de Mayo de 2026"
    
    # Las enviamos a la plantilla HTML
    return render_template(
        'index.html', 
        usuario=nombre_usuario, 
        mensaje=mensaje_bienvenida, 
        fecha=fecha_actual
    )

if __name__ == '__main__':
    app.run(debug=True) # Activamos modo debug para ver cambios sin reiniciar
