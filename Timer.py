import time
import winsound
import tkinter as tk
import threading
from tkinter import font

timer_active = False
timer_lock = threading.Lock()


def start_timer():
    """Fonction appelé quand on clique sur START."""
    global timer_active
    try:
        intervalle = float(entry_intervalle.get())
        if intervalle <=0:
            label_status.config(text="❌ Die Zahl muss positiv sein!", fg="red")
            return

        with timer_lock:
            if timer_active:
                return
            timer_active = True


        label_status.config(text=f"Timer has Begun!",fg="green")
        btn_start.config(state=tk.DISABLED)
        btn_stop.config(state=tk.NORMAL)


        threading.Thread(
            target=run_timer,
            args=(intervalle,),
            daemon=True
        ).start()

    except ValueError:
        label_status.config(text="❌ Der Eingabewert muss eine Zahl sein (zB: 10)", fg="red")

def run_timer(intervalle):
    global timer_active

    while True:
        with timer_lock:
            if not timer_active:
                break
        window.after(0, lambda: label_status.config(text=" 🐣 Time to hatch!", fg="blue"))
        winsound.Beep(1000, 150)
        window.after(0, lambda: label_status.config(
            text=" ⚡ Running...",
            fg="green"
        ))
        time.sleep(intervalle - 0.15)


def stop_timer():
    global timer_active
    with timer_lock:
        timer_active = False

    """Fonction apellé quand on clique sur STOP."""
    label_status.config(text="⏹ Timer gestoppt!", fg="orange")
    btn_start.config(state=tk.NORMAL)
    btn_stop.config(state=tk.DISABLED)

def on_closing():
    """Appelée quand on ferme la fenêtre."""
    global timer_active
    with timer_lock:
        timer_active = False
    window.destroy()

#principal window
window = tk.Tk()
window.title("Timer SC2 (BY NIKKI) Viel Spaß Christoph")
window.geometry("700x250")
window.protocol("WM_DELETE_WINDOW", on_closing)

#Fonts
custom_font = font.Font(family="Helvetica", size=15, weight="bold")

#interval label
label_intervalle = tk.Label(window, text="Zeit (Sekunden) : ",font=custom_font)
label_intervalle.pack(pady=5) # pady = vertical padding (marge)

#Writing box für Zeit
entry_intervalle = tk.Entry(window, font=custom_font)
entry_intervalle.pack(pady=5)

# Start button
btn_start = tk.Button(
    window,
    text="Start!",
    command=start_timer,
    font=custom_font,
    bg="#4CAF50",
    fg="white")
btn_start.pack(side= tk.LEFT,padx=10)

# Bouton "Arrêter" (désactivé au début)
btn_stop = tk.Button(
    window,
    text="Stop!",
    command=stop_timer,
    font=custom_font,
    bg="#f44336",
    fg="white",
    state=tk.DISABLED)
btn_stop.pack(side=tk.LEFT,padx=10)

#Label status
label_status= tk.Label(
    window,
    text="🟢 Bereit zum Starten!",
    font=("Helvetica", 10, "bold"),
    fg="blue",
    pady=10
)
label_status.pack(pady=20)
if __name__ == '__main__':

    window.mainloop()


