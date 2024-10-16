import threading
import time
import pyautogui
import tkinter as tk
from tkinter import ttk
import keyboard

clicking = False
click_thread = None

def start_clicking():
    global clicking, click_thread

    if clicking:
        return

    clicking = True
    click_thread = threading.Thread(target=auto_click)
    click_thread.start()

def stop_clicking():
    global clicking
    clicking = False

def auto_click():
    button = button_var.get()
    interval = float(interval_var.get())
    click_type = click_type_var.get()

    while clicking:
        if click_type == "Single":
            pyautogui.click(button=button)
        elif click_type == "Double":
            pyautogui.doubleClick(button=button)
        time.sleep(interval)

def on_hotkey():
    if clicking:
        stop_clicking()
    else:
        start_clicking()

app = tk.Tk()
app.title("Auto Clicker By kosmo6666")
app.geometry("300x200")

interval_var = tk.StringVar(value="0.1")
button_var = tk.StringVar(value="left")
click_type_var = tk.StringVar(value="Single")

tk.Label(app, text="Click Interval (seconds):").pack(pady=5)
interval_entry = tk.Entry(app, textvariable=interval_var)
interval_entry.pack(pady=5)

tk.Label(app, text="Mouse Button:").pack(pady=5)
button_menu = ttk.Combobox(app, textvariable=button_var, values=["left", "right"])
button_menu.pack(pady=5)

tk.Label(app, text="Click Type:").pack(pady=5)
click_type_menu = ttk.Combobox(app, textvariable=click_type_var, values=["Single", "Double"])
click_type_menu.pack(pady=5)

start_button = tk.Button(app, text="Start", command=start_clicking)
start_button.pack(pady=5)

stop_button = tk.Button(app, text="Stop", command=stop_clicking)
stop_button.pack(pady=5)

keyboard.add_hotkey("ctrl+shift+S", on_hotkey)

app.protocol("WM_DELETE_WINDOW", stop_clicking)
app.mainloop()

keyboard.remove_hotkey("ctrl+shift+S")