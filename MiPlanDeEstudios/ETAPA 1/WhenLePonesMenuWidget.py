import tkinter as tk
from tkinter import messagebox

# Funciones de ejemplo
def nueva_ventana():
    messagebox.showinfo("Nueva ventana", "Has creado un nuevo archivo.")

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Menús en Tkinter")
ventana.geometry("400x300")

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)  # asociamos la barra con la ventana

# Crear el menú 'Archivo'
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Opciones dentro de 'Archivo'
menu_archivo.add_command(label="Nuevo", command=nueva_ventana)
menu_archivo.add_separator()  # Línea divisora
menu_archivo.add_command(label="Salir", command=salir)

ventana.mainloop()
