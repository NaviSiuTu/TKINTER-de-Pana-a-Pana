import tkinter as tk

def mostrar_edad():
    edad = spin.get()
    print(f"Tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Spinbox Example")
ventana.geometry("300x200")

Ledad = tk.Label(ventana, text="Selecciona tu edad:")
Ledad.pack()

spin = tk.Spinbox(ventana, from_=0, to=100)
spin.pack()

boton = tk.Button(ventana, text="Mostrar Edad", command=mostrar_edad)
boton.pack()

spin_dias = tk.Spinbox(ventana, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
spin_dias.pack()

ventana.mainloop()
