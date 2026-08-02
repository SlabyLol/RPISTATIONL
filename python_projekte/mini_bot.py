import tkinter as tk
import random

RULES = [
    (["hallo", "hi", "hey", "servus"], ["Hallo! Wie geht's dir?", "Hey! Schön dich zu sehen.", "Hi! Was gibt's Neues?"]),
    (["wie geht", "geht es dir"], ["Mir geht's gut, danke der Nachfrage!", "Bestens! Und dir?"]),
    (["name"], ["Ich bin MiniBot, dein kleiner Chat-Assistent.", "Man nennt mich MiniBot."]),
    (["wetter"], ["Ich kann leider nicht aus dem Fenster schauen, aber ich hoffe es ist schön bei dir!"]),
    (["witz"], ["Warum können Geister so schlecht lügen? Weil man durch sie hindurchsieht!",
                "Was ist grün und steht vor der Tür? Ein Klopfsalat!"]),
    (["tschüss", "bye", "ciao"], ["Tschüss! Bis bald!", "Ciao! War schön mit dir zu chatten."]),
    (["danke"], ["Gern geschehen!", "Kein Problem!"]),
    (["hilfe"], ["Frag mich einfach etwas, z.B. 'Wie geht es dir?' oder 'Erzähl mir einen Witz'."]),
]

FALLBACKS = [
    "Das habe ich nicht ganz verstanden. Kannst du es anders formulieren?",
    "Interessant! Erzähl mir mehr davon.",
    "Hmm, dazu fällt mir gerade nichts ein.",
]


class MiniBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Bot")
        self.root.geometry("450x500")

        tk.Label(root, text="MiniBot Chat", font=("Arial", 18, "bold")).pack(pady=10)

        self.chat_log = tk.Text(root, height=20, width=52, state="disabled", font=("Arial", 10), wrap="word")
        self.chat_log.pack(padx=10, pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=5, fill="x", padx=10)

        self.entry = tk.Entry(input_frame, font=("Arial", 12))
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda e: self.send())
        self.entry.focus()

        tk.Button(input_frame, text="Senden", command=self.send,
                  bg="#2196F3", fg="white").pack(side="left", padx=5)

        self.append_message("MiniBot", "Hallo! Ich bin MiniBot. Schreib mir etwas!")

    def append_message(self, sender, message):
        self.chat_log.config(state="normal")
        self.chat_log.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_log.see(tk.END)
        self.chat_log.config(state="disabled")

    def get_response(self, text):
        lower = text.lower()
        for keywords, responses in RULES:
            if any(k in lower for k in keywords):
                return random.choice(responses)
        return random.choice(FALLBACKS)

    def send(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.append_message("Du", text)
        self.entry.delete(0, tk.END)
        response = self.get_response(text)
        self.root.after(300, lambda: self.append_message("MiniBot", response))


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBot(root)
    root.mainloop()
