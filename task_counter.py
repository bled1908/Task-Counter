import tkinter as tk
from tkinter import messagebox
import winsound
import os
import random

SAVE_FILE = "counter_state.txt"

MOTIVATION_MESSAGES = [
    "You're doing great ✨",
    "Proud of you 💖",
    "Keep going 🌙",
    "Small steps matter 🌱",
    "You’re closer than before 🌼",
    "You are amazing 💫"
]

FLOWER_STAGES = [
    "🌱",  # 100%
    "🌿",  # 75%
    "🌷",  # 50%
    "🌼",  # 25%
    "✨"   # 0% (done)
]

def play_chime():
    winsound.Beep(880, 300)

def load_counter():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def save_counter():
    with open(SAVE_FILE, "w") as f:
        f.write(str(counter))

def update_flower():
    if starting_value == 0:
        flower_label.config(text="🌱")
        return
    
    progress = counter / starting_value

    if progress == 0:
        flower_label.config(text="✨")
    elif progress > 0.75:
        flower_label.config(text="🌱")
    elif progress > 0.50:
        flower_label.config(text="🌿")
    elif progress > 0.25:
        flower_label.config(text="🌷")
    else:
        flower_label.config(text="🌼")

def decrease_counter():
    global counter
    if counter > 0:
        counter -= 1
        save_counter()
        label.config(text=f"💛 {counter} tasks left")
        update_flower()

        # Motivational message popup (non-blocking)
        status_label.config(text=random.choice(MOTIVATION_MESSAGES))

        if counter == 0:
            play_chime()
            label.config(text="✨ All tasks completed! ✨")
            flower_label.config(text="✨")
            messagebox.showinfo("Yay!", "🎉 You finished everything! Beautiful work!")
    else:
        messagebox.showinfo("Done!", "You already reached zero 🤍")

def set_counter():
    global counter, starting_value
    try:
        counter = int(entry.get())
        starting_value = counter
        save_counter()
        label.config(text=f"💛 {counter} tasks left")
        update_flower()
        status_label.config(text="")
    except ValueError:
        messagebox.showerror("Oops!", "Please enter a valid number!")

# UI Setup
window = tk.Tk()
window.title("Cute Task Counter")
window.geometry("320x330")
window.config(bg="#FFF8F3")

counter = load_counter()
starting_value = counter if counter > 0 else 1

title_label = tk.Label(window, text="🌼 Task Counter 🌼", font=("Helvetica", 18, "bold"), bg="#FFF8F3", fg="#7A4B7C")
title_label.pack(pady=10)

entry = tk.Entry(window, font=("Helvetica", 16), justify="center")
entry.pack(pady=5)

set_button = tk.Button(window, text="Set Starting Count 💫", font=("Helvetica", 12), bg="#F7D6E0", activebackground="#F3C4D4", command=set_counter)
set_button.pack(pady=10)

label = tk.Label(window, text=f"💛 {counter} tasks left", font=("Helvetica", 16), bg="#FFF8F3", fg="#444")
label.pack(pady=5)

flower_label = tk.Label(window, text="🌱", font=("Helvetica", 40), bg="#FFF8F3")
flower_label.pack(pady=5)
update_flower()

decrease_button = tk.Button(window, text="I finished one! ✅", font=("Helvetica", 14), bg="#C8EAD3", activebackground="#B4DCC4", command=decrease_counter)
decrease_button.pack(pady=10)

status_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#FFF8F3", fg="#6D5A72")
status_label.pack(pady=5)

window.mainloop()
