import requests

def check_movement(threshold):
    # URL des ETS2 Telemetry Servers
    url = "http://localhost:25555/api/ets2/telemetry"

    try:
        # API-Anfrage senden und die Antwort erhalten
        response = requests.get(url)
        
        # JSON-Daten aus der API-Antwort extrahieren
        telemetry_data = response.json()

        # Überprüfen, ob das Fahrzeug in Bewegung ist
        speed = telemetry_data["truck"]["speed"]
        is_moving = speed > threshold

        return is_moving

    except requests.exceptions.ConnectionError:
        print("Verbindung zum ETS2 Telemetry Server fehlgeschlagen.")
        return False
