import tkinter as tk

ventana = tk.Tk()
ventana.title("Imagen en Label")
ventana.geometry("400x400")

# Cargar imagen .png
imagen = tk.PhotoImage(file="ejemplo.png")  # Debe estar en la misma carpeta

# Crear un label con la imagen
label_img = tk.Label(ventana, image=imagen)
label_img.pack()

ventana.mainloop()
