#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.title("LED Rainbow")
root.geometry("470x180")
root.configure(bg="black")

canvas = tk.Canvas(root, width=450, height=100, bg="black", highlightthickness=0)
canvas.pack(pady=20)

colors = [
    "red",
    "orange",
    "yellow",
    "lime",
    "cyan",
    "blue",
    "magenta",
    "white"
]

leds = []

for i in range(8):
    x = 20 + i * 52
    led = canvas.create_oval(
        x, 30,
        x + 35, 65,
        fill=colors[i],
        outline="white",
        width=2
    )
    leds.append(led)

running = True
offset = 0


def animate():
    global offset
    if running:
        for i in range(8):
            canvas.itemconfig(
                leds[i],
                fill=colors[(i + offset) % len(colors)]
            )
        offset += 1
    root.after(180, animate)


def toggle():
    global running
    running = not running
    btn.config(text="Start" if not running else "Stop")


btn = tk.Button(root, text="Stop", command=toggle)
btn.pack()

animate()
root.mainloop()
