import random
from itertools import permutations 
import math

class SimulatedAnnealing():
    def __init__(self,stops_list,cost_list,temp_in):
        self.stops_list = stops_list
        self.cost_list = cost_list
        self.temp_in = temp_in
        self.it = 0
        self.temp = None
        self.current = None
        self.next = None
        self.permutation_list = []

        permut = permutations(self.stops_list, len(self.stops_list)) 
        
        for i in permut:
            self.permutation_list.append(list(i))
        print("la longitud de permutaciones es:")
        print (len(self.permutation_list))

    def start(self):
        self.current = self.permutation_list[0]
        self.permutation_list.remove(self.current)
        while True:
            self.temp = self.temp_in - self.it

            if self.temp <= 0:
                return self.current

            try:
                self.next = self.permutation_list[ random.randint( 0,len(self.permutation_list)-1 ) ]
                self.permutation_list.remove(self.next)
            except:
                pass
            cost_current = self.path_cost(self.current)
            cost_next = self.path_cost(self.next)
            dif = cost_next - cost_current
            if dif < 0:
                self.current = self.next
            else:
                prob = random.random()
                if prob < math.exp(dif/self.temp):
                    self.current = self.next
            self.it = self.it + 1

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