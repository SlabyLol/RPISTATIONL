#!/usr/bin/env python3
import tkinter as tk

root = tk.Tk()
root.title("LED Simulator")
root.geometry("450x250")
root.configure(bg="#202020")

leds = []

canvas = tk.Canvas(root, width=420, height=120, bg="#202020", highlightthickness=0)
canvas.pack(pady=20)

for i in range(8):
    x = 40 + i * 45
    led = canvas.create_oval(x, 40, x + 30, 70, fill="gray20", outline="white")
    leds.append(led)

status = [False] * 8


def toggle(index):
    status[index] = not status[index]
    color = "lime" if status[index] else "gray20"
    canvas.itemconfig(leds[index], fill=color)


button_frame = tk.Frame(root, bg="#202020")
button_frame.pack()

for i in range(8):
    tk.Button(
        button_frame,
        text=str(i + 1),
        width=3,
        command=lambda i=i: toggle(i)
    ).grid(row=0, column=i, padx=3)


def all_on():
    for i in range(8):
        status[i] = True
        canvas.itemconfig(leds[i], fill="lime")


def all_off():
    for i in range(8):
        status[i] = False
        canvas.itemconfig(leds[i], fill="gray20")


bottom = tk.Frame(root, bg="#202020")
bottom.pack(pady=15)

tk.Button(bottom, text="Alle AN", command=all_on).pack(side="left", padx=10)
tk.Button(bottom, text="Alle AUS", command=all_off).pack(side="left", padx=10)

root.mainloop()
