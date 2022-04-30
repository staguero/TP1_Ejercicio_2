def seleccion(costos,poblacion):
    ordenado_costos=sorted(costos, reverse=True)
    ordenado_poblacion=[]
    for i in ordenado_costos:
        posicion=costos.index(i)
        ordenado_poblacion.append(poblacion[posicion])
        
    #print(ordenado_costos)
    #print(ordenado_poblacion)

    long_poblacion=len(ordenado_poblacion)
    
    #Poblacion PAR
    if long_poblacion%2==0:
        bandera=int(long_poblacion/2)
        combinaciones=[]
        for j in range(2,bandera+1):
            combinaciones.append(1)
            combinaciones.append(j)
        combinaciones.append(2)
        combinaciones.append(3)
    else:
        pass

    #print(combinaciones)

    return ordenado_poblacion,combinaciones

#costos=   [6,7,8,9,10,11,12,25]
#poblacion=[1,2,3,4,5,6,7,8]

#seleccion(costos,poblacion)