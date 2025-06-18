import tkinter as tk 

def MostrarSeleccion():
    seleccion = Juego_var.get()

    print (f"Omggg, que nota, tu juego favorito es: {seleccion}")

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("RadioButtons")

Lhobbie = tk.Label(ventana, text="Cual es tu juego favorito🐱‍🚀", font=("Arial", 15, "bold"))
Lhobbie.pack()

Juego_var = tk.StringVar()
Juego_var.set("COD 👏")


Rad1 = tk.Radiobutton(ventana, text="COD", variable=Juego_var, value ="COD")
Rad1.pack(anchor="w")
Rad2 = tk.Radiobutton(ventana, text="Fornite", variable=Juego_var, value ="Fornite")
Rad2.pack(anchor="w")
Rad3 = tk.Radiobutton(ventana, text="PvS", variable=Juego_var, value ="PvS")
Rad3.pack(anchor="w")
Rad4 = tk.Radiobutton(ventana, text="TombRaider", variable=Juego_var, value ="TombRaider")
Rad4.pack(anchor="w")

Mostrar = tk.Button(ventana, text="Mostrar Seleccion", command= MostrarSeleccion)
Mostrar.pack(anchor="w")

ventana.mainloop()