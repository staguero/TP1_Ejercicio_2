import random

def crear_poblacion(cantidad_individuos,cantidad_casilleros):
    poblacion=[]
    valor=1
    
    for j in range(0,cantidad_individuos):
        individuo=[0]*cantidad_casilleros
        for i in range(0,cantidad_casilleros):
            posicion=random.randint(0,cantidad_casilleros-1)
            if individuo[posicion]==0:
                individuo[posicion]=valor
                valor+=1
            
            else:
                posicion_alternativa=individuo.index(0)
                individuo[posicion_alternativa]=valor
                valor+=1
        poblacion.append(individuo)
        valor=1
    
    return poblacion

#print(crear_poblacion(10,32))