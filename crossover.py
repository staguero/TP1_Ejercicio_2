def crossover(padre_1,padre_2):
    cantidad_casilleros=len(padre_1)
    corte_1=cantidad_casilleros//3
    corte_2=corte_1*2
    #print(corte_1)
    #print(corte_2)
    #print(padre_1[corte_1],padre_1[corte_2])
    #print(padre_2[corte_1],padre_2[corte_2])
    
    hijo_1=[0]*cantidad_casilleros
    hijo_2=[0]*cantidad_casilleros

    #Creacion hijos
    for i in range(corte_1,corte_2+1):
        hijo_1[i]=padre_2[i]
        hijo_2[i]=padre_1[i]
    #print(hijo_1)
    #print(hijo_2)

    hijo_1=generacion(padre_1,hijo_1,corte_1,corte_2,cantidad_casilleros)
    hijo_2=generacion(padre_2,hijo_2,corte_1,corte_2,cantidad_casilleros)
    

    return hijo_1,hijo_2

def generacion(padre,hijo,corte_1,corte_2,cantidad_casilleros):
    #1er recorrido: punto de corte hasta el final 
    contador_1=0
    for j in range(corte_2+1,cantidad_casilleros): 
        if padre[j] not in hijo[corte_1:corte_2+1]:
            hijo[j-contador_1]=padre[j]
            ultima_posicion=j-contador_1
        else:
            contador_1+=1
    #2do Recorrido: desde el punto inicial hasta el corte 2
    posicion_partida=ultima_posicion+1        
    cantidad=cantidad_casilleros-posicion_partida #es la cantidad de posiciones que me queda para llegar al final
    contador_2=0
    #print("Llgue hasta: ",ultima_posicion)
    #print(hijo)
    #print("faltan para llegar: ",cantidad)
    #print("voy a ir hasta: ",corte_2+cantidad)
    for t in range(0,corte_2+cantidad):
        if padre[t] not in hijo[corte_1:corte_2+1]:
            if posicion_partida <= cantidad_casilleros-1:
                hijo[posicion_partida]=padre[t]
                posicion_partida+=1
            else:
                hijo[t-cantidad-contador_2]=padre[t]
        else:
            contador_2+=1
    
    return hijo


#listaA=[20,7,19,2,17,9,23,21,14,30,1,32,22,8,27,10,15,16,4,28,12,31,29,3,11,25,13,26,5,18,24,6]
#listaB=[1,19,10,9,8,2,7,20,16,21,15,3,29,11,22,32,4,30,23,31,5,24,17,25,12,28,6,13,26,14,18,27]

#print(listaA)
#print(listaB)

#hijo1,hijo2=crossover(listaA,listaB)
#print(hijo1)
#print(len(hijo1))
#print(hijo2)
#print(len(hijo2))