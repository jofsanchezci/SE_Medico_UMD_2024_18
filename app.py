from flask import Flask, render_template, request

app = Flask(__name__)

# Base de conocimientos
base_conocimiento = [
    {"condiciones": ["fiebre alta", "dolor de cabeza"], "diagnostico": "infección viral"},
    {"condiciones": ["fiebre alta", "tos persistente"], "diagnostico": "neumonía"},
    {"condiciones": ["dolor abdominal", "náuseas"], "diagnostico": "gastroenteritis"},
    {"condiciones": ["fiebre alta", "erupción cutánea"], "diagnostico": "sarampión"},
]

# Motor de inferencia
def diagnosticar(sintomas):
    for regla in base_conocimiento:
        if all(condicion in sintomas for condicion in regla["condiciones"]):
            return regla["diagnostico"]
    return "No se pudo determinar el diagnóstico."

@app.route("/", methods=["GET", "POST"])
def index():
    diagnostico = None
    if request.method == "POST":
        sintomas = request.form.getlist("sintomas")
        diagnostico = diagnosticar(sintomas)
    return render_template("index.html", diagnostico=diagnostico, base_conocimiento=base_conocimiento)

if __name__ == "__main__":
    app.run(debug=True)
