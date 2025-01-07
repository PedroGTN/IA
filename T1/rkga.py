import decoder as ddr
import sys
import time
import random as rnd
import math

class rkga:
    #Inicializando o objeto com valores de limite de tempo,
    #limite de iteracoes e localizacao dos arquivos necessarios
    def __init__(self, time_limit, iteration_limit, inst_loc, res_loc):
        rnd.seed(time.time()) #inicializando rng com uma seed
        self.decoder = ddr.decoder(inst_loc) #criando objeto do decoder

        #criando valores de status do final do algoritmo
        self.best_crom = None
        self.best_crom_value = math.inf
        self.elapsed_time = 0

        #inicializando as variaveis com base nos valores supridos
        self.time_limit = time_limit if time_limit != 0 else 60
        self.iteration_limit = iteration_limit if iteration_limit != 0 else math.inf
        self.inst_loc = inst_loc
        self.res_loc = res_loc

        #inicializando populacao
        self.pop_size = 10
        self.population = [None] * self.pop_size
        self.init_pop()

    #inicializa a populacao
    def init_pop(self):
        for i in range(self.pop_size):
            self.population[i] = self.rand_crom()

    #cria um cromossomo aleatorio
    def rand_crom(self):
        crom = [0] * self.decoder.size
        for i in range(self.decoder.size):
            crom[i] = rnd.random()
        return crom

    #faz o rank da populacao com base no valor do decoder
    def rank(self):
        pop_rank = [None] * self.pop_size

        for i in range(self.pop_size):
            pop_rank[i] = [self.decoder.decode(self.population[i]), self.population[i]]

        pop_rank.sort()

        return pop_rank

    #faz o cruzamento de dois pais gerando um filho
    def breed(self, pai1, pai2):
        child = [0] * self.decoder.size

        for i in range(self.decoder.size):
            child[i] = pai1[i] if rnd.randint(0, 1) else pai2[i]

        return child

    #gera um vetor de filhos baseado na pop atual
    def gen_children(self, size=3):
        new_croms = []

        #seleciona dois pais aleatorios da pop e fica com o melhor, faz o mesmo uma 
        #segunda vez, assim selecionando os pais que seram usados na funcao breed
        for i in range(size):
            i, j = rnd.randint(0, self.pop_size-1), rnd.randint(0, self.pop_size-1)
            pai1 = self.population[i] if self.decoder.decode(self.population[i]) < self.decoder.decode(self.population[j]) else self.population[j]
            i, j = rnd.randint(0, self.pop_size-1), rnd.randint(0, self.pop_size-1)
            pai2 = self.population[i] if self.decoder.decode(self.population[i]) < self.decoder.decode(self.population[j]) else self.population[j]
            new_croms.append(self.breed(pai1, pai2))

        return new_croms

    #cria uma populacao nova com elites, filhos e mutantes (cromossomos randos)
    def new_pop(self, pop_rank, new_croms, e_size=4, c_size=3, m_size=3):
        newpop = [None] * e_size 

        for i in range(e_size):
            newpop[i] = pop_rank[i][1]
        
        newpop += new_croms

        for i in range(m_size):
            newpop.append(self.rand_crom())

        return newpop

    #loop principal do programa
    def start(self):
        #cria variaveis de controle 
        init_time = time.time()
        self.elapsed_time = init_time - init_time
        it_counter = 0

        #loop principal
        while self.elapsed_time <= self.time_limit and it_counter < self.iteration_limit :
            #rankeada a pop
            curr_rank = self.rank()

            #verifica se houve melhora
            if curr_rank[0][0] < self.best_crom_value:
                it_counter = 0 #reset de iteracoes sem melhora
                self.best_crom_value = curr_rank[0][0]
                self.best_crom = curr_rank[0][1]
                print("curr best value:", self.best_crom_value)
                print("curr best cromossome:", self.best_crom)
                print("\n")

            #cria novos filhos baseados na pop atual
            new_croms = self.gen_children()

            #gera a nova pop
            self.population = self.new_pop(curr_rank, new_croms)
            
            #atualiza as variaveis de controle
            self.elapsed_time = time.time() - init_time
            it_counter += 1

        #escreve os resultados em um arquivo
        with open(self.res_loc, 'w') as arq:
            arq.write("best value: " + str(self.best_crom_value) + '\n')
            arq.write("best cromossome: ")
            for i in self.best_crom: 
                arq.write(str(i) + ' ')
            arq.write('\n')
            arq.write("elapsed time: " + str(self.elapsed_time) + '\n')

    #retorna os status em um array
    def get_status(self):
        return [self.best_crom, self.best_crom_value, self.elapsed_time]


        







