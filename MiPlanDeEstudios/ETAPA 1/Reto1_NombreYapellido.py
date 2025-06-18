import tkinter as tk
from tkinter import messagebox
def Saludo():
    SNombre = Nombre.get()
    SApellido = Apellido.get()
    print(f"Hola {SNombre} {SApellido}!, ¿Cómo estás?")
    messagebox.showinfo(f"Hola {SNombre} {SApellido}!, ¿Cómo estás?")

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Reto 1")

Tname = tk.Label(ventana, text = "Cual es tu nombre?", font=("Arial", 14))
Tname.pack()

Nombre = tk.Entry(ventana)
Nombre.pack()

Tapellido = tk.Label(ventana, text= "Cual es tu apellido?", font=("Arial", 14))
Tapellido.pack()

Apellido = tk.Entry(ventana)
Apellido.pack()

BotonSaludo = tk.Button(ventana, text="Saludo", command=Saludo)
BotonSaludo.pack()

ventana.mainloop()