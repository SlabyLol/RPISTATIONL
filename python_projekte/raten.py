#!/usr/bin/env python3

import tkinter as tk
import random

zahl = random.randint(1, 100)

root = tk.Tk()
root.title("Zahl erraten")
root.geometry("320x220")

tk.Label(root, text="Errate eine Zahl zwischen 1 und 100").pack(pady=10)

eingabe = tk.Entry(root, justify="center")
eingabe.pack()

ausgabe = tk.Label(root, text="")
ausgabe.pack(pady=15)


def pruefen():
    global zahl

    try:
        tipp = int(eingabe.get())
    except:
        ausgabe.config(text="Bitte eine Zahl eingeben.")
        return

    if tipp < zahl:
        ausgabe.config(text="Zu klein!")
    elif tipp > zahl:
        ausgabe.config(text="Zu groß!")
    else:
        ausgabe.config(text="🎉 Richtig!")
        zahl = random.randint(1, 100)
        eingabe.delete(0, tk.END)


tk.Button(root, text="Prüfen", command=pruefen).pack(pady=10)

root.mainloop()
