import tkinter as tk

ventana = tk.Tk()
ventana.title("Todos los íconos Bitmap")
ventana.geometry("500x400")

iconos = [
    "error", "info", "question", "warning", "hourglass",
    "gray12", "gray25", "gray50", "gray75"
]

tk.Label(ventana, text="Íconos Bitmap disponibles:", font=("Arial", 14, "bold")).pack(pady=10)

contenedor = tk.Frame(ventana)
contenedor.pack()

for i, icono in enumerate(iconos):
    frame = tk.Frame(contenedor, padx=10, pady=5)
    frame.grid(row=i // 3, column=i % 3)

    label_icono = tk.Label(frame, bitmap=icono)
    label_icono.pack()
    
    label_nombre = tk.Label(frame, text=icono)
    label_nombre.pack()

ventana.mainloop()
