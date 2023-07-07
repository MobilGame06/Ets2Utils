import time
import pygetwindow as gw
import keyboard
from utils import settings_utils
from utils import telemetry

settings_file = 'settings.json'
is_active = False 


def writeText():
    time.sleep(2)
    keyboard.press('y')
    keyboard.release('y')

    time.sleep(0.5)
    active_window = gw.getActiveWindow()
    if active_window.title == "Euro Truck Simulator 2 Multiplayer" or active_window.title == "American Truck Simulator Multiplayer":
        text = settings_utils.read_entry(settings_file, "text")
        print(text)
        keyboard.write(text)
        keyboard.press('enter')
        keyboard.press('enter')
    else:
        print("ETS or ATS is not active or in focus.")


timer_start = 0

def check_movement():
    global is_moving, timer_start
    timer_start = time.time()
    while is_active:
        time.sleep(5)

        # Bewegungsstatus abfragen
        is_moving = telemetry.check_movement(0.1)

        # Ausgabe des Bewegungsstatus
        if is_moving:
            print("The vehicle is moving..")
            timer_start = time.time() 
        else:
            print("The vehicle is stationary or not in play.")
            if timer_start != 0 and time.time() - timer_start >= 20:
                print("Text is being written...")
                writeText()
                timer_start = time.time() 