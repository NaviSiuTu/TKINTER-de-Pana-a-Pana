import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def ClickTo():
    name = CuadroDeMensaje.get()
    print(f"Hola, {name}!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("VentanaConEstructura")
ventana.geometry("600x400")

#---- TEXTO PRINCIPAL CENTRADO Y ARRIBA ------ TITULOS
LabelFuncional = tk.Label(ventana, text= "Prueba de Cosas chistosas" , font=("Arial", 16))
LabelFuncional.pack()



CuadroDeMensaje = tk.Entry (ventana)
CuadroDeMensaje.pack()





#---- BOTON QUE INTERACTUA CON CONSOLA -----
Boton = tk.Button(ventana, text="ClickBro", font= ("TimesNewRoman", 12), command=ClickTo)
Boton.pack()


ventana.mainloop()