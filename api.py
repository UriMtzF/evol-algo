from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from pyhton.evolucion_diferencial import EvolucionDiferencial

app = Flask(__name__)
CORS(app)

evol_algo = EvolucionDiferencial(
    pop_size=4, bounds=[-10, 10], dim=3, Cr=0.5
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get-population', methods=['GET'])
def generate():
    evol_algo.regenerate_population()
    data = {
        "code": 200,
        "data": {"population": evol_algo.population.tolist()}
    }
    return jsonify(data)


@app.route('/api/get-result/<int:generation>', methods=['GET'])
def get_result(generation):
    maximize = [arr.tolist() for arr in evol_algo.maximization(generation)]
    minimize = [arr.tolist() for arr in evol_algo.minimization(generation)]
    data = {
        "code": 200,
        "data": {
            "maximize": maximize,
            "minimize": minimize,
        }
    }
    return jsonify(data)


app.run('0.0.0.0', port=8000, debug=True)
