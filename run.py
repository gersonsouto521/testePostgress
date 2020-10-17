from flask import Flask, jsonify, render_template, request
import os
from service import inserir_plan, mostrar_plan
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

#@app.route("/inserir/<name>/<age>", methods=['POST'])
@app.route("/inserir" , methods=['POST'])
def inserir():
    planilhaWishLocal = request.form['romaneio']
    inserir_plan(planilhaWishLocal)
    return "Home PAGE"

@app.route("/mostrar")
def mostrar():
    a = mostrar_plan()
    return jsonify(a)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    #app.run()