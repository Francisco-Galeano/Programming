#alumnos = ["A", "B", "C"]

#print(alumnos)

#print(alumnos.pop(0))

#print(alumnos)

def es_par(numero):
	if numero % 2 == 0:
		return True
	else:
		return False
			
numero = int(input("Ingrese un número: "))
es_par(numero)
if es_par(numero) == True:
	print("Es par")
else:
	print("No es par")







	
