from flask import Flask, request, render_template
from ddg import buscar

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def mostrar_resultado():
    dado = request.form['id_dado']
    return render_template("resultado.html", resultados = realizar_busca(dado), valor_pesquisado = dado, qtde_resultados = len(realizar_busca(dado)))
    

def realizar_busca(dado):
    resultado = buscar(dado)
    return resultado

if __name__ == "__main__":
    app.run(port = 8000, debug = True)
