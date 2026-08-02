import tkinter as tk
import re

EMOJI_MAP = {
    "liebe": "❤️", "hund": "🐶", "katze": "🐱", "haus": "🏠", "auto": "🚗",
    "sonne": "☀️", "mond": "🌙", "stern": "⭐", "wasser": "💧", "feuer": "🔥",
    "essen": "🍔", "pizza": "🍕", "kaffee": "☕", "musik": "🎵", "geld": "💰",
    "lachen": "😂", "traurig": "😢", "wütend": "😠", "glücklich": "😊", "müde": "😴",
    "baum": "🌳", "blume": "🌸", "regen": "🌧️", "schnee": "❄️", "party": "🎉",
    "geburtstag": "🎂", "buch": "📚", "computer": "💻", "handy": "📱", "zeit": "⏰",
    "schule": "🏫", "arbeit": "💼", "spiel": "🎮", "fußball": "⚽", "flugzeug": "✈️",
    "zug": "🚆", "geschenk": "🎁", "herz": "💖", "stark": "💪", "fisch": "🐟",
    "vogel": "🐦", "ja": "✅", "nein": "❌", "gut": "👍", "schlecht": "👎",
}

class EmojiTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Übersetzer")
        self.root.geometry("550x500")

        tk.Label(root, text="Emoji Übersetzer", font=("Arial", 18, "bold")).pack(pady=15)
        tk.Label(root, text="Gib einen Text ein - bekannte Wörter werden zu Emojis:",
                 font=("Arial", 10)).pack()

        self.input_text = tk.Text(root, height=6, width=60, font=("Arial", 12))
        self.input_text.pack(pady=10, padx=10)

        tk.Button(root, text="Übersetzen", command=self.translate,
                  bg="#2196F3", fg="white", font=("Arial", 12), width=15).pack(pady=5)

        self.output_text = tk.Text(root, height=6, width=60, font=("Arial", 14), state="disabled")
        self.output_text.pack(pady=15, padx=10)

    def translate(self):
        text = self.input_text.get("1.0", tk.END)

        def replace(match):
            word = match.group(0)
            lower = word.lower()
            return EMOJI_MAP.get(lower, word)

        result = re.sub(r"[A-Za-zÄÖÜäöüß]+", replace, text)

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmojiTranslator(root)
    root.mainloop()
