import tkinter as tk

def mostrar_seleccion():
    seleccion = lista.curselection()
    for i in seleccion:
        print("Seleccionaste:", lista.get(i))

ventana = tk.Tk()
ventana.title("Listbox en acción")
ventana.geometry("400x300")

# Creamos el Listbox
lista = tk.Listbox(ventana, selectmode=tk.MULTIPLE, height=6)
opciones = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go"]
for opcion in opciones:
    lista.insert(tk.END, opcion)
lista.pack()

# Botón para mostrar selección
boton = tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack()

ventana.mainloop()
