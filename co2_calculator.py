# co2_calculator.py

def calculate_emission_CO2(total_weight_kg, distance_km):
    emission_factor = 1.20
    total_weight_tonnes = total_weight_kg / 1000
    CO2_emission = emission_factor * total_weight_tonnes * distance_km
    return CO2_emission

def calculate_emission_CO2_gazole(litres_gazole):
    emission_factor = 2.67
    CO2_emission = emission_factor * litres_gazole
    return CO2_emission

def calculate_emission_CO2_batterie(consommation_batterie_kWh):
    emission_factor = 0.0005
    distance_km = consommation_batterie_kWh * 100
    CO2_emission = emission_factor * distance_km
    return CO2_emission
