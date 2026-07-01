from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola Flask"

@app.route("/error")
def error():
    return "Error solucionado"

if __name__ == "__main__":
    app.run(debug=True)