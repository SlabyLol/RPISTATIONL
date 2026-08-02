import tkinter as tk
import random
import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "×": operator.mul,
}


class BossFight:
    def __init__(self, root):
        self.root = root
        self.root.title("Mathe Bossfight")
        self.root.geometry("450x560")

        tk.Label(root, text="Mathe Bossfight", font=("Arial", 20, "bold")).pack(pady=10)

        self.boss_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#b71c1c")
        self.boss_label.pack(pady=5)
        self.boss_hp_canvas = tk.Canvas(root, width=300, height=20, bg="#555", highlightthickness=0)
        self.boss_hp_canvas.pack()
        self.boss_hp_bar = self.boss_hp_canvas.create_rectangle(0, 0, 300, 20, fill="#e53935")

        self.player_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#1565c0")
        self.player_label.pack(pady=(20, 5))
        self.player_hp_canvas = tk.Canvas(root, width=300, height=20, bg="#555", highlightthickness=0)
        self.player_hp_canvas.pack()
        self.player_hp_bar = self.player_hp_canvas.create_rectangle(0, 0, 300, 20, fill="#43a047")

        self.question_label = tk.Label(root, text="", font=("Arial", 22, "bold"), fg="#6a1b9a")
        self.question_label.pack(pady=(20, 5))

        answer_frame = tk.Frame(root)
        answer_frame.pack(pady=5)
        self.answer_entry = tk.Entry(answer_frame, font=("Arial", 14), justify="center", width=8)
        self.answer_entry.pack(side="left", padx=5)
        self.answer_entry.bind("<Return>", lambda e: self.attack())
        self.attack_btn = tk.Button(answer_frame, text="Angreifen", command=self.attack,
                                     bg="#e53935", fg="white", font=("Arial", 12))
        self.attack_btn.pack(side="left", padx=5)

        self.log = tk.Text(root, height=7, width=45, state="disabled", font=("Arial", 10))
        self.log.pack(pady=15)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.heal_btn = tk.Button(btn_frame, text="Heilen", command=self.heal,
                                   bg="#43a047", fg="white", font=("Arial", 12), width=12)
        self.heal_btn.grid(row=0, column=0, padx=5)
        self.defend_btn = tk.Button(btn_frame, text="Verteidigen", command=self.defend,
                                     bg="#1565c0", fg="white", font=("Arial", 12), width=12)
        self.defend_btn.grid(row=0, column=1, padx=5)

        self.restart_btn = tk.Button(root, text="Neu starten", command=self.reset, bg="#555", fg="white")
        self.restart_btn.pack(pady=10)

        self.reset()

    def reset(self):
        self.boss_hp_max = 120
        self.boss_hp = self.boss_hp_max
        self.player_hp_max = 100
        self.player_hp = self.player_hp_max
        self.heals_left = 3
        self.defending = False
        self.over = False
        self.update_bars()
        self.log_clear()
        self.write_log("Der Kampf beginnt! Löse Mathe-Aufgaben, um den Drachenboss zu besiegen!")
        self.new_question()
        self.answer_entry.config(state="normal")
        self.answer_entry.focus()

    def new_question(self):
        op_symbol = random.choice(list(OPS.keys()))
        if op_symbol == "×":
            a, b = random.randint(2, 12), random.randint(2, 12)
        else:
            a, b = random.randint(5, 50), random.randint(1, 50)
            if op_symbol == "-" and b > a:
                a, b = b, a
        self.current_answer = OPS[op_symbol](a, b)
        self.question_label.config(text=f"{a} {op_symbol} {b} = ?")
        self.answer_entry.delete(0, tk.END)

    def log_clear(self):
        self.log.config(state="normal")
        self.log.delete("1.0", tk.END)
        self.log.config(state="disabled")

    def write_log(self, text):
        self.log.config(state="normal")
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)
        self.log.config(state="disabled")

    def update_bars(self):
        boss_ratio = max(self.boss_hp, 0) / self.boss_hp_max
        player_ratio = max(self.player_hp, 0) / self.player_hp_max
        self.boss_hp_canvas.coords(self.boss_hp_bar, 0, 0, 300 * boss_ratio, 20)
        self.player_hp_canvas.coords(self.player_hp_bar, 0, 0, 300 * player_ratio, 20)
        self.boss_label.config(text=f"Drachenboss HP: {max(self.boss_hp,0)}/{self.boss_hp_max}")
        self.player_label.config(text=f"Du HP: {max(self.player_hp,0)}/{self.player_hp_max}")

    def attack(self):
        if self.over:
            return
        try:
            guess = int(self.answer_entry.get())
        except ValueError:
            self.write_log("Bitte eine Zahl eingeben!")
            return

        if guess == self.current_answer:
            dmg = random.randint(15, 25)
            self.boss_hp -= dmg
            self.write_log(f"Richtig! Du greifst an und verursachst {dmg} Schaden!")
        else:
            self.write_log(f"Falsch! Die richtige Antwort war {self.current_answer}. Kein Schaden!")

        self.defending = False
        self.new_question()
        self.check_end_and_boss_turn()

    def heal(self):
        if self.over:
            return
        if self.heals_left <= 0:
            self.write_log("Keine Heilungen mehr übrig!")
            return
        self.heals_left -= 1
        heal_amount = random.randint(15, 25)
        self.player_hp = min(self.player_hp_max, self.player_hp + heal_amount)
        self.write_log(f"Du heilst dich um {heal_amount} HP. ({self.heals_left} Heilungen übrig)")
        self.defending = False
        self.check_end_and_boss_turn()

    def defend(self):
        if self.over:
            return
        self.defending = True
        self.write_log("Du gehst in Verteidigungsstellung.")
        self.check_end_and_boss_turn()

    def check_end_and_boss_turn(self):
        self.update_bars()
        if self.boss_hp <= 0:
            self.write_log("Der Drachenboss ist besiegt! DU HAST GEWONNEN!")
            self.over = True
            self.answer_entry.config(state="disabled")
            return

        dmg = random.randint(8, 22)
        if self.defending:
            dmg = dmg // 2
            self.write_log("Der Boss greift an, aber du blockst einen Teil des Schadens!")
        self.player_hp -= dmg
        self.write_log(f"Der Drachenboss greift an und verursacht {dmg} Schaden!")
        self.update_bars()

        if self.player_hp <= 0:
            self.write_log("Du wurdest besiegt... GAME OVER.")
            self.over = True
            self.answer_entry.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = BossFight(root)
    root.mainloop()
