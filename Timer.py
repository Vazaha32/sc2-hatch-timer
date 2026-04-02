import sys
import os
import time
import tkinter as tk
import threading
from tkinter import font
import ctypes

# Variables globales
running = False
intervalle = 0.0

# Chemin des ressources (pour PyInstaller)
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# --- SON (non-bloquant) ---
def play_sound():
    """Joue un son très court (100ms) sans bloquer le timer."""
    def _play():
        try:
            winmm = ctypes.windll.winmm
            winmm.PlaySound(resource_path("poc.wav").encode('utf-8'), None, 0x00020000 | 0x0001)
            time.sleep(0.1)  # 100ms
            winmm.PlaySound(None, None, 0)  # Arrête le son
        except:
            pass  # Ignore les erreurs (pour éviter les crashes)
    threading.Thread(target=_play, daemon=True).start()

# --- TIMER (précis) ---
def run_timer():
    global running
    next_bip = time.time() + intervalle  # Prochain bip à intervalle fixe

    while running:
        current_time = time.time()

        # Si c'est l'heure du bip
        if current_time >= next_bip:
            window.after(0, lambda: label_status.config(text="🐣 Time to hatch!", fg="blue"))
            play_sound()  # Bip sans bloquer
            next_bip = current_time + intervalle  # Prochain bip
            window.after(0, lambda: label_status.config(text="⚡ Running...", fg="green"))

        # Petite pause pour éviter la surcharge CPU
        time.sleep(0.01)

# --- Boutons ---
def start_timer():
    global running, intervalle
    try:
        intervalle = float(entry_intervalle.get())
        if intervalle <= 0:
            label_status.config(text="❌ Die Zahl muss positiv sein!", fg="red")
            return

        running = True
        btn_start.config(state=tk.DISABLED)
        btn_stop.config(state=tk.NORMAL)
        label_status.config(text="⚡ Running...", fg="green")
        threading.Thread(target=run_timer, daemon=True).start()
    except ValueError:
        label_status.config(text="❌ Der Eingabewert muss eine Zahl sein!", fg="red")

def stop_timer():
    global running
    running = False
    btn_start.config(state=tk.NORMAL)
    btn_stop.config(state=tk.DISABLED)
    label_status.config(text="⏹ Timer gestoppt!", fg="orange")

# --- Interface ---
window = tk.Tk()
window.title("Timer SC2 FOR UKGER (BY NIKKI)")
window.geometry("700x250")

# Fonts
custom_font = font.Font(family="Helvetica", size=15, weight="bold")

# Champ d'entrée
label_intervalle = tk.Label(window, text="Zeit (Sekunden):", font=custom_font)
label_intervalle.pack(pady=5)
entry_intervalle = tk.Entry(window, font=custom_font)
entry_intervalle.pack(pady=5)

# Boutons
btn_start = tk.Button(window, text="Start!", command=start_timer, font=custom_font, bg="#4CAF50", fg="white")
btn_start.pack(side=tk.LEFT, padx=10)
btn_stop = tk.Button(window, text="Stop!", command=stop_timer, font=custom_font, bg="#f44336", fg="white", state=tk.DISABLED)
btn_stop.pack(side=tk.LEFT, padx=10)

# Statut
label_status = tk.Label(window, text="🟢 Bereit zum Starten!", font=("Helvetica", 10, "bold"), fg="blue", pady=10)
label_status.pack(pady=20)

window.mainloop()
