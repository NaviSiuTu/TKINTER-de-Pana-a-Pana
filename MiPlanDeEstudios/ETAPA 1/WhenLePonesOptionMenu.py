import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ejemplo OptionMenu")
ventana.geometry("400x200")

# Variable para guardar la selección
opcion = tk.StringVar()
opcion.set("Python")  # Valor por defecto

# Lista de opciones
opciones = ["Python", "JavaScript", "Java", "C++", "Go"]

# Crear el OptionMenu
menu = tk.OptionMenu(ventana, opcion, *opciones)
menu.pack(pady=20)

# Función al dar clic
def mostrar():
    seleccion = opcion.get()
    tk.messagebox.showinfo("Lenguaje seleccionado", f"Elegiste: {seleccion}")

# Botón para mostrar lo elegido
boton = tk.Button(ventana, text="Mostrar selección", command=mostrar)
boton.pack()

ventana.mainloop()
