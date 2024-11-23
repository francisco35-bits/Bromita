from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reproducción de Audio</title>
    </head>
    <body>
        <h1>Bienvenido a la Página</h1>
        <audio id="audio" autoplay>
            <source src="/static/audio/sonido.mp3" type="audio/mpeg">
            Tu navegador no soporta la reproducción de audio.
        </audio>
        <script>
            const audio = document.getElementById('audio');
            audio.volume = 5.0; // Configura el volumen al 100%
        </script>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(debug=True)
