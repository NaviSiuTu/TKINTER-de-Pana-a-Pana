import tkinter as tk

def saludo():  #PONER ESE TEXT EN MINUSCULA
    etiqueta.config(text="uff como amo a Laura") #Si o si tenemos que definir una función para declarar lo que queremos hacer cuando se hace click

ventana = tk.Tk() #Forma de iniciar la ventana
ventana.title ("PRUEBA X") #Aqui le pones el titulo de la ventana
ventana.geometry("600x700") #Aquí le das las dimensiones a la ventana


etiqueta = tk.Label(ventana, text="Esto es un texto") #Funciona para crear textos en la GUI 
etiqueta.pack (pady=10)



boton = tk.Button(ventana, text= "K onda boludo", command = saludo)
boton.pack() #El pack es como un mainloop que nos permite dar a ver lo que se puso

ventana.mainloop() #Esto hace que la ventana se mantenga abierta todo el tiempo