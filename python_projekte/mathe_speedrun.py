import tkinter as tk
import random
import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "×": operator.mul,
}

class MatheSpeedrun:
    def __init__(self, root):
        self.root = root
        self.root.title("Mathe Speedrun")
        self.root.geometry("400x400")

        tk.Label(root, text="Mathe Speedrun", font=("Arial", 20, "bold")).pack(pady=15)

        self.time_label = tk.Label(root, text="Zeit: 60", font=("Arial", 14, "bold"), fg="#c62828")
        self.time_label.pack(pady=5)

        self.score_label = tk.Label(root, text="Punkte: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.question_label = tk.Label(root, text="", font=("Arial", 28, "bold"))
        self.question_label.pack(pady=25)

        self.entry = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda e: self.check_answer())

        tk.Button(root, text="Antworten", command=self.check_answer,
                  bg="#2196F3", fg="white", font=("Arial", 12), width=15).pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.feedback_label.pack(pady=5)

        self.start_btn = tk.Button(root, text="Start", command=self.start_game,
                                    bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
        self.start_btn.pack(pady=15)

        self.running = False

    def start_game(self):
        self.score = 0
        self.time_left = 60
        self.running = True
        self.score_label.config(text="Punkte: 0")
        self.entry.config(state="normal")
        self.new_question()
        self.entry.focus()
        self.countdown()

    def new_question(self):
        op_symbol = random.choice(list(OPS.keys()))
        if op_symbol == "×":
            a, b = random.randint(2, 12), random.randint(2, 12)
        else:
            a, b = random.randint(1, 100), random.randint(1, 100)
            if op_symbol == "-" and b > a:
                a, b = b, a
        self.answer = OPS[op_symbol](a, b)
        self.question_label.config(text=f"{a} {op_symbol} {b} = ?")
        self.entry.delete(0, tk.END)

    def check_answer(self):
        if not self.running:
            return
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.feedback_label.config(text="Bitte eine Zahl eingeben!", fg="orange")
            return

        if guess == self.answer:
            self.score += 1
            self.score_label.config(text=f"Punkte: {self.score}")
            self.feedback_label.config(text="Richtig!", fg="lightgreen" if False else "green")
        else:
            self.feedback_label.config(text=f"Falsch! Richtig war {self.answer}", fg="red")

        self.new_question()

    def countdown(self):
        if not self.running:
            return
        if self.time_left <= 0:
            self.end_game()
            return
        self.time_label.config(text=f"Zeit: {self.time_left}")
        self.time_left -= 1
        self.root.after(1000, self.countdown)

    def end_game(self):
        self.running = False
        self.question_label.config(text="Zeit abgelaufen!")
        self.feedback_label.config(text=f"Endpunktzahl: {self.score}", fg="blue")
        self.entry.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatheSpeedrun(root)
    root.mainloop()
