import tkinter as tk
 

ventana = tk.Tk()
ventana.title("Experimento random con canvas")
ventana.geometry("600x400")

canvas = tk.Canvas(ventana, width=300, height=300, bg="white")
canvas.pack(pady=20)


canvas.create_rectangle(50, 50, 200, 150, fill= "lightblue", outline="blue")
canvas.create_oval(100, 180, 200, 280, fill= "pink", outline="red")
canvas.create_line(0, 0, 300, 300, fill= "green", width=3)
canvas.create_text(150, 20, text="Hola canvas")

ventana.mainloop()