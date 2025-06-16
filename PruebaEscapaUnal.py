import tkinter as tk

def iniciar_juego():
    # Esto es solo una simulación de empezar el juego
    instrucciones.delete("1.0", tk.END)
    instrucciones.insert(tk.END, "¡El juego ha comenzado!\n(Aquí cargarías tu juego real en Canvas o similar)")

root = tk.Tk()
root.title("Escapa de la UNAL - Inicio")
root.geometry("500x300")

# Frame para organizar el contenido
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Texto con instrucciones
instrucciones = tk.Text(frame, height=10, width=60, wrap=tk.WORD, font=("Arial", 12))
instrucciones.pack(pady=10)

texto_inicial = (
    "🕹️ Bienvenido a Escapa de la Unal 🕹️\n\n"
    "Usa las flechas del teclado para moverte.\n"
    "Recoge las monedas y evita las trampas.\n"
    "Supera todos los niveles y conviértete en el rey del laberinto.\n\n"
    "¡Buena suerte!"
)

instrucciones.insert(tk.END, texto_inicial)
instrucciones.config(state=tk.DISABLED)  # Para que no se edite

# Botón para comenzar el juego
boton_jugar = tk.Button(frame, 
                        text="Iniciar juego", 
                        font=("Arial", 12, "bold"), 
                        bg="lime", 
                        command=iniciar_juego)
boton_jugar.pack(pady=10)

root.mainloop()
