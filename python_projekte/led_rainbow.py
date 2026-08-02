import tkinter as tk
import colorsys

NUM_LEDS = 12

class LedRainbow:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Rainbow")
        self.root.configure(bg="#1e1e1e")
        self.running = False
        self.offset = 0.0

        tk.Label(root, text="LED Rainbow", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white").pack(pady=10)

        self.canvas = tk.Canvas(root, width=NUM_LEDS * 50 + 20, height=100,
                                 bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(padx=20, pady=10)

        self.ovals = []
        for i in range(NUM_LEDS):
            x = 10 + i * 50
            oval = self.canvas.create_oval(x, 20, x + 40, 60, fill="#333", outline="#555")
            self.ovals.append(oval)

        speed_frame = tk.Frame(root, bg="#1e1e1e")
        speed_frame.pack(pady=5)
        tk.Label(speed_frame, text="Geschwindigkeit:", bg="#1e1e1e", fg="white").pack(side="left")
        self.speed = tk.Scale(speed_frame, from_=1, to=20, orient="horizontal",
                               bg="#1e1e1e", fg="white", troughcolor="#444", highlightthickness=0)
        self.speed.set(5)
        self.speed.pack(side="left")

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)
        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start,
                                    bg="#4CAF50", fg="white", width=10)
        self.start_btn.grid(row=0, column=0, padx=5)
        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop,
                                   bg="#f44336", fg="white", width=10)
        self.stop_btn.grid(row=0, column=1, padx=5)

    def hsv_to_hex(self, h):
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))

    def start(self):
        if not self.running:
            self.running = True
            self.animate()

    def stop(self):
        self.running = False

    def animate(self):
        if not self.running:
            return
        for i, oval in enumerate(self.ovals):
            hue = (self.offset + i / NUM_LEDS) % 1.0
            self.canvas.itemconfig(oval, fill=self.hsv_to_hex(hue))
        self.offset += 0.01 * self.speed.get()
        self.root.after(40, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = LedRainbow(root)
    root.mainloop()
