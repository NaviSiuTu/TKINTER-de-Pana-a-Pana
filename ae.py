import tkinter as tk
from PIL import Image, ImageTk  # pip install pillow

# Ventana principal
root = tk.Tk()
root.title("Login Retro")
root.geometry("400x500")
root.resizable(False, False)

# === Cargar imágenes ===
# Marco de fondo
marco_img = Image.open("Menu.png").resize((417, 497))
marco_tk = ImageTk.PhotoImage(marco_img)

# Logo
logo_img = Image.open("Menu (1).png").resize((130, 130))
logo_tk = ImageTk.PhotoImage(logo_img)

# === Canvas para fondo e imagen ===
canvas = tk.Canvas(root, width=400, height=500, highlightthickness=0)
canvas.pack()

# Imagen del marco
canvas.create_image(200, 250, image=marco_tk)

# Imagen del logo en la parte superior
canvas.create_image(200, 120, image=logo_tk)

# === Etiquetas para campos ===
label_user = tk.Label(root, text="NOMBRE", font=("Courier", 10, "bold"), bg="#00C000", fg="black")
label_pass = tk.Label(root, text="CONTRASEÑA", font=("Courier", 10, "bold"), bg="#00C000", fg="black")

label_user.place(x=100, y=180)
label_pass.place(x=100, y=230)

# === Entradas y botón ===
username_entry = tk.Entry(root, font=("Courier", 10), justify="center", bg="#00C000", fg="black")
password_entry = tk.Entry(root, font=("Courier", 10), show="*", justify="center", bg="#00C000", fg="black")
login_button = tk.Button(root, text="LOGIN", font=("Courier", 10, "bold"), bg="black", fg="white")

# === Posicionamiento preciso ===
username_entry.place(x=100, y=200, width=200, height=30)
password_entry.place(x=100, y=250, width=200, height=30)
login_button.place(x=150, y=310, width=100, height=35)

root.mainloop()

