import tkinter as tk
import json

def registrarse ():
    Nombre = Nnombre.get()
    Contraseña = Ncontraseña.get()

    datos ={
        "Usuario": Nombre,
        "Contraseña": Contraseña
    }

    with open("datos_usuario.json", "w") as archivo:
        json.dump(datos, archivo)
        
    resultado.config(text=f"Credenciales guardadas!, bienvenido {Nombre}")

ventana = tk.Tk()
ventana.title("Con persistencia de datos")
ventana.geometry("600x400")

Lnombre = tk.Label(ventana, text="Nombre de Usuario", font=("Arial", 15, "bold"))
Lnombre.pack()

Nnombre = tk.Entry (ventana)
Nnombre.pack()

Lcontraseña = tk.Label(ventana, text="Contraseña", font=("Arial", 15, "bold"))
Lcontraseña.pack()

Ncontraseña = tk.Entry(ventana, show="*")
Ncontraseña.pack()

boton = tk.Button(ventana, text="Iniciar Sesión", command=registrarse )
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()
ventana.mainloop()