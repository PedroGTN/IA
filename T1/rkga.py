import decoder as ddr
import sys
from datetime import datetime as dt
import random as rnd

class rkga:
    def __init__(self, time_limit, iteration_limit, inst_loc, res_loc):
        decoder = ddr.decoder(inst_loc)
        rnd.seed(dt.now().timestamp()) 
        self.time_limit = time_limit
        self.iteration_limit = iteration_limit
        self.inst_loc = inst_loc
        self.res_loc = res_loc
        self.population = [None] * 1000
        self.init_pop()

    def init_pop(self):

    def rand_crom(self):
        crom = []
        for i in range():



    def start(self):
        init_time = dt.now().second()
        curr_time = init_time
        it_counter = 0
        while():


            curr_time = dt.now().second()
            it_counter += 1
        







