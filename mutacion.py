import random

def mutacion(lista):
    flag=1
    while flag==1:
        posicion_1=random.randint(0,len(lista))
        posicion_2=random.randint(0,len(lista))
        if posicion_1==posicion_2:
            posicion_2=random.randint(0,len(lista))
        else:
            flag=2

    valor_posicion_1=lista[posicion_1]
    valor_posicion_2=lista[posicion_2]

    lista[posicion_1]=valor_posicion_2
    lista[posicion_2]=valor_posicion_1

    return lista

#listaA=[20,7,19,2,17,9,23,21,14,30,1,32,22,8,27,10,15,16,4,28,12,31,29,3,11,25,13,26,5,18,24,6]
#print(listaA)
#lista_nueva=mutacion(listaA)
#print(lista_nueva)