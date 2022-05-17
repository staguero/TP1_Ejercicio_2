def lector_ordenes(longitud_de_orden):
    archivo=open('ordenes.txt',"r")
    lista_archivo=archivo.readlines()

    lista_momentanea=[]
    lista_final=[]
    contador=0 #lo uso para saber cuantas ordenes hay

    for linea in lista_archivo:
        if "Order" in linea:
            posicion=lista_archivo.index(linea)
            contador+=1
            for i in range(posicion+1,posicion+longitud_de_orden+1):
                lista_momentanea.append(lista_archivo[i])

    for i in range(0,len(lista_momentanea),longitud_de_orden):
        lista_final.append(lista_momentanea[i:i+longitud_de_orden])   
    
    #Borrado de caracteres
    caracteres="P \n"
    for mapa in lista_final:
        for i in range(0,longitud_de_orden):
            for x in range(len(caracteres)):
                mapa[i]=mapa[i].replace(caracteres[x],"")

    return lista_final
