import tkinter as tk
import pyqrcode
from PIL import Image, ImageTk
import io
from tkinter import messagebox

def generate_qr():
    data = url_entry.get().strip()   
    if data:
        try:
            qr = pyqrcode.create(data)
            qr_io = io.BytesIO()
            qr.png(qr_io, scale=6)
            qr_io.seek(0)  
            img = Image.open(qr_io)
            qr_img = ImageTk.PhotoImage(img)
            qr_label.config(image=qr_img)
            qr_label.image = qr_img
            
        except Exception as e:
            messagebox.showerror("Error : {e}")
    else:
        messagebox.showerror("Error", "Please enter a URL or text.")

root = tk.Tk()
root.title("QR Code Generator")

global url_entry
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=5)

global qr_label
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()