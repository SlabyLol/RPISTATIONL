import tkinter as tk
import random

CELL = 20
COLS, ROWS = 25, 20
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL

class Snake:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.root.configure(bg="#111")

        tk.Label(root, text="Snake", font=("Arial", 18, "bold"), bg="#111", fg="white").pack(pady=5)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#000", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        self.score_label = tk.Label(root, text="Punkte: 0", font=("Arial", 12), bg="#111", fg="white")
        self.score_label.pack(pady=5)

        self.root.bind("<Key>", self.on_key)

        self.restart_btn = tk.Button(root, text="Neu starten", command=self.reset,
                                      bg="#555", fg="white")
        self.restart_btn.pack(pady=5)

        self.reset()

    def reset(self):
        self.snake = [(COLS // 2, ROWS // 2), (COLS // 2 - 1, ROWS // 2), (COLS // 2 - 2, ROWS // 2)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.game_over = False
        self.spawn_food()
        self.score_label.config(text="Punkte: 0")
        self.loop()

    def spawn_food(self):
        while True:
            pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if pos not in self.snake:
                self.food = pos
                break

    def on_key(self, event):
        key = event.keysym
        if key == "Up" and self.direction != (0, 1):
            self.next_direction = (0, -1)
        elif key == "Down" and self.direction != (0, -1):
            self.next_direction = (0, 1)
        elif key == "Left" and self.direction != (1, 0):
            self.next_direction = (-1, 0)
        elif key == "Right" and self.direction != (-1, 0):
            self.next_direction = (1, 0)
        elif key == "space" and self.game_over:
            self.reset()

    def loop(self):
        if self.game_over:
            return
        self.direction = self.next_direction
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if (new_head[0] < 0 or new_head[0] >= COLS or
                new_head[1] < 0 or new_head[1] >= ROWS or
                new_head in self.snake):
            self.end_game()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Punkte: {self.score}")
            self.spawn_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(120, self.loop)

    def draw(self):
        self.canvas.delete("all")
        for i, (x, y) in enumerate(self.snake):
            color = "#4CAF50" if i > 0 else "#8BC34A"
            self.canvas.create_rectangle(x * CELL, y * CELL, x * CELL + CELL, y * CELL + CELL,
                                          fill=color, outline="#000")
        fx, fy = self.food
        self.canvas.create_oval(fx * CELL, fy * CELL, fx * CELL + CELL, fy * CELL + CELL,
                                 fill="#f44336", outline="")

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER\nLeertaste für Neustart",
                                 fill="white", font=("Arial", 18, "bold"), justify="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = Snake(root)
    root.mainloop()
