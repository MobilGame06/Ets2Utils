import requests
from utils import settings_utils
settings_file = 'settings.json'

def check_movement(threshold):
    url = settings_utils.read_entry(settings_file, "telemetryIP") + "/api/ets2/telemetry"
    try:
        response = requests.get(url)
        
        telemetry_data = response.json()

        speed = telemetry_data["truck"]["speed"]
        is_moving = speed > threshold

        return is_moving

    except requests.exceptions.ConnectionError:
        print("Connection to ETS2 Telemetry Server failed.")
        return False
