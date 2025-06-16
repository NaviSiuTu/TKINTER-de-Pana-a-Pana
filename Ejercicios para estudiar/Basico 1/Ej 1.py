import tkinter as tk

def cambiarname():
    nombre = ponername.get()  # ⬅️ Sacar lo que el usuario escribió
    etiqueta.config(text=f"Hola, {nombre}")  # ⬅️ Cambiar el texto de la etiqueta

ventana = tk.Tk()  # ⬅️ Crea la ventana
ventana.title("Cambio de Name")  # ⬅️ Título de la ventana
ventana.geometry("300x200")  # ⬅️ Tamaño de la ventana

ponername = tk.Entry(ventana)  # ⬅️ Caja para escribir texto
ponername.pack(pady=10)  # ⬅️ Mostrar la caja con espacio

boton = tk.Button(ventana, text="Tu name", command=cambiarname)  # ⬅️ Botón
boton.pack(pady=10)  # ⬅️ Mostrar el botón con espacio

etiqueta = tk.Label(ventana, text="Saludiño caralo")
etiqueta.pack()

ventana.mainloop()  # ⬅️ Mostrar todo y mantener la ventana abierta


