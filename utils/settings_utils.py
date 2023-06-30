import json

def create_entry(settings_file, key, value):
    try:
        with open(settings_file, 'r', encoding='utf-8') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}
    
    settings[key] = value
    
    with open(settings_file, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=4)

def update_entry(settings_file, key, new_value):
    try:
        with open(settings_file, 'r', encoding='utf-8') as file:
            settings = json.load(file)
    except FileNotFoundError:
        print("The settings file was not found.")
        return
    
    if key in settings:
        settings[key] = new_value
    else:
        print(f"The key '{key}' was not found.")
        return
    
    with open(settings_file, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=4)

def read_entry(settings_file, key):
    try:
        with open(settings_file, 'r', encoding='utf-8') as file:
            settings = json.load(file)
    except FileNotFoundError:
        print("The settings file was not found.")
        return
    
    if key in settings:
        return settings[key]
    else:
        print(f"The key '{key}' was not found.")
        return None
