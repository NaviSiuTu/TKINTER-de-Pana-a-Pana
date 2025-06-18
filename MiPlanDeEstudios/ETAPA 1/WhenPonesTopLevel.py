import tkinter as tk

def ventanita ():
    nuevaventana = tk.Toplevel()
    nuevaventana.title ("OMG")
    nuevaventana.geometry("300x100")
    ventana.quit

    mensaje = tk.Label(nuevaventana, text="NOSEQUEPONEJAJAJAEKISDE")
    mensaje.pack()

    cerrar = tk.Button(nuevaventana, text="Cerrar", command=nuevaventana.destroy)
    cerrar.pack()


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("PruebaDeTopLevel")

boton = tk.Button(ventana, text="Abrir TopLevel", command=ventanita)
boton.pack()

ventana.mainloop()