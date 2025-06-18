import tkinter as tk

ventana = tk.Tk()
ventana.title("LabelFrame Example")
ventana.geometry("400x300")

# Creamos el marco con título
marco = tk.LabelFrame(ventana, text="Datos del Usuario", padx=10, pady=10)
marco.pack(padx=20, pady=20)

# Agregamos widgets dentro del marco
label_nombre = tk.Label(marco, text="Nombre:")
label_nombre.pack()

entry_nombre = tk.Entry(marco)
entry_nombre.pack()

label_edad = tk.Label(marco, text="Edad:")
label_edad.pack()

entry_edad = tk.Entry(marco)
entry_edad.pack()

ventana.mainloop()
