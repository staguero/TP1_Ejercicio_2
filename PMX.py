import random
from copy import deepcopy

father_2 = [1,4,7,2,3,6,5]
father_1 = [4,2,5,7,3,1,6]

cut_point = random.randint(0,len(father_1)-2) #menos 2 para evitar que sea una copia igual al padre
print(cut_point)
son_1 = deepcopy(father_2)
for pos_f1,value_f1 in enumerate(father_1):
    if pos_f1 <= cut_point:
        pos_f2 = son_1.index(value_f1)
        son_1[pos_f2] = son_1[pos_f1]
        son_1[pos_f1] = value_f1

son_2 = deepcopy(father_1)
for pos_f2,value_f2 in enumerate(father_2):
    if pos_f2 <= cut_point:
        pos_f1 = son_2.index(value_f2)
        son_2[pos_f1] = son_2[pos_f2]
        son_2[pos_f2] = value_f2

print(son_1)
print(son_2)