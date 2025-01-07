import decoder as ddr
import sys
import time
import random as rnd
import math

class rkga:
    def __init__(self, time_limit, iteration_limit, inst_loc, res_loc):
        rnd.seed(time.time()) 
        self.decoder = ddr.decoder(inst_loc)
        self.best_crom = None
        self.best_crom_value = math.inf
        self.elapsed_time = 0
        self.time_limit = time_limit if time_limit != 0 else 60
        self.iteration_limit = iteration_limit if iteration_limit != 0 else math.inf
        self.inst_loc = inst_loc
        self.res_loc = res_loc
        self.pop_size = 10
        self.population = [None] * self.pop_size
        self.init_pop()

    def init_pop(self):
        for i in range(self.pop_size):
            self.population[i] = self.rand_crom()

    def rand_crom(self):
        crom = [0] * self.decoder.size
        for i in range(self.decoder.size):
            crom[i] = rnd.random()
        return crom

    def rank(self):
        pop_rank = [None] * self.pop_size

        for i in range(self.pop_size):
            pop_rank[i] = [self.decoder.decode(self.population[i]), self.population[i]]

        pop_rank.sort()

        return pop_rank

    def breed(self, pai1, pai2):
        child = [0] * self.decoder.size

        for i in range(self.decoder.size):
            child[i] = pai1[i] if rnd.randint(0, 1) else pai2[i]

        return child


    def gen_children(self, size=3):
        new_croms = []

        for i in range(size):
            i, j = rnd.randint(0, self.pop_size-1), rnd.randint(0, self.pop_size-1)
            pai1 = self.population[i] if self.decoder.decode(self.population[i]) < self.decoder.decode(self.population[j]) else self.population[j]
            i, j = rnd.randint(0, self.pop_size-1), rnd.randint(0, self.pop_size-1)
            pai2 = self.population[i] if self.decoder.decode(self.population[i]) < self.decoder.decode(self.population[j]) else self.population[j]
            new_croms.append(self.breed(pai1, pai2))

        return new_croms

    def new_pop(self, pop_rank, new_croms, e_size=4, c_size=3, m_size=3):
        newpop = [None] * e_size 

        for i in range(e_size):
            newpop[i] = pop_rank[i][1]
        
        newpop += new_croms

        for i in range(m_size):
            newpop.append(self.rand_crom())

        return newpop

    def start(self):
        init_time = time.time()
        self.elapsed_time = init_time - init_time
        it_counter = 0
        while self.elapsed_time <= self.time_limit and it_counter < self.iteration_limit :
            
            curr_rank = self.rank()

            if curr_rank[0][0] < self.best_crom_value:
                it_counter = 0
                self.best_crom_value = curr_rank[0][0]
                self.best_crom = curr_rank[0][1]
                print("curr best value:", self.best_crom_value)
                print("curr best cromossome:", self.best_crom)
                print("\n")

            new_croms = self.gen_children()

            self.population = self.new_pop(curr_rank, new_croms)
            
            self.elapsed_time = time.time() - init_time
            it_counter += 1

        with open(self.res_loc, 'w') as arq:
            arq.write("best value: " + str(self.best_crom_value) + '\n')
            arq.write("best cromossome: ")
            for i in self.best_crom: 
                arq.write(str(i) + ' ')
            arq.write('\n')
            arq.write("elapsed time: " + str(self.elapsed_time) + '\n')

    def get_status(self):
        return [self.best_crom, self.best_crom_value, self.elapsed_time]


        







