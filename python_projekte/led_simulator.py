import tkinter as tk

ROWS, COLS = 4, 4
ON_COLOR = "#ff3b30"
OFF_COLOR = "#3a3a3a"

class LedSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Simulator")
        self.root.configure(bg="#1e1e1e")
        self.leds = {}

        title = tk.Label(root, text="LED Simulator", font=("Arial", 18, "bold"),
                          bg="#1e1e1e", fg="white")
        title.pack(pady=10)

        grid_frame = tk.Frame(root, bg="#1e1e1e")
        grid_frame.pack(padx=20, pady=10)

        for r in range(ROWS):
            for c in range(COLS):
                canvas = tk.Canvas(grid_frame, width=60, height=60,
                                    bg="#1e1e1e", highlightthickness=0)
                oval = canvas.create_oval(5, 5, 55, 55, fill=OFF_COLOR, outline="#555")
                canvas.grid(row=r, column=c, padx=8, pady=8)
                canvas.bind("<Button-1>", lambda e, rc=(r, c): self.toggle(rc))
                self.leds[(r, c)] = {"canvas": canvas, "oval": oval, "state": False}

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Alle An", command=self.all_on,
                  bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Alle Aus", command=self.all_off,
                  bg="#555", fg="white", width=10).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Zufall", command=self.randomize,
                  bg="#2196F3", fg="white", width=10).grid(row=0, column=2, padx=5)

    def toggle(self, rc):
        led = self.leds[rc]
        led["state"] = not led["state"]
        color = ON_COLOR if led["state"] else OFF_COLOR
        led["canvas"].itemconfig(led["oval"], fill=color)

    def all_on(self):
        for led in self.leds.values():
            led["state"] = True
            led["canvas"].itemconfig(led["oval"], fill=ON_COLOR)

    def all_off(self):
        for led in self.leds.values():
            led["state"] = False
            led["canvas"].itemconfig(led["oval"], fill=OFF_COLOR)

    def randomize(self):
        import random
        for led in self.leds.values():
            led["state"] = random.choice([True, False])
            color = ON_COLOR if led["state"] else OFF_COLOR
            led["canvas"].itemconfig(led["oval"], fill=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = LedSimulator(root)
    root.mainloop()
