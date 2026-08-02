import tkinter as tk

STORY = {
    "start": {
        "text": "Du wachst in einem dunklen Wald auf. Vor dir teilt sich der Weg.",
        "options": [
            ("Nach links gehen", "hoehle"),
            ("Nach rechts gehen", "fluss"),
        ],
    },
    "hoehle": {
        "text": "Du findest eine Höhle. Aus ihr dringt ein leises Knurren.",
        "options": [
            ("Hineingehen", "drache"),
            ("Zurück zum Weg", "start"),
        ],
    },
    "fluss": {
        "text": "Du erreichst einen reißenden Fluss. Eine wacklige Brücke führt hinüber.",
        "options": [
            ("Über die Brücke gehen", "dorf"),
            ("Am Ufer entlang gehen", "boot"),
        ],
    },
    "drache": {
        "text": "Ein Drache! Er sieht dich an, scheint aber müde zu sein.",
        "options": [
            ("Angreifen", "ende_tod"),
            ("Leise weggehen", "schatz"),
        ],
    },
    "schatz": {
        "text": "Während der Drache schläft, entdeckst du einen Schatz in der Ecke!",
        "options": [
            ("Schatz nehmen und fliehen", "ende_sieg"),
        ],
    },
    "dorf": {
        "text": "Du erreichst ein friedliches Dorf. Die Bewohner heißen dich willkommen.",
        "options": [
            ("Im Dorf bleiben", "ende_dorf"),
        ],
    },
    "boot": {
        "text": "Du findest ein altes Boot und fährst den Fluss hinunter, bis du das Meer erreichst.",
        "options": [
            ("Weiter aufs Meer hinausfahren", "ende_meer"),
        ],
    },
    "ende_tod": {"text": "Der Drache war doch nicht so müde... GAME OVER.", "options": []},
    "ende_sieg": {"text": "Du entkommst mit dem Schatz! GEWONNEN!", "options": []},
    "ende_dorf": {"text": "Du lässt dich im Dorf nieder und lebst glücklich. ENDE.", "options": []},
    "ende_meer": {"text": "Du segelst in neue Abenteuer hinaus. ENDE.", "options": []},
}


class Adventure:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-Adventure")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("500x400")

        tk.Label(root, text="Das Waldabenteuer", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white").pack(pady=15)

        self.text_label = tk.Label(root, text="", font=("Arial", 12), wraplength=440,
                                    bg="#1e1e1e", fg="white", justify="left")
        self.text_label.pack(pady=15, padx=20)

        self.btn_frame = tk.Frame(root, bg="#1e1e1e")
        self.btn_frame.pack(pady=10)

        self.restart_btn = tk.Button(root, text="Neu starten", command=self.restart,
                                      bg="#555", fg="white")
        self.restart_btn.pack(pady=10)

        self.goto("start")

    def goto(self, node_key):
        self.node_key = node_key
        node = STORY[node_key]
        self.text_label.config(text=node["text"])

        for widget in self.btn_frame.winfo_children():
            widget.destroy()

        if not node["options"]:
            tk.Label(self.btn_frame, text="--- ENDE ---", font=("Arial", 12, "bold"),
                     bg="#1e1e1e", fg="yellow").pack()
        else:
            for label, target in node["options"]:
                tk.Button(self.btn_frame, text=label, width=30,
                          command=lambda t=target: self.goto(t),
                          bg="#2196F3", fg="white").pack(pady=4)

    def restart(self):
        self.goto("start")


if __name__ == "__main__":
    root = tk.Tk()
    app = Adventure(root)
    root.mainloop()
