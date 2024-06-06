from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contacto")
def contact():
    return render_template('contacto.html')

@app.route("/cuiriosidades")
def curiosities():
    return render_template('curiosidades.html')

@app.route("/info")
def info():
    return render_template('informacion_flask.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
    