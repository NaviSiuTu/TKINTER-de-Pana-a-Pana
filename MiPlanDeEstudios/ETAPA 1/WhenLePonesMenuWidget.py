import tkinter as tk
from tkinter import messagebox

def salir():
    ventana.quit()

def mostrar_info():
    messagebox.showinfo("Acerca de", "Esta es una app creada con Tkinter 😎")

ventana = tk.Tk()
ventana.title("Menú en Tkinter")
ventana.geometry("400x300")

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=salir)

# Menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_info)

ventana.mainloop()