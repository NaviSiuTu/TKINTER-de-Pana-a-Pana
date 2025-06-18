import tkinter as tk

ventana = tk.Tk()
ventana.title("Mensaje largo")
ventana.geometry("400x300")

mensaje_largo = """Bienvenido a esta aplicación.
Este es un mensaje de texto largo que se ajusta automáticamente al ancho de la ventana sin que tengas que hacer nada."""

msg = tk.Message(ventana, text=mensaje_largo, width=300, font=("Arial", 12))
msg.pack(pady=20)

ventana.mainloop()
