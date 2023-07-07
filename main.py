import customtkinter
from CTkMessagebox import CTkMessagebox
import antiAfk
import threading
from utils import settings_utils
import os
from PIL import Image

settings_file = 'settings.json'

def start_antiAFK():
    if not antiAfk.is_active:
        antiAfk.is_active = True
        movement_thread = threading.Thread(target=antiAfk.check_movement)
        movement_thread.start()
        antiAfkButton.configure(text="Deactivate Anti AFK", fg_color="#c0392b", hover_color="#e74c3c")
    else:
        antiAfk.is_active = False
        antiAfkButton.configure(text="Activate Anti AFK", fg_color="#16a085", hover_color="#1abc9c")

def save_antiAFK():
    settings_utils.update_entry(settings_file, "text", antiAfkTextbox.get('1.0', '6.0').replace('\n', ' '))
    CTkMessagebox(title="Info", message="Text Saved")



app = customtkinter.CTk()
app.resizable(False, False)
app.title("ETS2Utils")
app.geometry("550x550")

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=10, pady=10, fill='both', expand=True)

tabview.add("AntiAfk")
tabview.add("Settings")
tabview.set("AntiAfk") 


#AntiAfk TAB
AntiAfkTab = tabview.tab("AntiAfk")

antiAfkTextbox = customtkinter.CTkTextbox(master=AntiAfkTab, width=400, height=100)
antiAfkTextbox.grid(row=0, column=0, padx=10, pady=(20, 10))
antiAfkTextbox.insert("0.0", settings_utils.read_entry(settings_file, "text"))

save_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "save_icon.png")))
antiAfkSaveButton = customtkinter.CTkButton(master=AntiAfkTab, text="", image=save_icon, fg_color="#16a085", hover_color="#1abc9c" ,command=save_antiAFK, width=50, height=50)
antiAfkSaveButton.grid(row=0, column=1, padx=(10, 0), pady=(20, 10))

antiAfkButton = customtkinter.CTkButton(master=AntiAfkTab, text="Activate Anti AFK", fg_color="#16a085", hover_color="#1abc9c", text_color="black" ,command=start_antiAFK)
antiAfkButton.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))

#Settings TAB
SettingsTab = tabview.tab("Settings")

telemetryUrlTextbox = customtkinter.CTkTextbox(master=SettingsTab, width=400, height=10)
telemetryUrlTextbox.grid(row=0, column=0, padx=10, pady=(20, 10))
telemetryUrlTextbox.insert("0.0", settings_utils.read_entry(settings_file, "telemetryIP"))
app.mainloop()