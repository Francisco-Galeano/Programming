import tkinter as tk

ventana = tk.Tk()
ventana.config(width = 500, height = 500)
ventana.title("Puede votar?")

etiqueta_1 = tk.Label(bg = "red", fg = "black")
etiqueta_1.place(x = 50, y = 100, width = 400, height = 50)

boton_1 = tk.Button(text = "Ha ingresado la edad? Entonces CLICK AQUI!") # no olvidar el "command"
boton_1.place(x = 50, y = 150, width = 400, height = 50)

etiqueta_2 = tk.Label(text = "Ingrese en la siguiente caja la edad", bg = "red", fg = "black")
etiqueta_2.place(x = 50, y = 200, width = 400, height = 50)

caja_1 = tk.














ventana.mainloop()
