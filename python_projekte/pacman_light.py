import tkinter as tk
import random

CELL = 30
MAZE = [
    "###########",
    "#....#....#",
    "#.##.#.##.#",
    "#.........#",
    "#.##.#.##.#",
    "#....#....#",
    "#.#######.#",
    "#.........#",
    "#.##.#.##.#",
    "#....#....#",
    "###########",
]
ROWS = len(MAZE)
COLS = len(MAZE[0])
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL


class PacmanLight:
    def __init__(self, root):
        self.root = root
        self.root.title("Pacman Light")

        tk.Label(root, text="Pacman Light", font=("Arial", 18, "bold")).pack(pady=5)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        self.score_label = tk.Label(root, text="Punkte: 0", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=5)
        self.info_label = tk.Label(root, text="Pfeiltasten zum Bewegen", font=("Arial", 10))
        self.info_label.pack()

        self.root.bind("<Key>", self.on_key)
        self.reset()
        self.loop()

    def reset(self):
        self.walls = set()
        self.dots = set()
        for r, row in enumerate(MAZE):
            for c, ch in enumerate(row):
                if ch == "#":
                    self.walls.add((r, c))
                elif ch == ".":
                    self.dots.add((r, c))

        self.player = [1, 1]
        self.dots.discard(tuple(self.player))
        self.direction = (0, 0)
        self.ghost = [ROWS - 2, COLS - 2]
        self.score = 0
        self.game_over = False
        self.won = False
        self.score_label.config(text="Punkte: 0")

    def on_key(self, event):
        if self.game_over:
            if event.keysym == "space":
                self.reset()
            return
        if event.keysym == "Up":
            self.direction = (-1, 0)
        elif event.keysym == "Down":
            self.direction = (1, 0)
        elif event.keysym == "Left":
            self.direction = (0, -1)
        elif event.keysym == "Right":
            self.direction = (0, 1)

    def loop(self):
        if not self.game_over:
            self.update()
        self.draw()
        self.root.after(200, self.loop)

    def update(self):
        r, c = self.player
        nr, nc = r + self.direction[0], c + self.direction[1]
        if (nr, nc) not in self.walls and 0 <= nr < ROWS and 0 <= nc < COLS:
            self.player = [nr, nc]

        pos = tuple(self.player)
        if pos in self.dots:
            self.dots.remove(pos)
            self.score += 10
            self.score_label.config(text=f"Punkte: {self.score}")

        if not self.dots:
            self.game_over = True
            self.won = True

        # Geist bewegt sich zufällig, bevorzugt Richtung Spieler
        gr, gc = self.ghost
        options = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ngr, ngc = gr + dr, gc + dc
            if (ngr, ngc) not in self.walls and 0 <= ngr < ROWS and 0 <= ngc < COLS:
                options.append((ngr, ngc))
        if options:
            options.sort(key=lambda p: abs(p[0] - self.player[0]) + abs(p[1] - self.player[1]))
            if random.random() < 0.7:
                self.ghost = list(options[0])
            else:
                self.ghost = list(random.choice(options))

        if self.ghost == self.player:
            self.game_over = True
            self.won = False

    def draw(self):
        self.canvas.delete("all")
        for (r, c) in self.walls:
            x, y = c * CELL, r * CELL
            self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill="#1a237e", outline="#0d1350")

        for (r, c) in self.dots:
            x, y = c * CELL + CELL // 2, r * CELL + CELL // 2
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="#ffeb3b", outline="")

        pr, pc = self.player
        px, py = pc * CELL, pr * CELL
        self.canvas.create_oval(px + 3, py + 3, px + CELL - 3, py + CELL - 3, fill="#ffeb3b", outline="")

        gr, gc = self.ghost
        gx, gy = gc * CELL, gr * CELL
        self.canvas.create_oval(gx + 3, gy + 3, gx + CELL - 3, gy + CELL - 3, fill="#f44336", outline="")

        if self.game_over:
            msg = "GEWONNEN!" if self.won else "GAME OVER"
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"{msg}\nLeertaste für Neustart",
                                     fill="white", font=("Arial", 16, "bold"), justify="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = PacmanLight(root)
    root.mainloop()
