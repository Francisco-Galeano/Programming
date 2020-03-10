import tkinter as tk

def saludar():
	nombre = caja1.get()
	# print("We are orcs from", nombre)
	etiqueta1.config(text="We are orcs from " + nombre)
	


ventana = tk.Tk() # crear ventana
ventana.config(width=600, height=350) # determino alto y ancho de la ventana




# caja de texto, equivalente al imput




etiqueta1 = tk.Label(bg="red", fg="black") # crea una etiqueta. la etiqueta es el equivalente al print
etiqueta1.place(x=30, y=50, width=150, height=25) # establezco donde quiero que la etiqueta se muestre. paso hasta 4 coordenadas. X e Y obligación(o sino se centra)





boton1 = tk.Button(text="The home of Sauron", command=saludar)  # creo un botón
boton1.place(x=30, y=80, width=150) # establezco donde quiero que el botón se muestre. paso hasta 4 coordenadas




caja1 = tk.Entry() # creo una caja de texto
caja1.place(x=30, y=110, width=125, height=35) # establezco donde quiero que la caja se muestre. paso hasta 4 coordenadas









ventana.mainloop() # mostrarla en pantalla. esto va siempre al final

