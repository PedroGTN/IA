import sys
import rkga

#recebendo dados do usuário
time_limit = int(sys.argv[1])
iteration_limit = int(sys.argv[2])
inst_loc = sys.argv[3]
res_folder = sys.argv[4]
res_loc = res_folder + inst_loc.split('/')[-1].split('.')[0] + '_res.out' #criando nome do arquivo de saida

#criando objeto de rkga
alg = rkga.rkga(time_limit, iteration_limit, inst_loc, res_loc)

#mandando começar 
alg.start()

#recebendo o status final e printando
status = alg.get_status()
print("best value:", status[0])
print("best tour:", status[1])
print("best cromossome:", status[2])
print("elapsed time:", status[3])
print("elapsed iterations:", status[4])