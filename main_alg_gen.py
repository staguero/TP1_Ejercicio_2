from algoritmo_genetico import *

#columnas_estante=int(input('Cantidad de columnas por estantería: '))
#estantes_f=int(input('Cantidad de Filas de estantería: '))
#estantes_c=int(input('Cantidad de Columnas de estantería: '))
#cantidad_individuos=int(input('Cantidad de individuos: '))
#long_ordenes=int(input('Longitud de ordenes'))

columnas_estante=4
estantes_f=2
estantes_c=2

cantidad_individuos=6 #cuantos mapas voy a probar
long_ordenes=10 #cantidad de pedidos por orden

algoritmo_genetico(columnas_estante,estantes_f,estantes_c,cantidad_individuos,long_ordenes)