import tkinter as tk
import random

WIDTH, HEIGHT = 400, 500
GRAVITY = 0.6
JUMP = -9
PIPE_GAP = 140
PIPE_WIDTH = 60
PIPE_SPEED = 3

class Flappy:
    def __init__(self, root):
        self.root = root
        self.root.title("Flappy Bird")

        tk.Label(root, text="Flappy Bird", font=("Arial", 18, "bold")).pack(pady=5)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#70c5ce", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        self.root.bind("<space>", self.jump)
        self.canvas.bind("<Button-1>", self.jump)

        self.info_label = tk.Label(root, text="Leertaste / Klick zum Fliegen", font=("Arial", 10))
        self.info_label.pack()

        self.reset()
        self.loop()

    def reset(self):
        self.bird_x = 80
        self.bird_y = HEIGHT // 2
        self.velocity = 0
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.spawn_timer = 0
        self.spawn_pipe()

    def spawn_pipe(self):
        gap_y = random.randint(80, HEIGHT - 80 - PIPE_GAP)
        self.pipes.append({"x": WIDTH, "gap_y": gap_y, "scored": False})

    def jump(self, event=None):
        if self.game_over:
            self.reset()
            return
        self.velocity = JUMP

    def loop(self):
        if not self.game_over:
            self.update()
        self.draw()
        self.root.after(30, self.loop)

    def update(self):
        self.velocity += GRAVITY
        self.bird_y += self.velocity

        for pipe in self.pipes:
            pipe["x"] -= PIPE_SPEED
            if not pipe["scored"] and pipe["x"] + PIPE_WIDTH < self.bird_x:
                pipe["scored"] = True
                self.score += 1

        self.pipes = [p for p in self.pipes if p["x"] > -PIPE_WIDTH]

        self.spawn_timer += 1
        if self.spawn_timer > 90:
            self.spawn_timer = 0
            self.spawn_pipe()

        if self.bird_y < 0 or self.bird_y > HEIGHT:
            self.game_over = True

        bird_r = 12
        for pipe in self.pipes:
            if pipe["x"] < self.bird_x + bird_r < pipe["x"] + PIPE_WIDTH or \
               pipe["x"] < self.bird_x - bird_r < pipe["x"] + PIPE_WIDTH:
                if self.bird_y - bird_r < pipe["gap_y"] or self.bird_y + bird_r > pipe["gap_y"] + PIPE_GAP:
                    self.game_over = True

    def draw(self):
        self.canvas.delete("all")
        for pipe in self.pipes:
            self.canvas.create_rectangle(pipe["x"], 0, pipe["x"] + PIPE_WIDTH, pipe["gap_y"],
                                          fill="#4CAF50", outline="#2e7d32")
            self.canvas.create_rectangle(pipe["x"], pipe["gap_y"] + PIPE_GAP, pipe["x"] + PIPE_WIDTH, HEIGHT,
                                          fill="#4CAF50", outline="#2e7d32")

        self.canvas.create_oval(self.bird_x - 12, self.bird_y - 12, self.bird_x + 12, self.bird_y + 12,
                                 fill="#FFEB3B", outline="#F57F17")

        self.canvas.create_text(WIDTH // 2, 30, text=str(self.score), font=("Arial", 24, "bold"), fill="white")

        if self.game_over:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER\nKlick zum Neustart",
                                     fill="white", font=("Arial", 18, "bold"), justify="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = Flappy(root)
    root.mainloop()
