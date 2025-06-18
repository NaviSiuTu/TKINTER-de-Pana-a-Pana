import tkinter as tk

def mostrar_registro():
    frame_login.pack_forget()  # oculta el login
    frame_registro.pack(fill="both", expand=True)  # muestra el registro

def mostrar_login():
    frame_registro.pack_forget()
    frame_login.pack(fill="both", expand=True)

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Cambio de pantalla con Frames")

# Frame para login
frame_login = tk.Frame(ventana)
frame_login.pack(fill="both", expand=True)

titulo = tk.Label(frame_login, text="Bienvenido", font=("Arial", 20))
titulo.pack(pady=10)

btn_ir_a_registro = tk.Button(frame_login, text="Registrarse", command=mostrar_registro)
btn_ir_a_registro.pack(pady=10)

# Frame para registro
frame_registro = tk.Frame(ventana)

lbl_nombre = tk.Label(frame_registro, text="Nombre:")
lbl_nombre.pack()
entry_nombre = tk.Entry(frame_registro)
entry_nombre.pack()

btn_volver = tk.Button(frame_registro, text="Volver al Login", command=mostrar_login)
btn_volver.pack(pady=10)

ventana.mainloop()
