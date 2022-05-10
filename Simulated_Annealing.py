import random
from itertools import permutations 
import math
import copy 
import time


class SimulatedAnnealing():
    def __init__(self,stops_list,cost_list,temp_in):
        self.stops_list = stops_list
        self.cost_list = cost_list
        self.temp_in = temp_in
        self.it = 0
        self.temp = None
        self.current = None

    def start(self):
        random.seed(time.process_time)
        self.current = copy.deepcopy(self.stops_list)
        next = copy.deepcopy(self.current)
        best=copy.deepcopy(self.current)
        cost_best=self.path_cost(best)
        it=[]
        camino=[]
        probabilidad=[]
        temperatura=[]
        costo_mejor=[]
        diferencias=[]
        while True: 
            self.temp = self.temp_in - self.it
            if self.temp <= 0:
                return costo_mejor
                #return camino #para visualizar el camino y no solo los mejores en cada iteración
                #return [best, cost_best, it, camino, diferencias, probabilidad, temperatura] 
            try:
                permuts=random.sample(self.current,k=2)
                while 20000 in permuts:
                    permuts=random.sample(self.current,k=2)
                aux=copy.deepcopy(next)
                c1=True
                c2=True
                for i in range(0,len(next)):
                    if aux[i]==permuts[0] and c1:
                        c1=False
                        next[i]=permuts[1]
                    if aux[i]==permuts[1] and c2:
                        c2=False
                        next[i]=permuts[0]
            except:
                print ("Error")
                pass
            cost_current = self.path_cost(self.current)
            cost_next = self.path_cost(next)
            dif = cost_next - cost_current
            if dif < 0:
                self.current = copy.deepcopy(next)
                cost_current = cost_next
                if (cost_current < cost_best):
                    best=copy.deepcopy(self.current)
                    cost_best=cost_current
            else:
                prob = dif*random.random()
                if prob < dif*math.exp((-((self.temp_in-self.temp)/(self.temp_in)))):
                    self.current = copy.deepcopy(next)
            self.it = self.it + 1
            it.append(self.it)
            probabilidad.append(math.exp((-((self.temp_in-self.temp)/(self.temp_in)))))
            temperatura.append(self.temp)
            diferencias.append(dif)
            next=copy.deepcopy(self.current)
            camino.append(cost_current)
            costo_mejor.append(cost_best)
            
    def path_cost(self,path):
        cost = 0
        count = 0
        while count < len(path)-1:
            for i in self.cost_list:
                if path[0+count] == i[0] and path[1+count] == i[1]: 
                    cost = cost + i[2]
                elif path[0+count] == i[1] and path[1+count] == i[0]:
                    cost = cost + i[2]
            count = count + 1
        return cost