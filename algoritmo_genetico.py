#Algoritmos a utilizar
from Node import *
from A_Star import *
from Simulated_Annealing import *

#Funciones creadas para el método
from lector_ordenes import *
from crear_poblacion import *
from crear_mapa import *
from seleccion import *
from crossover import *
from mutacion import *

class algoritmo_genetico():
    def __init__(self,columnas_estante,estantes_f,estantes_c,cantidad_individuos,long_ordenes):
        self.columnas_estante=columnas_estante
        self.estantes_f=estantes_f
        self.estantes_c=estantes_c
        self.cantidad_individuos=cantidad_individuos
        self.long_ordenes=long_ordenes

        self.mapa_filas=0
        self.mapa_columnas=0
        self.cantidad_casilleros=0

        self.poblacion=[]
        self.ordenes=[]
        self.mapa=[]
        self.fitness=[]
        self.seleccion=[]

    def iniciar_metodo(self):
        self.mapa_filas=2*self.estantes_f+4+(self.estantes_f-1)*2
        self.mapa_columnas=self.estantes_c*self.columnas_estante+4+(self.estantes_c-1)*2
        self.cantidad_casilleros=(self.columnas_estante*2)*(self.estantes_f*self.estantes_c)
        
        #Crear Poblacion
        self.poblacion=crear_poblacion(self.cantidad_individuos,self.cantidad_casilleros)
        
        #Lectura de ordenes
        self.ordenes=lector_ordenes(self.long_ordenes) #[[4,5,6,7],[6,5,4,7],[4,7,6,5]]
                
        for iteraciones in range(10): #es el método de parada que se me ocurrio
            for i in range(len(self.poblacion)): 
                #Crear el mapa
                self.mapa=crear_mapa(self.columnas_estante,self.estantes_f,self.estantes_c,self.poblacion[i])
                
                #Calculo de Fitness
                for orden in self.ordenes:
                    stops_list=orden
                    cost_list = []
                    count=0
                    while count <= len(stops_list):
                        for value in range(count+1,len(stops_list)):
                            inicio=str(stops_list[count])
                            fin=str(stops_list[value])
                            for j in range(self.mapa_columnas):
                                for i in range(self.mapa_filas):
                                    if self.mapa[i][j].id is not None:
                                        if self.mapa[i][j].id[5:]==inicio:
                                            current_node = self.mapa[i][j]
                                        if self.mapa[i][j].id[5:]==fin:
                                            target_node = self.mapa[i][j]

                            a_star = A_Star(self.mapa,current_node,target_node)
                            a_star.start_method(self.mapa_columnas,self.mapa_filas)

                            cost_list.append([inicio,fin,a_star.path_cost])
                        count = count + 1

                    simulated_annealing = SimulatedAnnealing(stops_list,cost_list,10000) # EL 100 ES LA TEMPERATURA INICIAL (NUMERO DE ITERACIONES BASICAMENTE)
                    lowcost_path=simulated_annealing.start()
                    print("El camino mas optimo es:")
                    print(lowcost_path)

                    #Acá tendría que calcular el costo de ese camino óptimo
                    #acá tendría que sumarlo con el costo de la orden anterior
                
                #acá tendría que calcular el fitness (promedio de los costos de ese mapa)
                #acá tendría que guardarlo en la lista de fitness generales de los mapas

            #Selección
            poblacion_ordenada,combinaciones=seleccion(self.fitness,self.poblacion)
            
            #Crossover y Mutación(escoje dos al azar y los cambia de lugar)
            poblacion_nueva=[]
            for t in range(0,int(len(poblacion_ordenada)/2)):
                hijo1,hijo2=crossover(poblacion_ordenada[combinaciones[t]],poblacion_ordenada[combinaciones[t+1]])
                #Mutacion
                poblacion_nueva.append(mutacion(hijo1))
                poblacion_nueva.append(mutacion(hijo2))
            
            self.poblacion*0
            self.poblacion=poblacion_nueva
