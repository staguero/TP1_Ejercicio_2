import random
from itertools import permutations 
import math
import copy 
#USO DE COPY.DEEPCOPY() PARA QUE LOS = NO APUNTEN AL MISMO ESPACIO DE MEMORIA 
#(NO SE PORQUE SUCEDE ESTO Y NO PUEDO USAR "COPY" O "[:]")

class SimulatedAnnealing():
    def __init__(self,stops_list,cost_list,temp_in):
        self.stops_list = stops_list
        self.cost_list = cost_list
        self.temp_in = temp_in
        self.it = 0
        self.temp = None
        self.current = None

    def start(self):
        self.current = copy.deepcopy(self.stops_list)
        next = copy.deepcopy(self.current)
        best=copy.deepcopy(self.current)
        cost_best=self.path_cost(best)
        while True:
            self.temp = self.temp_in - self.it
            if self.temp <= 0:
                return best 
            try:
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
                prob = random.random()
                print(self.temp)
                print(cost_current)
                print(cost_next)
                print(math.exp(-dif/self.temp))
                print()
                if prob < math.exp(-dif/self.temp):
                    self.current = copy.deepcopy(next)
            self.it = self.it + 1
            next=copy.deepcopy(self.current)

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