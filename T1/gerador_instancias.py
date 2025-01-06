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
from datetime import datetime as dt

#trocando folder
inst_folder = sys.argv[1]
os.chdir(inst_folder + '/')

#colocando uma seed no gerador de numeros random
rnd.seed(dt.now().timestamp()) 

#numero usado pra deslocar o
desloc = 750
desloc_div3 = desloc/3

#quantidade e tamanho das intancias, enunciado pedia por tamanho 6
inst_num = 10
inst_size = 6


for inst in range(inst_num):

    #abrindo arquivo de instancias
    with open("inst"+str(inst), 'w') as arq:

        #criando variaveis que seram usadas para calcular as coordenadas
        loc_x = 0
        loc_y = 0

        #colocando o tamanho da instancia na primeira linha
        arq.write(str(inst_size) + '\n')

        for i in range(inst_size):
                
                #numero aleatorio de -1 a 1
                loc_x = rnd.uniform(-1, 1)

                #calculando coordenada correspondente
                loc_y = (1 - loc_x**2)**0.5

                #processamento para variedade e tirar negativos para x e y
                loc_x*= desloc
                loc_x += desloc + desloc_div3 + rnd.uniform(-desloc_div3, desloc_div3)
                loc_y *= desloc
                loc_y += desloc + desloc_div3 + rnd.uniform(-desloc_div3, desloc_div3)

                #escrevendo resultado no arquivo
                arq.write(str(loc_x) + ' ' + str(loc_y) + '\n')
        
    

