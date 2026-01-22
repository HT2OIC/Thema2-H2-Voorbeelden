# Functie om sensor uit te lezen en json op te stellen.
def generate_json():
    sensorwaarde = sensor.value()
    return json.dumps({"Sensorpin": sensor, "Sensorwaarde": sensorwaarde})