import tkinter as tk

def tuedad():
    eda = messagebox.get()  # obtener lo escrito en la caja

    if eda.isdigit():  # solo si es número
        edad = int(eda)
        if edad < 18:
            cosoquemuestraqueedades.config(text="Tu eres menor de edad")
        elif edad < 60:
            cosoquemuestraqueedades.config(text="Tu eres mayor de edad")
        else:
            cosoquemuestraqueedades.config(text="Viejo sabroso 😎")
    else:
        cosoquemuestraqueedades.config(text="Escribe una edad válida, sea serio")

ventana = tk.Tk() #Inboca ventana
ventana.title("K onda gente")
ventana.geometry("500x600")

messagebox = tk.Entry(ventana)
messagebox.pack(pady=10)

boton = tk.Button(ventana, text="Tu que xuxa eres", command=tuedad)
boton.pack(pady=10)

cosoquemuestraqueedades = tk.Label(ventana, text="Tu edad, caralo") #Texto que cambiara
cosoquemuestraqueedades.pack(pady=20)

ventana.mainloop()
