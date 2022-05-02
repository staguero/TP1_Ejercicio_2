from itertools import combinations
from crear_mapa import *
from A_Star import *
from Simulated_Annealing import *
from crossover import *
import random


class Genetic_Algorithm():
    def __init__(self,n_shelfs,n_individuals,orders):
        self.n_shelfs = n_shelfs
        self.n_individuals = n_individuals
        self.orders=orders

        self.population=[]
        self.best_individual = None

    def create_individual(self):
        value = 1
        individual = [0] * self.n_shelfs
        while value < self.n_shelfs:
            pos=random.randint(0,self.n_shelfs-1)
            if individual[pos]==0:
                individual[pos]=value
                value += 1
            else:
                other_pos=individual.index(0)
                individual[other_pos]=value
                value+=1
        return individual

    def create_population(self):
        while len(self.population) < self.n_individuals:
            self.population.append(self.create_individual())

    def fitness(self,map,mapa_filas,mapa_columnas):
        global current_node,target_node
        total_cost = 0
        for order in self.orders:
            stops_list=order
            cost_list = []
            count=0
            while count < len(stops_list):
                for value in range(count+1,len(stops_list)):
                    inicio=str(stops_list[count])
                    fin=str(stops_list[value])
                    for j in range(mapa_columnas):
                        for i in range(mapa_filas):
                            if map[i][j].id is not None:
                                if map[i][j].id[5:]==inicio:
                                    current_node = map[i][j]
                                if map[i][j].id[5:]==fin:
                                    target_node = map[i][j]

                    a_star = A_Star(map,current_node,target_node)
                    a_star.start_method(mapa_columnas,mapa_filas)

                    cost_list.append([inicio,fin,a_star.path_cost])
                count = count + 1

            temp=len(stops_list)*100
            simulated_annealing = SimulatedAnnealing(stops_list,cost_list,temp) 
            lowcost_path = simulated_annealing.start()
            total_cost = lowcost_path[1] + total_cost

        return total_cost

    def selection(self,total_cost_list):
        ordered_cost=sorted(total_cost_list, reverse=True)
        ordered_population=[]
        for i in ordered_cost:
            pos=total_cost_list.index(i)
            ordered_population.append(self.population[pos])

        #Poblacion PAR
        #if len(ordered_population)%2==0:
        #    flag=int(len(ordered_population)/2)
        #    combinations=[]
        #    for j in range(2,flag+1):
        #        combinations.append(1)
        #        combinations.append(j)
        #    combinations.append(2)
        #    combinations.append(3)
        #else: 
        #    pass #POBLACION IMPAR? VER
        if len(ordered_population)%2==0:
            flag=int(len(ordered_population)/2) #trabajo con la mitad más alta
            combinations=[] #esta lista es la que entrego
            probabilities=[] #esta lista es momentanea, se genera en cada iteracion de nuevo
            for j in range(0,flag): #voy de cero hasta la mitad de la lista
               #multiplico cada fitness por un numero entre 0 y 1, lo que dijo el santi
               probabilities.append(ordered_cost[j]*random.random())
               #Itero dos veces, en donde elijo los 2 fitness más grandes y guardo sus posiciones
               for m in range(0,2):
                   max=max(probabilities) #saco el max
                   position_max=probabilities.index(max) #encuentro su posicion en la lista
                   combinations.append(position_max) #guardo esa posicion max
                   probabilities[position_max]=0 #lo hago 0 así en la 2 iteracion no lo encuentra
        
        return ordered_population,combinations

    def mutation(self,lista):
        while True:
            pos1=random.randint(0,len(lista)-1)
            pos2=random.randint(0,len(lista)-1)
            if pos1==pos2:
                pos2=random.randint(0,len(lista)-1)
            else:
                break

        aux1=lista[pos1]
        aux2=lista[pos2]

        lista[pos1]=aux2
        lista[pos2]=aux1

        return lista
        
    def start(self,n_it,columnas_estante,estantes_f,estantes_c):
        it = 0
        mapa_filas=2*estantes_f+4+(estantes_f-1)*2
        mapa_columnas=estantes_c*columnas_estante+4+(estantes_c-1)*2
        self.create_population()
        while it < n_it:
            total_cost_list = []
            for individual in self.population:
                map = crear_mapa(columnas_estante,estantes_f,estantes_c,individual)
                total_cost_list.append(self.fitness(map,mapa_filas,mapa_columnas))
            
            #Agregado este cálculo de probabilidad
            for k in range(0,len(total_cost_list)):
                total_cost_list[k]=1/total_cost_list[k]
            
            ord_population,combinations=self.selection(total_cost_list)
            new_population=[]
            self.best_individual = ord_population[0]
            for t in range(0,int(len(ord_population)/2)):
                hijo1,hijo2=crossover(ord_population[combinations[t]],ord_population[combinations[t+1]])
                new_population.append(self.mutation(hijo1))
                new_population.append(self.mutation(hijo2))
            
            self.population.clear()
            self.population = new_population