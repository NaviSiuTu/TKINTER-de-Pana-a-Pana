import tkinter as tk
import json
import os


archivo = "usuarios.json"

if not os.path.exists(archivo):
    with open (archivo,"w") as f:
        json.dump([], f)
#___________________ FUNCIONES ________________

def registrar_usuario():
    nombre = Enombre.get()
    edad = Eedad.get()

    if nombre == "" or edad == "":
        mensaje.config(text="Por favor completa todos los campos")
        return
    
    try:
        edad = int(edad)
    except ValueError:
        mensaje.config(text="Edad debe ser un número.")
        return
    
    nuevo_usuario = {"nombre": nombre, "edad": edad}
    
    with open(archivo, "r") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            datos = []

    if not isinstance(datos, list):
        datos = [datos]
    
    datos.append(nuevo_usuario)

    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

    mensaje.config(text=f"Usuario {nombre} registrado con exito.")

    Enombre.delete (0, "end")
    Eedad.delete(0,"end")

#INTERFAZ

ventana = tk.Tk()
ventana.title("RegisterDeUsuario")
ventana.geometry("600x400")

titulo = tk.Label(ventana, text="Registro de Usuario", font=("Arial", 16, "bold"))
titulo.pack()

Lnombre = tk.Label(ventana, text="Nombre:")
Lnombre.pack()

Enombre = tk.Entry(ventana)
Enombre.pack()

Ledad = tk.Label(ventana, text="Edad:")
Ledad.pack()

Eedad = tk.Entry(ventana)
Eedad.pack()

boton_registrase = tk.Button(ventana, text="Registrarse", command= registrar_usuario)
boton_registrase.pack()

mensaje = tk.Label(ventana, text="", fg="green")
mensaje.pack()


ventana.mainloop()