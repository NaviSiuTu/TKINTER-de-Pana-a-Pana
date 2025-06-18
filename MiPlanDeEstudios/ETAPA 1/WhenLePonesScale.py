import tkinter as tk

def Energiaja():
    energia = NivelDeEnergia.get()
    nombre = Enombre.get()
    Resultado.config(text=f"Holaaa {nombre}, tu nivel de energía es {energia}")

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Energia Mental")

Lnombre = tk.Label(ventana, text="Como se llama tu nombre?", font=("Arial", 15, "bold"))
Lnombre.pack()

Enombre = tk.Entry(ventana)
Enombre.pack()

Lenergia= tk.Label(ventana, text="Cuál es tu nivel de energía?", font=("Arial", 13, "bold"))
Lenergia.pack()

NivelDeEnergia = tk.Scale(ventana, from_=0, to_=10, orient= "horizontal", font=("Arial", 12))
NivelDeEnergia.pack()

Boton = tk.Button(ventana, text="Energía", command=Energiaja)
Boton.pack()

Resultado = tk.Label(ventana, text="", font=("TimesNewRoman", 15, "bold"))
Resultado.pack()
ventana.mainloop()

