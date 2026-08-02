import tkinter as tk

PASSWORT = "1234"

class PasswortTuer:
    def __init__(self, root):
        self.root = root
        self.root.title("Passwort-Tür")
        self.root.geometry("400x400")
        self.root.configure(bg="#222")
        self.open_state = False

        tk.Label(root, text="Geheime Tür", font=("Arial", 20, "bold"),
                 bg="#222", fg="white").pack(pady=15)

        self.canvas = tk.Canvas(root, width=200, height=200, bg="#222", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.door_left = self.canvas.create_rectangle(0, 0, 100, 200, fill="#8B4513", outline="#333")
        self.door_right = self.canvas.create_rectangle(100, 0, 200, 200, fill="#8B4513", outline="#333")
        self.canvas.create_oval(90, 95, 100, 105, fill="#ffd700", outline="")
        self.canvas.create_oval(100, 95, 110, 105, fill="#ffd700", outline="")

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center", show="*")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda e: self.check_password())
        self.entry.focus()

        tk.Button(root, text="Öffnen", command=self.check_password,
                  bg="#2196F3", fg="white", font=("Arial", 12), width=12).pack(pady=5)

        self.status_label = tk.Label(root, text="Gib das Passwort ein (Tipp: 1234)",
                                      font=("Arial", 10), bg="#222", fg="#aaa")
        self.status_label.pack(pady=10)

    def check_password(self):
        if self.entry.get() == PASSWORT:
            self.open_door()
        else:
            self.status_label.config(text="Falsches Passwort!", fg="red")
            self.shake_door()
        self.entry.delete(0, tk.END)

    def open_door(self):
        self.status_label.config(text="Zugang gewährt! Tür öffnet sich...", fg="lightgreen")
        self.animate_open(0)

    def animate_open(self, step):
        if step > 40:
            return
        self.canvas.coords(self.door_left, -step * 2, 0, 100 - step * 2, 200)
        self.canvas.coords(self.door_right, 100 + step * 2, 0, 200 + step * 2, 200)
        self.root.after(20, lambda: self.animate_open(step + 1))

    def shake_door(self):
        orig_x = 0
        for dx in [10, -10, 8, -8, 5, -5, 0]:
            self.root.after(0, lambda dx=dx: self.canvas.move(self.door_left, dx, 0))
            self.root.after(0, lambda dx=dx: self.canvas.move(self.door_right, dx, 0))


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswortTuer(root)
    root.mainloop()
