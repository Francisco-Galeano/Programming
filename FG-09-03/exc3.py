def devolver_mayor(numero_1, numero_2):
	if numero_1 > numero_2:
		return numero_1
	else:
		return numero_2

numero_1 = int(input("Ingrese el 1er numero: "))
numero_2 = int(input("Ingrese el 2do numero: "))

print(devolver_mayor(numero_1, numero_2))


def pueder_votar(edad):
	if edad >= 16:
		return True
	else:
		return False
		
edad = int(input("Ingrese la edad: "))
if pueder_votar(edad) == True:
	print("Puede votar")
else:
	print("No puede votar")
	
otro_numero = input("Flotante: ")
print(otro_numero)
suma = otro_numero + otro_numero # cómo no le meti el float al input en línea 25 el print de abajo me va a concatenar el str del input de la línea 25
print(suma)


