import customtkinter
import antiAfk
import threading
from utils import settings_utils

settings_file = 'settings.json'

def start_antiAFK():
    if not antiAfk.is_active:
        antiAfk.is_active = True
        movement_thread = threading.Thread(target=antiAfk.check_movement)
        movement_thread.start()
        antiAfkButton.configure(text="Deactivate Anti AFK")
    else:
        antiAfk.is_active = False
        antiAfkButton.configure(text="Activate Anti AFK")

def save_antiAFK():
    settings_utils.update_entry(settings_file, "text", textboxText.get('1.0', '6.0').replace('\n', ' '))
app = customtkinter.CTk()
app.title("ETS2Util")
app.geometry("700x550")


tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=10, pady=10, fill='both', expand=True)

tabview.add("AntiAfk")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("AntiAfk")  # set currently visible tab

tab_frame = tabview.tab("AntiAfk")

antiAfkButton = customtkinter.CTkButton(master=tab_frame, text="Activate Anti AFK", command=start_antiAFK)
antiAfkButton.pack(padx=20, pady=20)

textboxText = customtkinter.CTkTextbox(master=tab_frame, width=400, height=100)
textboxText.pack(padx=10, pady=10)

antiAfkSavekButton = customtkinter.CTkButton(master=tab_frame, text="Save", command=save_antiAFK)
antiAfkSavekButton.pack(padx=20, pady=20)
app.mainloop()