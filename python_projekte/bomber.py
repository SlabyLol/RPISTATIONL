import tkinter as tk
import random

CELL = 40
COLS, ROWS = 11, 9
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL

EMPTY, WALL, BLOCK = 0, 1, 2

class Bomber:
    def __init__(self, root):
        self.root = root
        self.root.title("Bomber")

        tk.Label(root, text="Bomber", font=("Arial", 18, "bold")).pack(pady=5)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#7cb342", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        self.info_label = tk.Label(root, text="Pfeiltasten = bewegen, Leertaste = Bombe legen",
                                    font=("Arial", 10))
        self.info_label.pack()
        self.score_label = tk.Label(root, text="Punkte: 0", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=5)

        self.root.bind("<Key>", self.on_key)
        self.reset()
        self.loop()

    def reset(self):
        self.grid = [[EMPTY] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1 or (r % 2 == 0 and c % 2 == 0):
                    self.grid[r][c] = WALL
                elif random.random() < 0.35 and not (r <= 2 and c <= 2):
                    self.grid[r][c] = BLOCK
        self.player = [1, 1]
        self.bombs = []
        self.explosions = []
        self.score = 0
        self.game_over = False
        self.score_label.config(text="Punkte: 0")

    def on_key(self, event):
        if self.game_over:
            if event.keysym == "space":
                self.reset()
            return
        r, c = self.player
        if event.keysym == "Up" and self.grid[r - 1][c] == EMPTY:
            self.player[0] -= 1
        elif event.keysym == "Down" and self.grid[r + 1][c] == EMPTY:
            self.player[0] += 1
        elif event.keysym == "Left" and self.grid[r][c - 1] == EMPTY:
            self.player[1] -= 1
        elif event.keysym == "Right" and self.grid[r][c + 1] == EMPTY:
            self.player[1] += 1
        elif event.keysym == "space":
            self.place_bomb()

    def place_bomb(self):
        pos = tuple(self.player)
        if not any(b["pos"] == pos for b in self.bombs):
            self.bombs.append({"pos": pos, "timer": 60})

    def loop(self):
        if not self.game_over:
            self.update()
        self.draw()
        self.root.after(50, self.loop)

    def update(self):
        for bomb in self.bombs[:]:
            bomb["timer"] -= 1
            if bomb["timer"] <= 0:
                self.explode(bomb["pos"])
                self.bombs.remove(bomb)

        for exp in self.explosions[:]:
            exp["timer"] -= 1
            if exp["timer"] <= 0:
                self.explosions.remove(exp)

        for exp in self.explosions:
            if list(exp["pos"]) == self.player:
                self.game_over = True

    def explode(self, pos):
        r, c = pos
        cells = [(r, c)]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and self.grid[nr][nc] != WALL:
                cells.append((nr, nc))
                if self.grid[nr][nc] == BLOCK:
                    self.grid[nr][nc] = EMPTY
                    self.score += 10
                    self.score_label.config(text=f"Punkte: {self.score}")

        for cell in cells:
            self.explosions.append({"pos": cell, "timer": 15})

    def draw(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x, y = c * CELL, r * CELL
                if self.grid[r][c] == WALL:
                    self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill="#5d4037", outline="#3e2723")
                elif self.grid[r][c] == BLOCK:
                    self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill="#a1887f", outline="#6d4c41")

        for bomb in self.bombs:
            r, c = bomb["pos"]
            x, y = c * CELL + CELL // 2, r * CELL + CELL // 2
            self.canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill="#212121")

        for exp in self.explosions:
            r, c = exp["pos"]
            x, y = c * CELL, r * CELL
            self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill="#ff9800", outline="")

        pr, pc = self.player
        px, py = pc * CELL + CELL // 2, pr * CELL + CELL // 2
        self.canvas.create_oval(px - 15, py - 15, px + 15, py + 15, fill="#2196F3", outline="")

        if self.game_over:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER\nLeertaste für Neustart",
                                     fill="white", font=("Arial", 18, "bold"), justify="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = Bomber(root)
    root.mainloop()
