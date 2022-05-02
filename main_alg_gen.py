from Genetic_Algorithm import *
from lector_ordenes import *

orders = lector_ordenes(10)
n_shelfs = 16
n_individuals = 10
object=Genetic_Algorithm(n_shelfs,n_individuals,orders)
object.start(20,2,2,2)
print(object.best_individual)