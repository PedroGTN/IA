import sys
import rkga

time_limit = int(sys.argv[1])
iteration_limit = int(sys.argv[2])
inst_loc = sys.argv[3]
res_folder = sys.argv[4]
res_loc = res_folder + inst_loc.split('/')[-1].split('.')[0] + '_res.out'

alg = rkga.rkga(time_limit, iteration_limit, inst_loc, res_loc)

alg.start()

status = alg.get_status()

print("best value:", status[1])
print("best cromossome:", status[0])