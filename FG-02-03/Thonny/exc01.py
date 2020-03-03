def pedir_nombres(cantidad):
    
    lista_de_nombres = []
    
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del alumno: ")
        lista_de_nombres.append(nombre)
               
    return lista_de_nombres



def buscar_elemento(lista, elemento_a_buscar):
    
    
    for i in range(len(lista)):
        if lista[i] == elemento_a_buscar:
            return True
            break
        else:
            continue
        
    return False
        
    
            
        
            
        
    
    
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

tamaño_lista = int(input("Ingrese la longitud de la lista: "))
lista_nombres = pedir_nombres(tamaño_lista)
elemento = str(input("Ingrese el elemento a buscar: "))
buscar_elemento(lista_nombres, elemento)
if buscar_elemento(lista_nombres, elemento) == True:
    print("Existe")
else:
    print("No existe")



