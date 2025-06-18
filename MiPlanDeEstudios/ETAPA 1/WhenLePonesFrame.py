import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo con Frames")
ventana.geometry("400x300")

# Frame 1 - Datos personales
frame_datos = tk.Frame(ventana, bg="lightblue", padx=10, pady=10)
frame_datos.pack(pady=10)

tk.Label(frame_datos, text="Nombre:").grid(row=0, column=0)
tk.Entry(frame_datos).grid(row=0, column=1)

tk.Label(frame_datos, text="Edad:").grid(row=1, column=0)
tk.Entry(frame_datos).grid(row=1, column=1)

# Frame 2 - Botones
frame_botones = tk.Frame(ventana, bg="lightgrey", padx=10, pady=10)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Guardar").pack(side="left", padx=5)
tk.Button(frame_botones, text="Cancelar").pack(side="left", padx=5)

otro_frame = tk.Frame(ventana, padx=20, pady=20, bg= "green")
otro_frame.pack()
boton = tk.Button(otro_frame, text="lol")
boton.pack()

ventana.mainloop()
