from Genetic_Algorithm import *
from lector_ordenes import *

def dibujo():
    for i in range(mapa_filas):
        print(mapa_dibujo[i])

columnas_estante=2
estantes_f=2
estantes_c=2
mapa_filas = 2*estantes_f+4+(estantes_f-1)*2
mapa_columnas= estantes_c*columnas_estante+4+(estantes_c-1)*2

orders = lector_ordenes(10)
for i in orders:
    i.insert(0,20000)
    i.append(20000)

n_shelfs = 16
n_individuals = 10
object=Genetic_Algorithm(n_shelfs,n_individuals,orders)
best_individual = object.start(10,2,2,2)
print("Mejor individuo")
print(best_individual)
mapa=crear_mapa(2,2,2,best_individual)

mapa_dibujo=[]
mapa_dibujo = [[0 for j in range(mapa_columnas)] for i in range(mapa_filas)]
for j in range(mapa_columnas):
        for i in range(mapa_filas):
            if mapa[i][j].id == "Empty":
                mapa_dibujo[i][j]="0 "
            else:
                mapa_dibujo[i][j]=mapa[i][j].id[5:]
dibujo()

