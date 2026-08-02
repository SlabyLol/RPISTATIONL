import tkinter as tk
import random

class RatenSpiel:
    def __init__(self, root):
        self.root = root
        self.root.title("Zahlen raten")
        self.root.configure(bg="#1e1e1e")
        self.geometry_reset()

        tk.Label(root, text="Zahlen raten", font=("Arial", 20, "bold"),
                 bg="#1e1e1e", fg="white").pack(pady=15)

        self.info_label = tk.Label(root, text="Ich denke an eine Zahl zwischen 1 und 100.",
                                    font=("Arial", 12), bg="#1e1e1e", fg="white")
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda e: self.check_guess())
        self.entry.focus()

        tk.Button(root, text="Raten", command=self.check_guess,
                  bg="#2196F3", fg="white", font=("Arial", 12), width=12).pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"),
                                      bg="#1e1e1e", fg="yellow")
        self.result_label.pack(pady=10)

        self.attempts_label = tk.Label(root, text="Versuche: 0", font=("Arial", 10),
                                        bg="#1e1e1e", fg="#aaa")
        self.attempts_label.pack()

        tk.Button(root, text="Neues Spiel", command=self.geometry_reset,
                  bg="#555", fg="white").pack(pady=15)

    def geometry_reset(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        if hasattr(self, "result_label"):
            self.result_label.config(text="Neue Zahl gewählt!")
            self.attempts_label.config(text="Versuche: 0")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Bitte eine Zahl eingeben!", fg="orange")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Versuche: {self.attempts}")

        if guess < self.number:
            self.result_label.config(text="Zu niedrig!", fg="cyan")
        elif guess > self.number:
            self.result_label.config(text="Zu hoch!", fg="cyan")
        else:
            self.result_label.config(text=f"Richtig! Die Zahl war {self.number}. "
                                           f"({self.attempts} Versuche)", fg="lightgreen")
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = RatenSpiel(root)
    root.mainloop()
