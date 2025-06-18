import tkinter as tk

def CalularSaludo():
    Nombre = Ename.get()
    Cuentame = Tcuentame.get("1.0", "end")
    print(f"Hola {Nombre}, que interesante tu historia, está para un libro, Y es\n\n{Cuentame} ")
ventana = tk.Tk()
ventana.title("Prueba con TextWidget")
ventana.geometry("600x400")

Lname = tk.Label(ventana, text="¿Cómo te llamas?")
Lname.pack()

Ename = tk.Entry(ventana)
Ename.pack()

LInfo = tk.Label(ventana, text="Cuentanos algo sobre ti")
LInfo.pack()

Tcuentame = tk.Text(ventana, height=10, width=10, font=("Arial",11))
Tcuentame.pack()

Button = tk.Button(ventana, text="Calcular Saludo", command=CalularSaludo )
Button.pack()

ventana.mainloop()