import tkinter as tk
from PIL import Image, ImageTk
import qrcode

def update_qr(event=None):
    text = entry.get("1.0", tk.END).strip()

    if not text:
        label.config(image="")
        label.image = None
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
    photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo

root = tk.Tk()
root.title("QR-Code Generator")
root.geometry("700x400")

left = tk.Frame(root)
left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right = tk.Frame(root)
right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(left, text="Text eingeben:").pack(anchor="w")

entry = tk.Text(left, width=40, height=15)
entry.pack(fill="both", expand=True)
entry.bind("<KeyRelease>", update_qr)

label = tk.Label(right)
label.pack(expand=True)

root.mainloop()
