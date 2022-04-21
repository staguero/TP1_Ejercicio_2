import numpy as np
from Node import *
from A_Star import *
from Simulated_Annealing import *
import os

def dibujo():
        for i in range(mapa_filas):
            print(mapa_dibujo[i])

if __name__ == "__main__":

    # >>>>>> CREACIÓN DE MAPA <<<<<<
    #Solicitud de datos
    columnas_estante=int(input('Cantidad de columnas por estantería: '))
    estantes_f=int(input('Cantidad de Filas de estantería: '))
    estantes_c=int(input('Cantidad de Columnas de estantería: '))
    #Elaboración de matriz "MAPA"
    mapa_filas = 2*estantes_f+4+(estantes_f-1)*2
    mapa_columnas= estantes_c*columnas_estante+4+(estantes_c-1)*2
    mapa_dimensiones= [mapa_filas,mapa_columnas]
    mapa=[]
    mapa = [[Node(i,j,None) for j in range(mapa_columnas)] for i in range(mapa_filas)]
    for j in range(mapa_columnas):
        for i in range(mapa_filas):
            mapa[i][j].setID("Empty")

    #Asignacion de estantes y su nombre
    fin_columnas=mapa_columnas-(2+columnas_estante)
    m=np.linspace(2,fin_columnas,estantes_c)
    print(estantes_c)
    fin_filas=mapa_filas-(2+2)
    m2=np.linspace(2,fin_filas,estantes_f)
    print(">>>>>>>>> Columna Comienzo Estantería <<<<<<<<<")
    print(m)
    print(">>>>>>>>> Fila  Comienzo Estantería <<<<<<<<<")
    print(m2)
    valor=1
    for j in m:
        for i in m2:
            col=int(j)
            for k in range(columnas_estante): 
                mapa[int(i)][col].setID( "Shelf" + str(valor) )
                mapa[int(i)+1][col].setID("Shelf" + str(valor+columnas_estante ) )
                col+=1
                valor+=1
            valor+=columnas_estante
    
    #Dibujo del mapa
    mapa_dibujo=[]
    mapa_dibujo = [[0 for j in range(mapa_columnas)] for i in range(mapa_filas)]
    print(">>>>>>>>> AREA DE TRABAJO <<<<<<<<<")
    for j in range(mapa_columnas):
        for i in range(mapa_filas):
            if mapa[i][j].id == "Empty":
                mapa_dibujo[i][j]="0 "
            else:
                mapa_dibujo[i][j]=mapa[i][j].id[5:]
    dibujo()
    stops = input("Escriba las paradas separadas por un espacio, ej:2 4 7\n")
    i=0
    stops_list = stops.split(" ")
    stops_list = list(set(stops_list))
    print(stops_list)
    #LISTA DE COSTOS
    cost_list = []
    count=0
    while count <= len(stops_list):
        for value in range(count+1,len(stops_list)):
            inicio=str(stops_list[count])
            fin=str(stops_list[value])
            for j in range(mapa_columnas):
                for i in range(mapa_filas):
                    if mapa[i][j].id is not None:
                        if mapa[i][j].id[5:]==inicio:
                            current_node = mapa[i][j]
                        if mapa[i][j].id[5:]==fin:
                            target_node = mapa[i][j]

            a_star = A_Star(mapa,current_node,target_node)
            a_star.start_method(mapa_columnas,mapa_filas)

            cost_list.append([inicio,fin,a_star.path_cost])
        count = count + 1

    simulated_annealing = SimulatedAnnealing(stops_list,cost_list,10000) # EL 100 ES LA TEMPERATURA INICIAL (NUMERO DE ITERACIONES BASICAMENTE)
    lowcost_path=simulated_annealing.start()
    os.system('cls')
    dibujo()
    print("El mejor camino encontrado es:")
    print(lowcost_path[0])
    print("Y el costo del recorrido es: %f " %(lowcost_path[1]))
    input()

    