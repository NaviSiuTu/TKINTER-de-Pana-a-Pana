import tkinter as tk
from tkinter import messagebox, PhotoImage, Scrollbar, PanedWindow, Text, LabelFrame, Toplevel, Canvas, Menu

def enviar_formulario():
    nombre = entry_nombre.get()
    mensaje = text_mensaje.get("1.0", "end-1c")
    hobby_list = []
    if hobby1.get(): hobby_list.append("Leer")
    if hobby2.get(): hobby_list.append("Caminar")
    juego = juego_fav.get()
    edad = spinbox_edad.get()
    ciudad = ciudad_var.get()
    resumen = f"""--- RESUMEN DEL FORMULARIO ---
Nombre: {nombre}
Edad: {edad}
Ciudad: {ciudad}
Juego Favorito: {juego}
Hobbies: {', '.join(hobby_list)}
Mensaje: {mensaje}
"""
    messagebox.showinfo("Formulario", resumen)

def abrir_ventana_secundaria():
    nueva = Toplevel()
    nueva.title("Ventana secundaria")
    nueva.geometry("300x200")
    tk.Label(nueva, text="¡Hola desde Toplevel!").pack(pady=20)

def mostrar_bitmap():
    bitmap_window = Toplevel()
    bitmap_window.title("Bitmap Example")
    bitmap_window.geometry("200x200")
    tk.Label(bitmap_window, bitmap="info").pack(pady=40)

# Ventana principal
ventana = tk.Tk()
ventana.title("Widgets Combinados")
ventana.geometry("900x750")

# Menú
menu_principal = Menu(ventana)
submenu = Menu(menu_principal, tearoff=0)
submenu.add_command(label="Nueva Ventana", command=abrir_ventana_secundaria)
submenu.add_command(label="Mostrar Bitmap", command=mostrar_bitmap)
menu_principal.add_cascade(label="Opciones", menu=submenu)
ventana.config(menu=menu_principal)

# Canvas
canvas = Canvas(ventana, width=300, height=100, bg="lightgrey")
canvas.create_text(150, 50, text="Canvas: Aquí puedes dibujar", font=("Arial", 12))
canvas.pack(pady=10)

# PanedWindow
paned = PanedWindow(ventana, orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=True)

# Frame izquierdo
frame_izq = tk.Frame(paned, bg="lightblue")
paned.add(frame_izq)

try:
    imagen = PhotoImage(file="avatar.png")  # Asegúrate de tener este archivo
    img_label = tk.Label(frame_izq, image=imagen)
    img_label.pack(pady=10)
except:
    tk.Label(frame_izq, text="[Imagen aquí]", bg="lightblue").pack(pady=10)

tk.Label(frame_izq, text="Nombre:", bg="lightblue").pack()
entry_nombre = tk.Entry(frame_izq)
entry_nombre.pack()

# Frame derecho
frame_der = tk.Frame(paned, padx=10, pady=10)
paned.add(frame_der)

tk.Label(frame_der, text="Edad:").grid(row=0, column=0, sticky="w")
spinbox_edad = tk.Spinbox(frame_der, from_=10, to=99)
spinbox_edad.grid(row=0, column=1, sticky="w")

tk.Label(frame_der, text="Ciudad:").grid(row=1, column=0, sticky="w")
ciudad_var = tk.StringVar(value="Selecciona")
tk.OptionMenu(frame_der, ciudad_var, "Bogotá", "Cali", "Huila").grid(row=1, column=1, sticky="w")

tk.Label(frame_der, text="Juego favorito:").grid(row=2, column=0, sticky="w")
juego_fav = tk.StringVar(value="PvS")
tk.Radiobutton(frame_der, text="PvS", variable=juego_fav, value="PvS").grid(row=2, column=1)
tk.Radiobutton(frame_der, text="Fornite", variable=juego_fav, value="Fornite").grid(row=2, column=2)

tk.Label(frame_der, text="Hobbies:").grid(row=3, column=0, sticky="w")
hobby1 = tk.BooleanVar()
hobby2 = tk.BooleanVar()
tk.Checkbutton(frame_der, text="Leer", variable=hobby1).grid(row=3, column=1, sticky="w")
tk.Checkbutton(frame_der, text="Caminar", variable=hobby2).grid(row=3, column=2, sticky="w")

# LabelFrame con Scrollbar
msg_frame = LabelFrame(frame_der, text="Mensaje")
msg_frame.grid(row=4, column=0, columnspan=3, pady=10, sticky="we")
text_mensaje = Text(msg_frame, height=5, width=40, wrap="word")
text_mensaje.pack(side="left", fill="both", expand=True)
scroll = Scrollbar(msg_frame, command=text_mensaje.yview)
scroll.pack(side="right", fill="y")
text_mensaje.config(yscrollcommand=scroll.set)

tk.Button(frame_der, text="Enviar", command=enviar_formulario).grid(row=5, column=0, columnspan=3, pady=10)

ventana.mainloop()
