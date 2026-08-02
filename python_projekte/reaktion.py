import tkinter as tk
import random
import time

class ReaktionsTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaktionstest")
        self.root.geometry("400x350")
        self.state = "idle"
        self.start_time = None
        self.after_id = None

        tk.Label(root, text="Reaktionstest", font=("Arial", 20, "bold")).pack(pady=15)

        self.status_label = tk.Label(root, text="Klicke 'Start', warte auf GRÜN,\ndann klicke so schnell wie möglich!",
                                      font=("Arial", 11))
        self.status_label.pack(pady=5)

        self.box = tk.Canvas(root, width=300, height=150, bg="#888", highlightthickness=2,
                              highlightbackground="#333")
        self.box.pack(pady=15)
        self.box_text = self.box.create_text(150, 75, text="Bereit?", font=("Arial", 16, "bold"), fill="white")
        self.box.bind("<Button-1>", lambda e: self.on_click())

        self.start_btn = tk.Button(root, text="Start", command=self.start_round,
                                    bg="#2196F3", fg="white", font=("Arial", 12), width=12)
        self.start_btn.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def start_round(self):
        self.state = "waiting"
        self.box.config(bg="#c0392b")
        self.box.itemconfig(self.box_text, text="Warte...")
        self.result_label.config(text="")
        delay = random.randint(1500, 4000)
        self.after_id = self.root.after(delay, self.go_green)

    def go_green(self):
        self.state = "ready"
        self.box.config(bg="#27ae60")
        self.box.itemconfig(self.box_text, text="JETZT KLICKEN!")
        self.start_time = time.time()

    def on_click(self):
        if self.state == "waiting":
            if self.after_id:
                self.root.after_cancel(self.after_id)
            self.result_label.config(text="Zu früh geklickt! Nochmal versuchen.", fg="orange")
            self.box.config(bg="#888")
            self.box.itemconfig(self.box_text, text="Bereit?")
            self.state = "idle"
        elif self.state == "ready":
            elapsed = (time.time() - self.start_time) * 1000
            self.result_label.config(text=f"Reaktionszeit: {elapsed:.0f} ms", fg="lightgreen")
            self.box.config(bg="#888")
            self.box.itemconfig(self.box_text, text="Bereit?")
            self.state = "idle"


if __name__ == "__main__":
    root = tk.Tk()
    app = ReaktionsTest(root)
    root.mainloop()
