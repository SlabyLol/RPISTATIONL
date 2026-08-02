import tkinter as tk
from collections import Counter
import re

class WordCount:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordcount")
        self.root.geometry("600x550")

        tk.Label(root, text="Wordcount Tool", font=("Arial", 18, "bold")).pack(pady=10)

        self.text = tk.Text(root, height=12, width=65, font=("Arial", 11))
        self.text.pack(pady=10, padx=10)

        tk.Button(root, text="Analysieren", command=self.analyze,
                  bg="#2196F3", fg="white", font=("Arial", 12), width=15).pack(pady=5)

        self.stats_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
        self.stats_label.pack(pady=10)

        tk.Label(root, text="Häufigste Wörter:", font=("Arial", 11, "bold")).pack()
        self.freq_text = tk.Text(root, height=8, width=65, font=("Arial", 10), state="disabled")
        self.freq_text.pack(pady=5, padx=10)

    def analyze(self):
        content = self.text.get("1.0", tk.END)
        words = re.findall(r"[A-Za-zÄÖÜäöüß]+", content)
        chars = len(content.rstrip("\n"))
        chars_no_space = len(content.replace(" ", "").replace("\n", ""))
        lines = content.count("\n") + (1 if content.strip() else 0)
        num_words = len(words)

        stats = (f"Wörter: {num_words}\n"
                 f"Zeichen (mit Leerzeichen): {chars}\n"
                 f"Zeichen (ohne Leerzeichen): {chars_no_space}\n"
                 f"Zeilen: {lines}")
        self.stats_label.config(text=stats)

        counter = Counter(w.lower() for w in words)
        top = counter.most_common(10)

        self.freq_text.config(state="normal")
        self.freq_text.delete("1.0", tk.END)
        for word, count in top:
            self.freq_text.insert(tk.END, f"{word}: {count}\n")
        self.freq_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = WordCount(root)
    root.mainloop()
