if __name__ == "__main__":
    print("Lista de Supermercado")
    lista_sm={}

    #Convertir las lineas del documento en Keys
    archivo=open("supermercado.txt","r").read().split('\n')
    for linea in archivo:
        if linea in lista_sm.keys():
            lista_sm[linea]+=1
        else:
            lista_sm[linea]=1
    print(lista_sm)
    
    #Solicitar 3 articulos
    for i in range(3):
        articulo=input("Introduzca un Articulo a su lista del Super: ")
        if articulo in lista_sm.keys():
            lista_sm[articulo]+=1
        else:
            lista_sm[articulo]=1

    # Imprimir de manera ordenada
    print ("----------------------")
    print ("Lista Actual")
    print ("----------------------")
    for k,v in lista_sm.items():
        print(k,v)
    
    #Eliminar Articulo
    cont=input("\nDesea Eliminar un articulo? (y/n): ")
    while cont.lower()=="y":
        opc = input("\nIngrese el articulo a Eliminar : ")
        if opc in lista_sm.keys():
            lista_sm[opc]-=1
            print("Se Elimino un "+opc+".")
            if lista_sm[opc]==0:
                del lista_sm[opc]
                print("El articulo "+opc+" fue eliminado completamente")
            cont=input("\nDesea Eliminar otro articulo? (y/n): ")
        else:
            print("Articulo invalido, intente nuevamente")
    print
    for k,v in lista_sm.items():
        print(k,v)
    
    #Subtitucion de Articulo
    cont=input("\nDesea Substituir un articulo? (y/n): ")
    while cont.lower()=="y":
        opc = input("\nIngrese el articulo a Substituir : ")
        if opc in lista_sm.keys():
            print("Se Substituyo "+opc+".")
            del lista_sm[opc]
            cont="n"
        else:
            print("Articulo invalido, intente nuevamente")
    sub=input("Por que articulo substituira el "+opc+"?")
    if sub in lista_sm:
        lista_sm[sub]+=1
        print("+1 "+sub)
    else:
        lista_sm[sub]=1
        print("Nuevo Articulo Añadido")

    # Imprimir nuevamente de manera ordenada
    print ("----------------------")
    print ("Lista Actual")
    print ("----------------------")
    for k,v in lista_sm.items():
        print(k,v)
    
    archivo=open("supermercado.txt","a+")
    for e in lista_sm:
        archivo.write("\n"+e)
    archivo.close()