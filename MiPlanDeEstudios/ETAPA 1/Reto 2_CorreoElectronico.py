import tkinter as tk 

def enviarcorreo():
    Nombre = Enombre.get()
    Correo = Ecorreo.get()
    Cuerpo = Comentario.get("1.0", "end-1c")

    print (f"Buenas tardes!, vas a enviar un correo\n\nCorreo: {Correo}\nNombre: {Nombre}\nMensaje: {Cuerpo}")


ventana = tk.Tk()
ventana.geometry("600x500")
ventana.title("Prueba de Correo Electrónico")

Lnombre = tk.Label(ventana, text="Cual es el nombre del destinatario?", font=("Arial", 15, "bold"))
Lnombre.pack()

Enombre= tk.Entry (ventana)
Enombre.pack()

Lcorreo = tk.Label(ventana, text="Cuál es el correo electrónico de destino?", font=("Arial", 15, "bold"))
Lcorreo.pack()

Ecorreo = tk.Entry(ventana)
Ecorreo.pack()

Lcuerpo = tk.Label(ventana, text="Escribe tu mensaje", font=("Arial", 15, "bold"))
Lcuerpo.pack()

Comentario = tk.Text(ventana, height= 10, width= 50, font=("Arial", 11))
Comentario.pack()

Enviar = tk.Button(ventana, text="Enviar Correo", command=enviarcorreo)
Enviar.pack()

ventana.mainloop()