def pedir_nombres(cantidad):
    
    lista_nombres = []
    
    for i in range(cantidad):
       nombres = input("Ingrese el nombre del alumno: ")
       lista_nombres.append(nombres)
               
    return lista_nombres

