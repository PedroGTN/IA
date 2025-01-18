#   Esse gerador de instancias e baseado em um que uso na minha IC
#   ele basicamente gera um numero aleatorio entre -1 e 1 (x) e considera
#   que esta em um circulo, com isso calculo a segunda coordenada (y) correspondente
#   ai para nao ficar apenas entre -1 e 1 eu multiplico pelo numero [desloc]
#   e depois adiciono esse mesmo numero para que nao haja numeros negativos
#   entao adiciono um terco desse [desloc] e depois mais um numero aleatorio 
#   que fica entre -[desloc]/3 e [desloc]/3 para gerar variedade

import os
import sys
import random as rnd
import time
import math

#trocando folder
inst_folder = sys.argv[3]
os.chdir(inst_folder + '/')

#colocando uma seed no gerador de numeros random
rnd.seed(time.time()) 

#numero usado pra deslocar o
desloc = 750
desloc_div3 = desloc/3

#quantidade e tamanho das intancias, enunciado pedia por tamanho 6
inst_num = int(sys.argv[1])
inst_size = int(sys.argv[2])


for inst in range(inst_num):

    #abrindo arquivo de instancias
    with open("inst"+str(inst)+".in", 'w') as arq:

        #colocando o tamanho da instancia na primeira linha
        arq.write(str(inst_size) + '\n')

        for i in range(inst_size):
                
                #gerando um angulo e um raio para definir a posição do nó
                angle = rnd.uniform(0, 360)
                radius = desloc + desloc_div3 + rnd.uniform(-desloc_div3, desloc_div3)
                
                #usando seno e cosseno para definir as coordenadas x e y do nó
                loc_x = math.cos(angle) * radius
                loc_y = math.sin(angle) * radius

                #escrevendo resultado no arquivo
                arq.write(str(loc_x) + ' ' + str(loc_y) + '\n')
        
    

