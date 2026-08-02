import tkinter as tk
import random

PIPS = {
    1: [(1, 1)],
    2: [(0, 0), (2, 2)],
    3: [(0, 0), (1, 1), (2, 2)],
    4: [(0, 0), (0, 2), (2, 0), (2, 2)],
    5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
}

class Wuerfel:
    def __init__(self, root):
        self.root = root
        self.root.title("Würfel")
        self.root.geometry("400x480")
        self.num_dice = 2

        tk.Label(root, text="Würfel-Simulator", font=("Arial", 18, "bold")).pack(pady=10)

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(pady=10)
        self.canvases = []

        control_frame = tk.Frame(root)
        control_frame.pack(pady=5)
        tk.Label(control_frame, text="Anzahl Würfel:").pack(side="left")
        self.dice_var = tk.IntVar(value=2)
        tk.Spinbox(control_frame, from_=1, to=6, width=5, textvariable=self.dice_var,
                   command=self.rebuild_dice).pack(side="left", padx=5)

        tk.Button(root, text="Würfeln!", command=self.roll,
                  bg="#2196F3", fg="white", font=("Arial", 14), width=15).pack(pady=15)

        self.sum_label = tk.Label(root, text="Summe: -", font=("Arial", 14, "bold"))
        self.sum_label.pack(pady=10)

        self.rebuild_dice()

    def rebuild_dice(self):
        for c in self.canvases:
            c.destroy()
        self.canvases = []
        n = self.dice_var.get()
        for i in range(n):
            c = tk.Canvas(self.canvas_frame, width=70, height=70, bg="white",
                           highlightthickness=2, highlightbackground="#333")
            c.grid(row=i // 3, column=i % 3, padx=8, pady=8)
            self.canvases.append(c)
        self.draw_face(0, [1] * n if n else [])
        for c in self.canvases:
            self.draw_pips(c, 1)

    def draw_pips(self, canvas, value):
        canvas.delete("all")
        for row, col in PIPS[value]:
            x = 12 + col * 23
            y = 12 + row * 23
            canvas.create_oval(x, y, x + 12, y + 12, fill="#222")

    def draw_face(self, idx, values):
        pass

    def roll(self):
        results = []
        for c in self.canvases:
            value = random.randint(1, 6)
            results.append(value)
            self.draw_pips(c, value)
        self.sum_label.config(text=f"Summe: {sum(results)}  ({', '.join(map(str, results))})")


if __name__ == "__main__":
    root = tk.Tk()
    app = Wuerfel(root)
    root.mainloop()
