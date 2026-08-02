import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def make_executable():
    file_path = filedialog.askopenfilename(
        title="Select a Shell Script",
        filetypes=[("Shell Scripts", "*.sh"), ("All Files", "*.*")]
    )

    if not file_path:
        return

    try:
        subprocess.run(["chmod", "+x", file_path], check=True)
        messagebox.showinfo(
            "Success",
            f"The script is now executable:\n\n{file_path}"
        )
    except subprocess.CalledProcessError:
        messagebox.showerror(
            "Error",
            "Failed to make the file executable."
        )

root = tk.Tk()
root.title("CHcollector")
root.geometry("400x180")
root.resizable(False, False)

title = tk.Label(
    root,
    text="CHcollector",
    font=("Arial", 16, "bold")
)
title.pack(pady=(15, 5))

description = tk.Label(
    root,
    text="Select a shell script to make it executable."
)
description.pack(pady=(0, 15))

button = tk.Button(
    root,
    text="Select .sh File",
    command=make_executable,
    width=20
)
button.pack()

root.mainloop()
