import tkinter as tk
import sys
import threading

SOUNDS = {
    "Beep": 800,
    "Boop": 300,
    "Alarm": 1200,
    "Blip": 1500,
    "Tief": 150,
    "Hoch": 2000,
    "Ping": 1000,
    "Buzz": 400,
    "Alert": 1800,
}

def play_tone(freq):
    if sys.platform == "win32":
        import winsound
        winsound.Beep(freq, 300)
    else:
        # Fallback fuer Linux/Mac: Terminal-Klingelton (Frequenz wird ignoriert)
        print("\a", end="", flush=True)


class Soundboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Soundboard")
        self.root.configure(bg="#1e1e1e")

        tk.Label(root, text="Soundboard", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white").pack(pady=15)

        grid = tk.Frame(root, bg="#1e1e1e")
        grid.pack(padx=20, pady=10)

        colors = ["#e53935", "#8e24aa", "#3949ab", "#00897b", "#43a047",
                  "#fdd835", "#fb8c00", "#6d4c41", "#546e7a"]

        for i, (name, freq) in enumerate(SOUNDS.items()):
            btn = tk.Button(grid, text=name, font=("Arial", 12, "bold"), width=10, height=3,
                             bg=colors[i % len(colors)], fg="white",
                             command=lambda f=freq: self.play(f))
            btn.grid(row=i // 3, column=i % 3, padx=6, pady=6)

        self.status = tk.Label(root, text="Bereit.", bg="#1e1e1e", fg="#aaa")
        self.status.pack(pady=10)

    def play(self, freq):
        self.status.config(text=f"Spiele Ton ({freq} Hz) ...")
        threading.Thread(target=play_tone, args=(freq,), daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = Soundboard(root)
    root.mainloop()
