from flask import Flask, render_template

app = Flask(__name__)

# Lista de imágenes locales (dentro de static/imagenes)
fotos = [
    "imagenes/foto1.jpg",
    "imagenes/foto2.jpg"
]

@app.route('/')
def index():
    return render_template("index.html", fotos=fotos)

if __name__ == '__main__':
    # Esto permite acceder desde el celular (misma red Wi-Fi)
    app.run(host='0.0.0.0', port=5000, debug=True)