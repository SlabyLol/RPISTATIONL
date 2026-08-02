import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import os
from datetime import datetime

current_img = None

def update_qr(event=None):
    global current_img

    text = text_entry.get("1.0", tk.END).strip()

    if not text:
        qr_label.config(image="")
        qr_label.image = None
        current_img = None
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    current_img = img

    photo = ImageTk.PhotoImage(img)

    qr_label.config(image=photo)
    qr_label.image = photo


def save_qr():
    global current_img

    if current_img is None:
        return

    os.makedirs("qrs", exist_ok=True)

    name = name_entry.get().strip()

    if not name:
        name = datetime.now().strftime("qr_%Y%m%d_%H%M%S")

    for c in '\\/:*?"<>|':
        name = name.replace(c, "_")

    current_img.save(f"qrs/{name}.png")

    status.config(text=f"Gespeichert: qrs/{name}.png")


root = tk.Tk()
root.title("QR-Code Generator")
root.geometry("750x450")

left = tk.Frame(root)
left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right = tk.Frame(root)
right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(left, text="Text:").pack(anchor="w")

text_entry = tk.Text(left, width=40, height=12)
text_entry.pack(fill="both", expand=True)
text_entry.bind("<KeyRelease>", update_qr)

tk.Label(left, text="Dateiname:").pack(anchor="w", pady=(10, 0))

name_entry = tk.Entry(left)
name_entry.pack(fill="x")

tk.Button(left, text="Speichern", command=save_qr).pack(pady=10)

status = tk.Label(left, text="")
status.pack()

qr_label = tk.Label(right)
qr_label.pack(expand=True)

root.mainloop()
