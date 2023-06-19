from tkinter import *

def play_game():
    # Implement play button functionality here
    print("Playing the game!")

def upload_mods():
    # Implement upload button functionality here
    print("Uploading mods...")

def login():
    # Implement login button functionality here
    print("Logging in...")

root = Tk()
root.title("Inferno Client")
root.geometry("800x600")

# Play Tab
play_tab = Frame(root)
play_tab.pack(fill=BOTH, expand=True)
play_icon = PhotoImage(file="play_icon.png")  # Replace with actual icon file
play_tab_button = Button(play_tab, image=play_icon)
play_tab_button.pack(side=TOP)
play_button = Button(play_tab, text="Play", font=("Arial", 24, "bold"), fg="red", command=play_game)
play_button.pack(fill=BOTH, expand=True)

# Mods Tab
mods_tab = Frame(root)
mods_tab.pack(fill=BOTH, expand=True)
mods_icon = PhotoImage(file="mods_icon.png")  # Replace with actual icon file
mods_tab_button = Button(mods_tab, image=mods_icon)
mods_tab_button.pack(side=TOP)
upload_button = Button(mods_tab, text="Upload Mods", command=upload_mods)
upload_button.pack(fill=BOTH, expand=True)

# Login Tab
login_tab = Frame(root)
login_tab.pack(fill=BOTH, expand=True)
login_button = Button(login_tab, text="Login", command=login)
login_button.pack(fill=BOTH, expand=True)

# Create tabs
tab_control = ttk.Notebook(root)
tab_control.add(play_tab, text="Play")
tab_control.add(mods_tab, text="Mods")
tab_control.add(login_tab, text="Login")
tab_control.pack(fill=BOTH, expand=True)

root.mainloop()
