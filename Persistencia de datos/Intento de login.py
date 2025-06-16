import tkinter as tk 
import json

def log():
    Usuario = user.get()
    Contraseña = contr.get()
    with open("usuarios.json", "r") as archivo:
        us = json.load(archivo)
    if Usuario == us and Contraseña == us:
        confirmado= tk .Label("Sesion Iniciada")
        confirmado.pack()
    else:
        confirmado = tk.Label("Pailas, credenciales malas")
        confirmado.pack()

ventana = tk.Tk()
ventana.title("Login chistoso")
ventana.geometry("500x600")
ventana.config(bg="#615966")


user_et= tk.Label(ventana, text="User", bg="#615966")
user_et.pack()

user = tk.Entry(ventana, bg="#615966")
user.pack()

contr_et = tk.Label(ventana, text="Password", bg="#615966")
contr_et.pack()

contr = tk.Entry(ventana, bg="#615966")
contr.pack()

boton= tk.Button(ventana, text="Login", bg="#615966", command = log)
boton.pack()

ventana.mainloop()