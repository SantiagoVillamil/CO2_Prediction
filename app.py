from flask import Flask, render_template, request, jsonify
from co2_calculator import calculate_emission_CO2, calculate_emission_CO2_gazole, calculate_emission_CO2_batterie

app = Flask(__name__)


@app.route('/co2_emission_distance', methods=['POST'])
def co2_emission_distance():
    poids_total_kg = float(request.form.get('poids_total_kg'))
    distance_km = float(request.form.get('distance_km'))
    result = calculate_emission_CO2(poids_total_kg, distance_km)
    return jsonify({'result': result})

@app.route('/co2_emission_gazole', methods=['POST'])
def co2_emission_gazole():
    litres_gazole = float(request.form.get('litres_gazole'))
    result = calculate_emission_CO2_gazole(litres_gazole)
    return jsonify({'result': result})

@app.route('/co2_emission_batterie', methods=['POST'])
def co2_emission_batterie():
    consommation_batterie_kWh = float(request.form.get('consommation_batterie_kWh'))
    result = calculate_emission_CO2_batterie(consommation_batterie_kWh)
    return jsonify({'result': result})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5002)
